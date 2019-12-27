
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

def build_dependency(arg):
  if hasattr(arg, '__version__'):
    return f'{arg.__name__}/{arg.__version__}'
  return str(arg)

def build_user_agent(dependencies, **kw):
  from ..__version__ import __package_name__, __url__, __version__
  import sys
  python = f'Python/{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'
  __DEFAULT_USER_AGENT__ = f'{__package_name__} ({__url__} {__version__}) [ {python} {" ".join(build_dependency(_) for _ in (dependencies if isinstance(dependencies, (tuple, list)) else [dependencies]) if _)}]'
  if kw.get('origin'):
    return {'User-Agent': __DEFAULT_USER_AGENT__, 'Origin': kw.get('origin')}
  return {'User-Agent': __DEFAULT_USER_AGENT__}

from ..base import _Base
class Client(_Base):
  """
  Client for interacting with HTTP

  Basic Usage::
    >>> c = Client()
    >>> c.get('https://httpbin.org/get')
    <Response [200]>
  Or as a context manager::
    >>> with Client() as c:
    ...  c.get('https://httpbin.org/get')
    <Response [200]>

    >>> async with Client() as c:
    ...  await c.get('https://httpbin.org/get')
    <Response [200]>
  """
  def __init__(self, *args, **kw):
    self.is_async = kw.pop('is_async', False)
    self.__loop__ = kw.pop('loop', None)
    self.__connector__ = kw.pop('connector', None)
    self.__raise_for_status__ = kw.pop('raise_for_status', False)
    self.__loop_signal_handler__()
    self.__http_session__ = kw.pop('session', None)
    self.headers = kw.pop('headers', None) or {}
    if kw.get('user_agent'):
      #self.headers.update({'user-agent': user_agent})
      self.headers['user-agent'] = kw.pop('user_agent', None)
    if kw.get('origin'):
      self.headers['origin'] = kw.pop('origin', None)

  def __loop_signal_handler__(self):
    if hasattr(self, '__loop__') and self.__loop__:
      import signal
      try:
        self.__loop__.add_signal_handler(signal.SIGINT, lambda: self.__loop__.stop())
        self.__loop__.add_signal_handler(signal.SIGTERM, lambda: self.__loop__.stop())
      except NotImplementedError:
        pass
  @property
  def raise_for_status(self):
    return hasattr(self, '__raise_for_status__') and self.__raise_for_status__

  @property
  def connector(self):
    if self.is_async and not self.__connector__:
      import aiohttp
      import asyncio
      if not hasattr(self, '__using_context_manager__') or asyncio.get_event_loop() is not self.loop:
        return aiohttp.TCPConnector(loop=self.loop)
      return aiohttp.TCPConnector(loop=asyncio.get_event_loop())
    return self.__connector__

  @property
  def loop(self):
    if self.is_async and not hasattr(self, '__loop__') or not self.__loop__ or self.__loop__.is_closed():
      from .loop import get_running_loop
      self.__loop__ = get_running_loop()
      self.__loop_signal_handler__()
    return self.__loop__
  async def __aenter__(self):
    setattr(self, '__old_is_async__', getattr(self, 'is_async', True))
    setattr(self, '__using_context_manager__', True)
    setattr(self, 'is_async', True)
    return self
  async def __aexit__(self, *args):
    setattr(self, 'is_async', getattr(self, '__old_is_async__', False))
    if hasattr(self, '__old_is_async__'):
      del self.__old_is_async__
    if hasattr(self, '__using_context_manager__'): del self.__using_context_manager__
    if self.__loop__ and self.__loop__.is_running():
      self.__loop__.stop()
    try:
      return await self.__http_session__.close()
    except AttributeError:
      pass
    #return await self.__http_session__.__aexit__(exc_type, exc_val, exc_tb)
  def __enter__(self):
    setattr(self, '__old_is_async__', getattr(self, 'is_async', False))
    setattr(self, 'is_async', False)
    return self
  def __exit__(self, *args):
    setattr(self, 'is_async', getattr(self, '__old_is_async__', False))
    if hasattr(self, '__old_is_async__'):
      del self.__old_is_async__
  def fix_headers(self, dep):
    if 'user-agent' not in self.headers:
      self.headers = {**self.headers, **build_user_agent(dep)}
  @property
  def http_session(self):
    #https://github.com/szastupov/aiotg/blob/ff42c38b8e55b00720d0a6086576faa40e61507d/aiotg/bot.py#L581
    if not self.is_async and (not self.__http_session__ or self.__http_session__ and 'requests' not in str(self.__http_session__.__class__)):
      import requests
      self.fix_headers(f'requests/{requests.__version__}')
      return requests.Session()
    if not self.__http_session__ or 'aiohttp' in str(self.__http_session__.__class__) and self.__http_session__.closed:
      import aiohttp
      self.fix_headers(f'aiohttp/{aiohttp.__version__}')
      self.__http_session__ = aiohttp.ClientSession(connector=self.connector, loop=self.loop, raise_for_status=self.raise_for_status)
    return self.__http_session__
  def __del__(self):
    try:
      self.__http_session__.detach()
    except AttributeError:
      pass
  def request(self, method, url, **kw):
    """Makes a HTTP request: DO NOT call this function yourself - Use provided methods"""
    from json.decoder import JSONDecodeError
    from ..exceptions import PyrezException
    import io
    __buffer__, __json__, __last_exc__, __exc_cls__, __headers__, __encoding__, __chunk_size__ = io.BytesIO(), kw.pop('json', False), None, kw.pop('http_exception', PyrezException), {**self.headers, **kw.pop('headers', {})}, kw.pop('encoding', 'utf-8'), kw.pop('chunk_size', 512)
    if self.is_async:
      async def _request_(self, method, url, **kw):
        import aiohttp
        import asyncio
        for n in range(kw.pop('max_tries', 5)):
          try:
            async with self.http_session.request(method, url, headers=__headers__, **kw) as r:
              if r.headers.get('Content-Type', '').startswith('application'):
                if r.headers.get('Content-Type', '').rfind('json') != -1 or __json__:
                  try:
                    return await r.json()
                  except (JSONDecodeError, ValueError, aiohttp.ContentTypeError):
                    return await resp.text(encoding=__encoding__)
                async for chunk in r.content.iter_chunked(__chunk_size__):
                  if chunk:
                    __buffer__.write(chunk)
                if __buffer__:
                  return __buffer__
              return r.content
          except (aiohttp.ServerDisconnectedError, asyncio.TimeoutError, aiohttp.ClientConnectorError, aiohttp.ClientOSError) as exc:
            __last_exc__ = exc
            await asyncio.sleep(n)
        if __last_exc__:
          raise __exc_cls__(__last_exc__)
      return _request_(self, method, url, **kw)
    import time
    import requests
    import urllib3
    for n in range(kw.pop('max_tries', 5)):
      try:
        with self.http_session.request(method, url, stream=kw.pop('stream', False), headers=__headers__, **kw) as r:
          if r.headers.get('Content-Type', '').startswith('application'):
            if r.headers.get('Content-Type', '').rfind('json') != -1 or __json__:
              try:
                return r.json()
              except (JSONDecodeError, ValueError):
                #r.encoding = r.apparent_encoding
                return r.text
            for chunk in r.iter_content(chunk_size=__chunk_size__):
              if chunk:
                __buffer__.write(chunk)
            if __buffer__:
              return __buffer__
          return r.content
      except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError) as exc: #urllib3.connection.HTTPConnection
        __last_exc__ = exc
        time.sleep(n)
    if __last_exc__:
      raise __exc_cls__(__last_exc__)

  def get(self, url, **kw):
    return self.request('GET', url, **kw)
  def post(self, url, **kw):
    return self.request('POST', url, headers={**self.headers, **kw.pop('headers', {})}, **kw)
  def options(self, url, **kw):
    return self.request('OPTIONS', url, headers={**self.headers, **kw.pop('headers', {})}, **kw)
  def head(self, url, **kw):
    return self.request('HEAD', url, headers={**self.headers, **kw.pop('headers', {})}, **kw)
  def put(self, url, **kw):
    return self.request('PUT', url, headers={**self.headers, **kw.pop('headers', {})}, **kw)
  def patch(self, url, **kw):
    return self.request('PATCH', url, headers={**self.headers, **kw.pop('headers', {})}, **kw)
  def delete(self, url, **kw):
    return self.request('DELETE', url, headers={**self.headers, **kw.pop('headers', {})}, **kw)

def img_download(url, c=None):
  try:
    from PIL import Image
    from io import BytesIO
  except ImportError:
    pass#raise?
  else:
    if not c:
      c = Client()
    if c._is_async if hasattr(c, '_is_async') else c.is_async:
      async def __img_download__():
        return Image.open(BytesIO(await c.http.get(url) if hasattr(c, 'http') else c.get(url)))
      return __img_download__()
    return Image.open(BytesIO(c.http.get(url) if hasattr(c, 'http') else c.get(url)))
