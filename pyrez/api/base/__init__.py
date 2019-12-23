
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
    #self.cookies = cookies or {}
    if self.debug_mode:
      self.logger = self.debug_mode = kw.pop('logger', None)
      if not self.logger:
        from ...logging import create_logger
        self.logger = create_logger(kw.pop('logger_name', None) or self.__class__.__name__)
    from ...utils.http import Client
    self._session_ = Client(*args, **kw)
  @property
  def http(self):
    return self._session_
  @property
  def is_async(self):
    return self.http.is_async
  @property
  def loop(self):
    return self.http.loop
  def __enter__(self):
    return self
  def __exit__(self, *args):
    self.http.close()#self._session_.close()
  async def __aenter__(self, *args):
    return self
  async def __aexit__(self, *args):
    await self.http.close()#self.close()
