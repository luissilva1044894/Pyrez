
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

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
    self.debug_mode = kw.pop('debug_mode', False)
    #self.cookies = cookies or {}
    if self.debug_mode:
      self.logger = self.debug_mode = kw.pop('logger', None)
      if not self.logger:
        from ..logging import create_logger
        self.logger = create_logger(kw.pop('logger_name', None) or self.__class__.__name__)
    from ..utils.http import Client
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
