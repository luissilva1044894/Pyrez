
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

def build_dependency(arg):
	if hasattr(arg, '__version__'):
		return f'{arg.__name__}/{arg.__version__}'
	return str(arg)

def build_user_agent(dependencies, origin=None):
	from ..__version__ import __package_name__, __url__, __version__
	import sys
	if isinstance(dependencies, list):
		dep = ' '.join(build_dependency(_) for _ in dependencies)
	else:
		dep = build_dependency(dependencies)
	python = f'Python/{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'
	__DEFAULT_USER_AGENT__ = f'{__package_name__} ({__url__} {__version__}) [{python} {dep}]'
	if origin:
		return {'User-Agent': __DEFAULT_USER_AGENT__, 'Origin': origin}
	return {'User-Agent': __DEFAULT_USER_AGENT__}

class Client:
	"""Client for interacting with HTTP"""
	def __init__(self, *args, **kw):
		import signal
		self.is_async = kw.pop('is_async', False)
		self.loop = kw.pop('loop', None)
		if not self.loop:
			from .loop import get as get_event_loop
			self.loop = get_event_loop()
		self.__http_session__ = kw.pop('session', None) or None
		self.headers = kw.pop('headers', None) or {}
		user_agent = kw.pop('user_agent', None)
		if user_agent:
			#self.headers.update({'user-agent': user_agent})
			self.headers['user-agent'] = user_agent
		try:
			self.loop.add_signal_handler(signal.SIGINT, lambda: self.loop.stop())
			self.loop.add_signal_handler(signal.SIGTERM, lambda: self.loop.stop())
		except NotImplementedError:
			pass
	async def __aenter__(self):
		self.is_async = True
		return self
	async def __aexit__(self, *args):
		await self.__http_session__.close()
	def __enter__(self):
		self.is_async = False
		return self
	def __exit__(self, *args):
		self.__http_session__.close()
	@property
	def http_session(self):
		#https://github.com/szastupov/aiotg/blob/ff42c38b8e55b00720d0a6086576faa40e61507d/aiotg/bot.py#L581
		if self.is_async:
			import aiohttp
			if not self.__http_session__ or not isinstance(self.__http_session__, aiohttp.ClientSession) or self.__http_session__.closed:
				self.__http_session__ = aiohttp.ClientSession(loop=self.loop)
			__lib__ = f'aiohttp/{aiohttp.__version__}'
		else:
			import requests
			self.__http_session__ = requests.Session()
			__lib__ = f'requests/{requests.__version__}'
		if 'user-agent' not in self.headers:
			self.headers = {**self.headers, **build_user_agent(__lib__)}
		return self.__http_session__
	def close(self):
		#if self.loop.is_running:
		#	self.loop.stop()
		try:
			return self.__http_session__.close()
		except AttributeError:
			return True
	def __del__(self):
		if self.__http_session__:
			try:
				self.__http_session__.detach()
			except AttributeError:
				pass
	def request(self, method, url, **kw):
		"""Makes a HTTP request: DO NOT call this function yourself - use provided methods"""
		from json.decoder import JSONDecodeError
		import io
		buffer, _json = io.BytesIO(), kw.pop('json', False)
		if self.is_async:
				async def _request_(self, method, url, **kw):
					import aiohttp
					import asyncio
					import io
					from json.decoder import JSONDecodeError
					for n in range(kw.pop('max_tries', 5)):
						try:
							async with self.http_session.request(method, url, **kw) as r:
								if r.headers.get('Content-Type', '').startswith('application'):
									if r.headers.get('Content-Type', '').rfind('json') or _json:
										try:
											return await r.json()
										except (JSONDecodeError, ValueError, aiohttp.ContentTypeError):
											return await resp.text(encoding=kw.get('encoding', 'utf-8'))
									async for chunk in r.content.iter_chunked(kw.get('chunk_size', 512)):
										if chunk:
											buffer.write(chunk)
									if buffer:
										return buffer
								return r.content
						except (aiohttp.ServerDisconnectedError, asyncio.TimeoutError, aiohttp.ClientConnectorError, aiohttp.ClientOSError) as exc:
							__last_exc__ = exc
							await asyncio.sleep(n)
					raise __last_exc__
				return _request_(self, method, url, **kw)
		import time
		import requests
		import urllib3
		for n in range(kw.pop('max_tries', 5)):
			try:
				with self.http_session.request(method, url, stream=kw.pop('stream', False), **kw) as r:
					if r.headers.get('Content-Type', '').startswith('application'):
						if r.headers.get('Content-Type', '').rfind('json') or _json:
							try:
								return r.json()
							except (JSONDecodeError, ValueError):
								return r.text
						for chunk in r.iter_content(chunk_size=kw.get('chunk_size', 512)):
							if chunk:
								buffer.write(chunk)
						if buffer:
							return buffer
					return r.text
			except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError) as exc: #urllib3.connection.HTTPConnection
				__last_exc__ = exc.args
				time.sleep(n)
		from ..exceptions import PyrezException
		raise PyrezException(__last_exc__)
	def get(self, url, *, headers={}, **kw):
		if self.is_async:
			async def _get_(self, url, *, headers={}, **kw):
				return await self.request('GET', url, headers={**self.headers, **headers}, **kw)
			return _get_(self, url, headers=headers, **kw)
		return self.request('GET', url, headers={**self.headers, **headers}, **kw)
