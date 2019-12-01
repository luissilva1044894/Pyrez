
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

class Base:
	'''
	@classmethod
	def Async(cls, headers=None, cookies=None, raise_for_status=True, logger_name=None, debug_mode=True, loop=None):
		return cls(headers=headers, cookies=cookies, raise_for_status=raise_for_status, logger_name=logger_name, debug_mode=debug_mode, is_async=True, loop=loop)
	'''
	def __init__(self, *args, **kw):
		self.debug_mode = kw.pop('debug_mode', False)
		self._is_async = kw.get('is_async', False)
		#self.cookies = cookies or {}
		'''
		if self._is_async:
			from ..utils.loop import get as get_event_loop
			self.loop = loop or get_event_loop()
		'''
		self.logger_name = kw.pop('logger_name', self.__class__.__name__)
		from ..utils.http import Client
		self._session_ = Client(*args, **kw)
	@property
	def loop(self):
		return self._session_.loop
	@property
	def http(self):
		return self._session_
	def __enter__(self):
		return self
	def __exit__(self, *args):
		self._session_.close()
	async def __aenter__(self, *args):
		return self
	async def __aexit__(self, *args):
		await self._session_.close()#self.close()
