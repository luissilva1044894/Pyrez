
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

#from .decorators import *
from .http import *
from .loop import *

class Info:
  @property
  def aiohttp(self):
    try:
      import aiohttp
    except ImportError:
      return
    else:
      return aiohttp.__version__
  @property
  def os(self):
    import platform
    #return '{platform.system} {platform.release} {platform.version}'.format(platform=platform.uname())
    return platform.platform()
  @property
  def pyrez(self):
    from ..__version__ import version_info
    #return '{ver.major}.{ver.minor}.{ver.micro}-{ver.releaselevel}'.format(ver=version_info)
    return version_info
  @property
  def python(self):
    import sys
    #return '{py.major}.{py.minor}.{py.micro}-{py.releaselevel}'.format(py=sys.version_info)
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
  def collect(self):
    __packages__ = []

    __packages__.append(f'{self.python_implementation}: {self.python}')
    __packages__.append(f'OS: {self.os}')
    __packages__.append(f'requests: {self.requests}')
    __packages__.append(f'aiohttp: {self.aiohttp}')

    uvloop = self.uvloop
    if uvloop:
      __packages__.append(f'uvloop: {uvloop}')
    rapidjson = self.rapidjson
    if rapidjson:
      __packages__.append(f'rapidjson: {rapidjson}')
    ujson = self.ujson
    if ujson:
      __packages__.append(f'ujson: {ujson}')
    return __packages__
  def __str__(self):
    return '\n'.join(self.collect())

if __name__ == '__main__':
  print(Info())

def ___(_, __, _____=None, *, api=None):
  if isinstance(_, str):
    try:
      return __(_, api=api)
    except (TypeError, ValueError) as exc:
      print(exc, _)
  if isinstance(_, list):
    __r__ = [__(api=api, **____) for ____ in (_ or []) if ____]
    if __r__ and len(__r__) < 2:
      return __r__[0]
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
  return None

__all__ = (
	'auth',
	'decorators',
	'http',
	'loop',
	'num',
	'sys',
	'time',
)
