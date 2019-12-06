
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

import enum as __enum__
class __value_alias_enum_dict__(__enum__._EnumDict):
  def __init__(self):
    super().__init__()
    self._value_aliases = {}
  def __setitem__(self, k, v):
    if k in self:
      self._value_aliases[v] = self[k]
    else:
      super().__setitem__(k, v)
class __value_alias_enum_meta__(__enum__.EnumMeta):
  @classmethod
  def __prepare__(meta_cls, cls, bases):
    return __value_alias_enum_dict__()
  def __new__(meta_cls, cls, bases, class_dict):
    enum_class = super().__new__(meta_cls, cls, bases, class_dict)
    enum_class._value_aliases_ = class_dict._value_aliases
    return enum_class
  def __call__(cls, v, *args, **kw):
    if isinstance(v, str):
      v = v.lower().replace(' ', '_')
    if v not in cls._value2member_map_:
      v = cls._value_aliases_.get(v, next(iter(cls)).value)
    return super().__call__(v, *args, **kw)
    '''
    try:
      return super().__call__(v, *args, **kw)
    except ValueError:
      return super().__call__(next(iter(cls)).value, *args, **kw)
    '''
class BaseEnum(__enum__.Enum):
  """Represents a generic enum object. This is a sub-class of :class:`enum.Enum`.

  Supported Operations:
  +-----------+---------------------------------------------+
  | Operation |                 Description                 |
  +===========+=============================================+
  | x == y    | Checks if two Enum are equal.               |
  +-----------+---------------------------------------------+
  | x != y    | Checks if two Enum are not equal.           |
  +-----------+---------------------------------------------+
  | hash(x)   | Return the Enum's hash.                     |
  +-----------+---------------------------------------------+
  | str(x)    | Returns the Enum's name with discriminator. |
  +-----------+---------------------------------------------+
  | int(x)    | Return the Enum's value as int.             |
  +-----------+---------------------------------------------+
  """
  #Unknown = 0
  #Unknown = None
  def __eq__(self, other):
    #if isinstance(other, self):
    #  return self.id == other.id
    try:
      return other == type(other)(self.id)
    except ValueError:
      pass
    return False
  def __hash__(self):
    return hash(self.id)
  def __int__(self):
    try:
      return int(self._value_)
    except ValueError:
      pass
    return -1
  def __repr__(self):
    import os
    from boolify import boolify
    if boolify(os.environ.get('READTHEDOCS')): #os.environ.get('READTHEDOCS') == 'True'
      return f'{self.__class__.__name__}.{str(self._name_)}'
    return f'{self.name} ({self.id})'
  def __str__(self):
    return str(self.id)
  def equal(self, other):
    return self.__eq__(other)
  @property
  def id(self):
    if str(self._value_).isnumeric():
      return int(self)
    return str(self._value_)
  @property
  def name(self):
    return str(self._name_.replace('_', ' '))
  @property
  def value(self):
    return self.id

class Enum(BaseEnum, metaclass=__value_alias_enum_meta__):
  def switch(cls, value):
    if not isinstance(value, cls.__class__):
      raise InvalidArgument(f'You need to use the {cls.__class__} enum to switch.')
    # cls._value_ = value._value_
    # cls._name_ = value._name_

class Named(Enum):
  """https://github.com/khazhyk/osuapi/blob/89a00b5e38b5742fb7b39213d94565b54fe95200/osuapi/enums.py#L6"""
  def __new__(cls, value, display):
    obj = object.__new__(cls)
    obj._value_ = value
    obj._display_name_ = display
    return obj
  def __str__(self):
    return self._display_name_

#from .endpoint import *
#from .format import *
__all__ = (
  'Enum',
  'endpoint',
  'format',
  #'language',
  #'portal_id',
  #'region',
  #'status',
  #'tier',
)

#queues > enum.EnumMeta