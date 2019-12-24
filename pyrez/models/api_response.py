
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

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
      try:
        return self.json[key]
      except (KeyError, AttributeError):
        pass
    #return super().__getattr__(key)

  def __getitem__(self, key):
    try:
      return self.json[key]
    except (KeyError, AttributeError):
      pass

  def __str__(self):
    return str(self.to_json())

  def to_json(self):
    import json
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
    self.error_msg = kw.get('ret_msg') or kw.get('error') or kw.get('errors') or None
    super().__init__(**kw)

  @property
  def has_error(self):
    return self.error_msg is not None
