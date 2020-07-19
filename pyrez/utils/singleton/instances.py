
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

class Singleton:#(type):
  """from pyrez.utils.singleton.instances import Singleton

  class SomeClass(object):
    __metaclass__ = Singleton
  class SomeClass(object, metaclass=Singleton):
    pass
  """
  _instances = {}
  def __call__(cls, *args, **kw):
    if cls not in cls._instances:
      cls._instances[cls] = super(Singleton, cls).__call__(*args, **kw)
    return cls._instances[cls]
