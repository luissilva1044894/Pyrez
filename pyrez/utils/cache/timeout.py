
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

class Timeout(object):
  """docstring for Timeout"""
  def __init__(self, *args, **kw):
    super(Timeout, self).__init__()
    self.__expires_at__ = kw.pop('timeout', 0)
  @property
  def needs_refresh(self):
    from datetime import datetime
    return datetime.utcnow() >= self.__expires_at__
