
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from datetime import datetime
import json

from ..utils.num import num_or_string

def __check__(k, v):
  if isinstance(v, (list, tuple)):
    for _ in v:
      if str(_).lower() in str(k).lower():
        return True
  return str(v).lower() in str(k).lower()
class Dict(dict):
  def __init__(self, **kw):
    """It can act both as a dictionary (c['foo']) and as an object (c.foo) to get values."""
    dict.__init__(self, kw or {})
    self.__kw__ = kw or {}
  '''
  def get(self, key, default=None):
    return self.__kw__.get(key, default)
  '''
  def __getattr__(self, key):
    if key not in self.__dict__:
      _value = self.json.get(key)
      if _value:
        if __check__(key, ['avg', 'gold', 'id', 'kills', 'level', 'losses', 'price', 'rating', 'rank', 'score', 'xp', 'win']):
          return num_or_string(_value)
        if __check__(key, ['date', 'dt', 'finished', 'started', 'time']):
          try:
            return datetime.strptime(_value, '%m/%d/%Y %I:%M:%S %p')
          except (TypeError, ValueError):
            pass
      return _value
    #return super().__getattr__(key)

  def __getitem__(self, key):
    try:
      return self.json[key]
    except (KeyError, AttributeError):
      pass

  def __str__(self):
    return str(self.to_json())

  def to_json(self):
    return json.dumps(self.json or {}, ensure_ascii=False, sort_keys=False, separators=(',', ':'), indent=None)
    #from ...utils.json import dumps
    #dumps(self.__kw__ or {}, ensure_ascii=False, sort_keys=False, separators=(',', ':'), indent=2)

  @property
  def json(self):
    return self.__kw__ or self.__dict__

class APIResponse(Dict):
  """Represents a generic Pyrez object. This is a super-class for all Pyrez models.

  Keyword Arguments
  -----------------
  error_msg:
    The message returned from the API request.
  json:
    The request as JSON, if you prefer.
  """
  def __init__(self, **kw):
    # self.content
    # self.headers
    # self.status
    self.__api__ = kw.pop('api', None)
    super().__init__(**kw)

  @property
  def ret_msg(self):
    return self.json.get('ret_msg') or self.json.get('error') or self.json.get('errors')

  @property
  def has_msg(self):
    return self.ret_msg is not None
