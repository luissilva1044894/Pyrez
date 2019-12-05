
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

def fix_name(obj):
  if hasattr(obj, '__class__'):
    if str(obj.__class__).rfind('function') == -1:
      return obj.__class__.__name__.lower()
  if hasattr(obj, '__name__'):
    return obj.__name__.lower()
  return str(obj).lower()

from ..singleton import Singleton
class Cache(Singleton):
  """https://gist.github.com/lalzada/3938daf1470a3b7ed7d167976a329638"""
  '''
  def __init__(self, *args, **kw):
    """Virtually private constructor."""
    #https://gist.github.com/pazdera/1098129
    if not hasattr(Cache, 'instance'):
      Cache.instance = self
      self._defaults, self._cache = {}, {}
    else: raise Exception
  '''
  def init(self, *args, **kw):
    #https://stackoverflow.com/a/11517201
    self._defaults, self._cache, _timeout = {}, kw.pop('cache', None) or {}, kw.pop('timeout', None) or 10
    from ..file import root_path
    self.root_path = root_path(__file__, __name__)
    self.set_defaults('timeout', _timeout)
    self.from_json('cache.json', True) # < ValueError: not enough values to unpack (expected 2, got 1)
  def has_key(self, key):
    return key in self._cache.keys()
  def get(self, key, silent=True):
    if silent:
      return self._cache.get(key)
    return self._cache[key]
  def set(self, key, value, **kw):
    # self.__[key] = Timeout(timeout=kw.pop('timeout', self._defaults['timeout']), **kw)
    self._cache[key] = value
  def save(self):
    from ..file import write_file
    from ..json import JSONEncoder
    import json
    write_file(f'{self.root_path}\\cache.json', json.dumps(self, cls=JSONEncoder, ensure_ascii=False))
  def from_json(self, filename, silent=False):
    import json
    import os
    filename = os.path.join(self.root_path, filename) #self.root_path / filename
    try:
      with open(filename) as f:
        #return self.from_mapping(json.loads(f.read()))
        r = json.loads(f.read())
        self._defaults = r.get('_defaults', self._defaults)
        self._cache = r.get('_cache', self._cache)
        self.root_path = r.get('root_path', self.root_path)
    except (FileNotFoundError, IsADirectoryError, IOError) as e:
      import errno
      if not silent and not e.errno in (errno.ENOENT, errno.EISDIR):
        e.strerror = 'Unable to load configuration file (%s)' % e.strerror
        raise
  def from_mapping(self, *mapping, **kw):
    mappings = []
    if len(mapping) == 1:
      if hasattr(mapping[0], 'items'):
        mappings.append(mapping[0].items())
      else:
        mappings.append(mapping[0])
    elif len(mapping) > 1:
      raise TypeError('expected at most 1 positional argument, got %d' % len(mapping))
    mappings.append(kw.items())
    for mapping in mappings:
      for (k, v) in mapping:
        setattr(self, k.lower(), self[k])
  def set_defaults(self, name, value, key=None):
    if isinstance(name, (list, tuple)):
      for _ in name:
        self.set_defaults(_, value)
    if key:
      self._defaults[key][name] = value
    else:
      self._defaults[name] = value
  @staticmethod
  def defaults(method, optional=False, **options):
    def decorator(f):
      import functools
      @functools.wraps(f)
      def decorated_function(*args, **kw):
        if not fix_name(args[0]) in Cache.instance._defaults.keys():
          Cache.instance._defaults[fix_name(args[0])] = {}
        if not method in Cache.instance._defaults[fix_name(args[0])]:
          print(f'f: {f}\nmethod: {method}\noptional: {optional}\noptions: {options}')
          from boolify import boolify
          #Cache.instance._defaults[fix_name(args[0])][method] = {**{'optional': kw.pop('optional', boolify(optional))}, **options}
          Cache.instance.set_defaults(method, {**{'optional': kw.pop('optional', boolify(optional))}, **options}, fix_name(args[0]))
          Cache.instance.save()
        return f(*args, **kw)
      return decorated_function
    return decorator
  @staticmethod
  def cache(f=None, **options):
    def decorator(f):
      import functools
      @functools.wraps(f)
      def decorated_function(*args, **kw):
        if not fix_name(args[0]) in Cache.instance._cache.keys():
          Cache.instance._cache[fix_name(args[0])] = {}
        if not f.__name__ in Cache.instance._cache[fix_name(args[0])]:
          from datetime import datetime
          Cache.instance._cache[fix_name(args[0])][f.__name__] = (args[1] if len(args) > 1 else None) or kw.pop('v', None)
          Cache.instance._cache[fix_name(args[0])]['updated'] = datetime.utcnow()
        return Cache.instance._cache[fix_name(args[0])][fix_name(f)]
      return decorated_function
    if f:
      return decorator(f)
    return decorator
if not hasattr(globals(), 'cache'):
  #http://aprenda-python.blogspot.com/2012/11/singleton-simples-em-python.html
  cache = Cache()

'''
class Cache(object):
  def __new__(cls, *args, **kw):
    if not hasattr(cls, '__instance__'):
      cls.__instance__ = super(Cache, cls).__new__(cls, *args, **kw)
    return cls.__instance__
  def __init__(self, *args, **kw):
    self._defaults = kw.pop('defaults', None) or {}
    # self._defaults = {'timeout': kw.pop('timeout', 600)}
    self._cache = kw.pop('cache', None) or {}
    # self.__ = {}
  def __str__(self):
    if hasattr(self, '__instance__'):
      return self.__instance__.__repr__()
    return super().__str__()
  def has_key(self, key):
    return key in self._cache.items()#self.__.items()
  def set(self, key, value, **kw):
    # self.__[key] = Timeout(timeout=kw.pop('timeout', self._defaults['timeout']), **kw)
    self._cache[key] = value
  @staticmethod
  
  @staticmethod
  def cache(f=None, **options):
    def decorator(f):
      import functools
      @functools.wraps(f)
      def decorated_function(*args, **kw):
        #if not hasattr(Cache, '__instance__'):
        #  Cache()
        # Aqui ler do disco
        if not Cache.__instance__.has_key(args[0].__class__.__name__):
          Cache.__instance__.set(args[0].__class__.__name__, {})
        if force or not Cache.__instance__[args[0].__class__.__name__].has_key(f.__name__) or Cache.__instance__[args[0].__class__.__name__][f.__name__].needs_refresh:
          r = f(*args, **kw) #Provavelmenten é coroutine
          Cache.__instance__[args[0].__class__.__name__][f.__name__] = Data(timeout=kw.pop('timeout', self._defaults['timeout']), **r)
          #return r
        return Cache.__instance__[args[0].__class__.__name__].get(f.__name__)
        
      return decorated_function
    if f:
      return decorator(f)
    return decorator
'''
