
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

'''
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
'''
class Data(object):
  """https://stackoverflow.com/a/1427504"""
  def __init__(self, key, value, *args, **kw):
    from datetime import datetime, timedelta
    __duration__ = kw.pop('duration', 15)
    self.expires_at = kw.pop('expires_at', None) or datetime.utcnow() + (__duration__ if isinstance(__duration__, timedelta) else timedelta(minutes=__duration__))
    self.key = key
    self.value = value
  def to_json(self):
    return { 'key': self.key, 'value': self.value, 'expires_at': self.expires_at.isoformat() }
  @staticmethod
  def from_json(obj):
    from datetime import datetime
    return Data(obj['key'], obj['value'], expires_at=datetime.fromisoformat(obj['expires_at']))
  def get(self, key, silent=True):
    if not isinstance(value, dict):
      return self.value
    if silent:
      return self.value.get(key)
    return self.value[key]
  @property
  def needs_refresh(self):
    from datetime import datetime
    return datetime.utcnow() >= self.expires_at
  def __repr__(self):
    return '<Data {%s:%s} expires at: %s>' % (self.key, self.value, self.expires_at)
