
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

class Data(dict):
  def __init__(self, *args, **kw):
    from datetime import datetime
    # self.__create_at__, self.__timeout__ = datetime.utcnow(), kw.pop('timeout', 0)
    # self._cache = kw.pop('cache', None) or {}
    self.__expires_at__ = datetime.utcnow() + kw.pop('timeout', 0) #Timeout(timeout)
    super().__init__(*args, **kw)
  def get(self, key, silent=True):
    if silent:
      return self._cache.get(key)
    return self._cache[key]
  def set(self, key, value):
    self._cache[key] = value
  @property
  def needs_refresh(self):
    from datetime import datetime
    return datetime.utcnow() >= self.__expires_at__
  def has_key(self, key):
    """Check whether the key exists."""
    return self.get(key.replace(' ', '_')) is not None
  __getitem__  = get
