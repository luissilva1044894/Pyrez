
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

def fix_name(obj):
  if hasattr(obj, '__class__'):
    if str(obj.__class__).rfind('function') == -1:
      return obj.__class__.__name__
  if hasattr(obj, '__name__'):
    return obj.__name__
  return str(obj)

from .singleton import Singleton
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
    self._defaults, self._cache = {}, kw.pop('cache', None) or {}
  @staticmethod
  def set_defaults(method, optional=False, **options):
    def decorator(f):
      import functools
      @functools.wraps(f)
      def decorated_function(*args, **kw):
        print(f'f: {f}\nmethod: {method}\noptional: {optional}\noptions: {options}')
        if not fix_name(args[0]) in Cache.instance._defaults.keys():
          Cache.instance._defaults[fix_name(args[0])] = {}
        Cache.instance._defaults[fix_name(args[0])][method] = {**{'optional': kw.pop('optional', optional)}, **options}
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
