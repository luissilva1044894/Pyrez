
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ..utils.http import Client

class _Base(object):
  @classmethod
  def Async(cls, *args, **kw):
    return cls(is_async=True, *args, **kw)

class Base(_Base):
  '''
  @classmethod
  def Async(cls, headers=None, cookies=None, raise_for_status=True, logger_name=None, debug_mode=True, loop=None):
    return cls(headers=headers, cookies=cookies, raise_for_status=raise_for_status, logger_name=logger_name, debug_mode=debug_mode, is_async=True, loop=loop)
  '''
  def __init__(self, *args, **kw):
    self._session_ = Client(logger_name=kw.pop('logger_name', self.__class__.__name__), *args, **kw)
  def __enter__(self, *args, **kw):
    self.http.__enter__(*args, **kw)
    return self
  def __exit__(self, *args, **kw):
    self.http.__exit__(*args, **kw)
  async def __aenter__(self, *args, **kw):
    await self.http.__aenter__(*args, **kw)
    return self
  async def __aexit__(self, *args, **kw):
    return await self.http.__aexit__(*args, **kw)#self.close()
  @property
  def debug_mode(self):
    return self.http.debug_mode
  @property
  def http(self):
    return self._session_
  @property
  def is_async(self):
    return self.http.is_async
  @property
  def logger(self):
    return self.http.logger
  @property
  def loop(self):
    return self.http.loop
