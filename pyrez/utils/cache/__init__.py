
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

def fix_name(obj):
  if hasattr(obj, '__class__'):
    if str(obj.__class__).rfind('function') == -1:
      return obj.__class__.__name__.upper()
  if hasattr(obj, '__name__'):
    return obj.__name__.upper()
  return str(obj).upper()
def fix_key(obj):
  return str(obj).upper()
def get_value(obj):
  if hasattr(obj, 'value'):
    return obj.value
  return obj

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
    self._defaults, _timeout = {}, kw.pop('timeout', None) or 10
    from ..file import get_path
    self.root_path = f'{get_path(root=True)}\\data'
    if not self.exists: self._cache = kw.pop('cache', None) or {}
    else: self.read()
    if not 'timeout' in self._defaults:
      self.set_defaults('timeout', _timeout)
  def has_key(self, key):
    return fix_key(key) in self._cache.keys()
  def __getitem__(self, key):
    return self.get(key)
  def get(self, key, silent=True, **kw):
    if kw.get('sub_key'):
      if silent:
        __x__ = self._cache.get(fix_key(key))
        if __x__:
          if ',' in kw.get('sub_key'):
            _key, _sub = kw.get('sub_key').split(',', 1)
            return __x__.get(fix_key(_key), {}).get(fix_key(_sub))
          return __x__.get(fix_key(kw.get('sub_key')))
        return None
      return self._cache[fix_key(key)][fix_key(kw.get('sub_key'))]
    if silent:
      return self._cache.get(fix_key(key))
    return self._cache[fix_key(key)]#get_value(self._cache[fix_key(key)])
  def set(self, key, value, **kw):
    from .data import Data
    if not self.has_key(fix_key(key)):
      self._cache[fix_key(key)] = {}
    if kw.get('sub_key'):
      if ',' in kw.get('sub_key'):
        _key, _sub = kw.get('sub_key').split(',', 1)
        if not self._cache[fix_key(key)].get(fix_key(_key)):
          self._cache[fix_key(key)][fix_key(_key)] = {}
        self._cache[fix_key(key)][fix_key(_key)][fix_key(_sub)] = Data(_sub, value, timeout=kw.pop('timeout', self._defaults['TIMEOUT']), **kw)
      else:
        self._cache[fix_key(key)][fix_key(kw.get('sub_key'))] = Data(kw.get('sub_key'), value, timeout=kw.pop('timeout', self._defaults['TIMEOUT']), **kw)
    else:
      self._cache[fix_key(key)] = Data(key, value, timeout=kw.pop('timeout', self._defaults['TIMEOUT']), **kw)
    # self.__[key] = Timeout(timeout=kw.pop('timeout', self._defaults['TIMEOUT']), **kw)
  @property
  def last_update(self):
    """Returns the time that the parent file was last updated."""
    import os
    from datetime import datetime
    return datetime.fromtimestamp(os.path.getmtime(self.filename))
  def wants_update(self, key, _cls, sub_key=None, *, force=False):
    if force:
      return force
    if self.has_key(_cls):
      if hasattr(self.get(_cls, sub_key=key), 'needs_refresh'):
        return self.get(_cls, sub_key=key).needs_refresh
      if sub_key:
        if hasattr(self.get(_cls, sub_key=f'{key},{sub_key}'), 'needs_refresh'):
          return self.get(_cls, sub_key=f'{key},{sub_key}').needs_refresh
        return not self.get(_cls, sub_key=f'{key},{sub_key}')
      return not self.get(_cls, sub_key=key)
    return not self.has_key(_cls) or key not in self._defaults.get(_cls, {}).keys() or self._defaults.get(_cls, {}).get(key, {}).get('optional')
  @property
  def filename(self):
    return f'{self.root_path}\\cache.json'
  @property
  def exists(self):
    '''Returns True if a matching cache exists in the current directory.'''
    import os
    return os.path.isfile(self.filename)
  def save(self):
    from ..file import write_file
    from ..json import JSONEncoder
    import json
    write_file(self.filename, json.dumps(self, cls=JSONEncoder, ensure_ascii=False))#, 'wb+'
  def from_json(self, filename, silent=False):
    import json
    try:
      with open(filename) as f:#, 'rb'
        #return self.from_mapping(json.loads(f.read()))
        r = json.loads(f.read())
        if isinstance(r, str):
          r = json.loads(r)
        self._defaults = r.get('_defaults', self._defaults)
        self._cache = r.get('_cache', self._cache if hasattr(self, '_cache') else {})
        for _ in self._cache:
          for __ in self._cache[_]:
            from .data import Data
            if isinstance(self._cache[_], dict):
              for ___ in self._cache[_][__]:
                if 'key' in self._cache[_][__][___]:
                  self._cache[_][__][___] = Data.from_json(self._cache[_][__][___])
            if 'key' in self._cache[_][__]:
              self._cache[_][__] = Data.from_json(self._cache[_][__])
    except (FileNotFoundError, IsADirectoryError, IOError, json.decoder.JSONDecodeError) as e:
      import errno
      if not silent and not e.errno in (errno.ENOENT, errno.EISDIR):
        e.strerror = 'Unable to load configuration file (%s)' % e.strerror
        raise
  def read(self):
    self.from_json(self.filename, True)
  def set_defaults(self, name, value, key=None):
    if isinstance(name, (list, tuple)):
      for _ in name:
        self.set_defaults(_, value)
    if key:
      self._defaults[fix_key(key)][fix_key(name)] = value
    else:
      self._defaults[fix_key(name)] = value
  @staticmethod
  def defaults(method, optional=False, **options):
    def decorator(f):
      import functools
      @functools.wraps(f)
      def decorated_function(*args, **kw):
        for _ in [method] if not isinstance(method, (list, tuple)) else method:
          if not fix_name(args[0]) in Cache.instance._defaults.keys():
            Cache.instance._defaults[fix_name(args[0])] = {}
          if not _ in Cache.instance._defaults[fix_name(args[0])]:
            #print(f'f: {f}\nmethod: {_}\noptional: {optional}\noptions: {options}')
            from boolify import boolify
            #Cache.instance._defaults[fix_name(args[0])][_] = {**{'optional': kw.pop('optional', boolify(optional))}, **options}
            Cache.instance.set_defaults(_, {**{'optional': kw.pop('optional', boolify(optional))}, **options}, fix_name(args[0]))
            Cache.instance.save()
        return f(*args, **kw)
      return decorated_function
    return decorator
if not hasattr(globals(), 'cache'):
  #http://aprenda-python.blogspot.com/2012/11/singleton-simples-em-python.html
  cache = Cache()
'''
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
'''
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
