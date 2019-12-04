
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

class Singleton(object):
  def __new__(cls, *args, **kw):
    if not hasattr(cls, 'instance') or not cls.instance:
      cls.instance = super().__new__(cls, *args, **kw)
      #cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
      if hasattr(cls.instance, 'init'):
      	cls.instance.init(*args, **kw)
    return cls.instance
    '''
    if not hasattr(cls, 'instance'):
      instance = object.__new__(cls)
      instance.init(*args, **kw)
      setattr(cls, 'instance', instance)
    return getattr(cls, 'instance')
    '''
