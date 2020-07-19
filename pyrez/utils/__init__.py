
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

def to_dict(obj):
  res = {}
  for key in obj:
    if type(obj[key]) is dict:
     subdict =  todict(obj[key])
     for k in subdict:
      res[k] = subdict[k]
    else:
      res[key] = obj[key]
  return res

def serialize_obj(obj):
  if hasattr(obj, 'to_dict'):
    return obj.to_dict()
  if hasattr(obj, 'to_json'):
    return obj.to_json()
  return obj.__dict__

def subscript(obj, sub, default=None):
  """Safely subscript silencing :code:`KeyError` or :code:`IndexError`, if given a default return upon failure else
  :code:`None`."""
  try:
    return obj[sub]
  except (KeyError, IndexError):
    return default

def call(func, default=None, *args, **kw):
  """Safely call a callable if fails or not callable returns the default."""
  if not callable(func):
    return default
  try:
    return func(*args, **kw)
  except:
    return default

def is_hashable(obj):
  """Determine whether `obj` can be hashed."""
  try:
    hash(obj)
    #return isinstance(obj, collections.Hashable)
  except TypeError:
    return False
  return True

def iterable(obj):
  try:
    return iter(obj)
  except Exception:
    pass
  return False

def fix_param(param, *, _join=None):
  #if isinstance(params, (list, tuple)):
    #  from datetime import datetime
    #  from enum import Enum
    #  url += f"/{'/'.join(p.strftime('yyyyMMdd') if isinstance(p, datetime) else str(p.value) if isinstance(p, Enum) or hasattr(p, 'value') else str(p) for p in params if p)}"
  #else:
    #  url += f'/{params}'
  if isinstance(param, (list, tuple)):
    #if _join: return f'{_join}'.join([fix_param(p) for p in param if p])
    return [fix_param(p) for p in param if p]
  from datetime import datetime
  from enum import Enum
  if isinstance(param, datetime):
    return param.strftime('%Y%M%d')#.strftime('yyyyMMdd')
  if hasattr(param, 'value') or isinstance(param, Enum):
    return str(param.value)
  return str(param)

def ___(_, __, _____=None, *, api=None, **kw):
  if is_instance_or_subclass(_, str) or is_instance_or_subclass(_, dict):
    try:
      if is_instance_or_subclass(_, dict):
        return __(**_, api=api) if api else __(**_)
        #'NoneType' object is not callable
      return __(_, api=api) if api else __(_)
    except (TypeError, ValueError) as exc:
      print(exc, _)
  if is_instance_or_subclass(_, list):# or is_instance_or_subclass(_, tuple):
    if __:
      if api:
        __r__ = [__(api=api, **____) for ____ in (_ or []) if ____]
      else:
        __r__ = [__(**____) for ____ in (_ or []) if ____]
    else:
      __r__ = _
    if __r__ and len(__r__) < 2:
      return __r__[0]
    if kw.get('filter_by'):
      from .num import num_or_string
      try:
        if kw.get('accepted_values'):
          __r__ = [_ for _ in __r__ if num_or_string(_[kw.get('filter_by')]) in kw.get('accepted_values', [])]# or num_or_string(_[kw.get('filter_by')]) not in kw.get('ignored_values', [])
        else:
          __r__ = [_ for _ in __r__ if num_or_string(_[kw.get('filter_by')])]
      except (KeyError, TypeError):
        pass
    if kw.get('sorted_by') or kw.get('filter_by'):
      try:
        __r__ = sorted(__r__, key=lambda x: x.get(kw.get('sorted_by')) or x.get(kw.get('filter_by')), reverse=kw.get('reverse') or False)
      except (KeyError, TypeError):
        pass
    return __r__
  '''
  try:
    return __(**_[0])
  except (IndexError, KeyError):
    return __(**_)
  except TypeError:
    pass
  '''
  if _____:
    raise _____
  return _ or None

def chunks(l, n):
  """Yield successive n-sized chunks from list.\n\nref: https://stackoverflow.com/a/312464"""
  if not n or not is_instance_or_subclass(n, int) or n <= 0:
    n = len(l)
  while l:
    chunk, l = l[:n], l[n:]
    yield chunk

  #[l[i*n:(i+1)*n] for i in range((len(l) + n - 1) / n )]

  #return [l[i:i + n] for i in range(0, len(l), n)]
  #return [l[i * n:(i + 1) * n] for i in range((len(l) + n - 1) // n )]

  #for i in range(0, len(l), n):
  #  yield l[i:i + n]

def flatten(x):
  _flatten_ = lambda l: [i for x in l for i in x]
  return _flatten_(x)
  #from functools import reduce
  #reduce(lambda x, y: x+y, x) #reduce(lambda x,y: x.extend(y) or x, x)

def ______(_, __, ___=False, **kw):
  _cls = kw.pop('cls', None)
  _chunks_ = chunks([str(_) for _ in __ if _ and str(_) != '0'], kw.pop('chunk_size', 10))
  if kw.get('loop') or ___:
    async def __p__():
      if kw.get('loop'):
        import asyncio
        return asyncio.gather(*[_(','.join(_ for _ in c), cls=_cls, **kw) for c in _chunks_], loop=kw.pop('loop', asyncio.get_event_loop()))
      return flatten([await _(','.join(_ for _ in c), cls=_cls, **kw) for c in _chunks_])
    return __p__()
  return flatten([_(','.join(_ for _ in c), cls=_cls, **kw) for c in _chunks_])

def is_instance_or_subclass(x, cls):
  """Return True if ``x`` is either a subclass or instance of ``cls``."""
  try:
    return issubclass(x, cls)
  except TypeError:
    return isinstance(x, cls)

def slugify(value):
  """Normalizes string, converts to lowercase, removes non-alpha characters, and converts spaces to hyphens.
  From: http://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename-in-python"""
  import re
  import unicodedata
  return (re.sub(r'[-\s]+', '-', re.sub(r'[^\w\s-]', '', unicodedata.normalize('NFKD', str(value)).encode('ascii', 'ignore').decode('utf-8', 'ignore'))) or value).strip().replace(' ', '-').replace("'", '').lower()

def camel_case(word, **kw):
  if kw.get('spacing'):
    return kw.pop('spacing', ' ').join(_.title() for _ in str(word).split('_'))
  return ''.join(x.capitalize() or '_' for x in str(word).split('_'))

class Info:
  def __str__(self):
    import sys
    if sys.platform == 'win32':
      return '\r\n'.join(self.collect())
    return '\n'.join(self.collect())
  __repr__ = __str__

  @property
  def arrow(self):
    try:
      import arrow
    except ImportError:
      return
    else:
      return arrow.__version__

  @property
  def aiohttp(self):
    try:
      import aiohttp
    except ImportError:
      return
    else:
      return aiohttp.__version__

  @property
  def boolify(self):
    try:
      from boolify import __version__
    except ImportError:
      return
    else:
      return __version__.__version__

  @property
  def colorama(self):
    try:
      import colorama
    except ImportError:
      return
    else:
      return colorama.__version__

  @property
  def os(self):
    import platform
    #return '{platform.system} {platform.release} {platform.version}'.format(platform=platform.uname())
    return platform.platform()

  @property
  def pyrez(self):
    from ..__version__ import __version__
    #return f'{version_info.major}.{version_info.minor}.{version_info.micro}-{version_info.releaselevel}'
    return __version__

  @property
  def python(self):
    import sys
    #from sys import version_info
    #return '{version_info.major}.{version_info.minor}.{version_info.micro}-{version_info.releaselevel}'
    return sys.version.replace('\n', '')

  @property
  def python_implementation(self):
    import platform
    return platform.python_implementation()

  @property
  def rapidjson(self):
    try:
      import rapidjson
    except ImportError:
      return
    else:
      return rapidjson.__version__

  @property
  def requests(self):
    try:
      import requests
    except ImportError:
      return
    else:
      return requests.__version__

  @property
  def uvloop(self):
    try:
      import uvloop
    except ImportError:
      return
    else:
      return uvloop.__version__

  @property
  def ujson(self):
    try:
      import ujson
    except ImportError:
      return
    else:
      return ujson.__version__

  @property
  def urllib3(self):
    try:
      import urllib3
    except ImportError:
      return
    else:
      return urllib3.__version__

  def collect(self):
    __packages__ = []

    __packages__.append(f'pyrez: {self.pyrez}')
    __packages__.append(f'{self.python_implementation}: {self.python}')
    __packages__.append(f'OS: {self.os}')

    if self.requests:
      __packages__.append(f'requests: {self.requests}')
    if self.urllib3:
      __packages__.append(f'urllib3: {self.urllib3}')
    if self.aiohttp:
      __packages__.append(f'aiohttp: {self.aiohttp}')
    if self.uvloop:
      __packages__.append(f'uvloop: {self.uvloop}')
    if self.rapidjson:
      __packages__.append(f'rapidjson: {self.rapidjson}')
    if self.ujson:
      __packages__.append(f'ujson: {self.ujson}')
    if self.arrow:
      __packages__.append(f'arrow: {self.arrow}')
    if self.boolify:
      __packages__.append(f'boolify: {self.boolify}')
    if self.colorama:
      __packages__.append(f'colorama: {self.colorama}')
    return __packages__

if __name__ == '__main__':
  print(Info())

#from .decorators import *
from .http import *
from .loop import *

__all__ = (
  'auth',
  'decorators',
  'http',
  'loop',
  'num',
  'sys',
  'time',
)
