#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

from boolify import boolify
import enum as __enum__
import os

from ..utils import camel_case, slugify
from ..utils.num import num_or_string

class __enum_meta__(__enum__.EnumMeta):
  def __getitem__(cls, name):
    try:
      return cls._member_map_[name]
    except KeyError:
      return cls(name)
  def __getattr__(cls, name):
    if name == '__new_member__':
      return super(cls).__getattr__(name)
      #except StopIteration:
    try:
      return cls._member_map_[name]
    except KeyError:
      return cls(name)
class __value_alias_enum_dict__(__enum__._EnumDict):
  def __init__(self):
    super().__init__()
    self._value_aliases = {}
  def __setitem__(self, k, v):
    if k in self:
      self._value_aliases[v] = self[k]
    else:
      super().__setitem__(k, v)
class __value_alias_enum_meta__(__enum_meta__):
  def __call__(cls, value, *args, **kw):
    if isinstance(value, str):
      value = value.lower().replace(' ', '_')
    if value not in cls._value2member_map_:
      value = (cls._value_aliases_ if hasattr(cls, '_value_aliases_') else {}).get(slugify(value)) or {**{_.name.lower().replace('_', ''): _.value for _ in cls}, **{str(_.value): _.value for _ in cls if str(_.value).isnumeric()}}.get(slugify(value).replace('-', '').replace('_', ''), next(iter(cls)).value)
    try:
      if isinstance(value, tuple):
        return super().__call__(value[0], *args, **kw)
      return super().__call__(value, *args, **kw)
    except ValueError:
      return super().__call__(next(iter(cls)).value, *args, **kw)
  @classmethod
  def __prepare__(meta_cls, cls, bases):
    return __value_alias_enum_dict__()
  def __new__(meta_cls, cls, bases, class_dict):
    enum_class = super().__new__(meta_cls, cls, bases, class_dict)
    enum_class._value_aliases_ = class_dict._value_aliases
    return enum_class
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
  @classmethod
  def members(cls):
    return cls.__members__
  @classmethod
  def items(cls):
    return cls.members().items()
  @classmethod
  def values(cls):
    return cls.members().values()
  @classmethod
  def keys(cls):
    return cls.members().keys()
  @classmethod
  def find_by_name(cls, name):
    if name:
      for v, e in cls.__members__.items():
        if name.lower() == v.lower():
          return e
  def equals(self, other):
    return self.__eq__(other)
  def __add__(self, other):
    if isinstance(other, (int, float)) or str(other).isnumeric():
      return int(self) + other
    return super().__add__(other)
  def __bool__(self):
    return -1 < int(self) > 0
  def __eq__(self, other):
    #https://docs.python.org/3.8/library/operator.html#module-operator
    #https://www.python-course.eu/python3_magic_methods.php
    #if hasattr(other, 'value'):#`RecursionError` here
    #  return other.value == self.value and other.name == self.name
    if isinstance(other, (self.__class__, __enum__.Enum)) or hasattr(other, '_value_'):
      return other._value_ == self._value_
    #if isinstance(other, (int, float)) or str(other).isnumeric():
    #  return int(self) == other
    if isinstance(other, str):
      return slugify(other) == slugify(self._value_) or slugify(other) == slugify(self._name_)
    return self._value_ == other
    #return super().__eq__(other)#self == other
  def __float__(self):
    try:
      return __float__(self._value_)
    except ValueError:
      pass
    return 0
  def __floordiv__(self, other):
    if isinstance(other, (int, float)) or str(other).isnumeric():
      return int(self) // other
    return super().__floordiv__(other)
  def __ge__(self, other):
    if other.__class__ is self.__class__:
      return self._value_ >= other._value_
    if isinstance(other, (int, float)) or str(other).isnumeric():
      return int(self) >= other
    return super().__ge__(other)
  def __gt__(self, other):
    if isinstance(other, (int, float)) or str(other).isnumeric():
      return int(self) > other
    return super().__gt__(other)
  def __hash__(self):
    return hash(self.id)
  def __index__(self):
    return int(self)
  def __int__(self):
    try:
      return int(self._value_)
    except ValueError:
      pass
    return 0
  def __le__(self, other):
    if isinstance(other, (int, float)) or str(other).isnumeric():
      return int(self) <= other
    return super().__le__(other)
  def __lt__(self, other):
    if isinstance(other, (int, float)) or str(other).isnumeric():
      return int(self) < other
    return super().__lt__(other)
  def __lshift__(self, other):
    if isinstance(other, int) or str(other).isnumeric():
      return int(self) << other
    return super().__lshift__(other)
  def __mod__(self, other):
    if isinstance(other, (int, float)) or str(other).isnumeric():
      return int(self) % other
    if hasattr(super(), '__mod__'):
      return super().__mod__(other)
  def __mul__(self, other):
    if isinstance(other, (int, float)) or str(other).isnumeric():
      return int(self) * other
    return super().__mul__(other)
  def __ne__(self, other):
    if isinstance(other, (int, float)) or str(other).isnumeric():
      return int(self) != other
    return super().__ne__(other)
  def __neg__(self):
    return -int(self)
  def __pos__(self):
    return +int(self)
  def __pow__(self, other):
    if isinstance(other, (int, float)) or str(other).isnumeric():
      return int(self) ** other
    return super().__pow__(other)
  def __repr__(self):
    if boolify(os.environ.get('READTHEDOCS')):
      return f'{self.__class__.__name__}.{str(self._name_)}'
    return '<%s.%s: %s>' % (self.__class__.__name__, self._name_, self.id)
  def __sub__(self, other):
    if isinstance(other, (int, float)) or str(other).isnumeric():
      return int(self) - other
    return super().__sub__(other)
  def __str__(self):
    return str(self.id)
  def __truediv__(self, other):
    if isinstance(other, (int, float)) or str(other).isnumeric():
      return int(self) / other
    return super().__truediv__(other)
  @property
  def id(self):
    return num_or_string(self._value_)
  """
  @property
  def name(self):
    return str(self._name_.replace('_', ' '))
  """

  @property
  def title(self):
    return self._name.title()
  @property
  def upper(self):
    return str(self).upper()
  @property
  def lower(self):
    return str(self).lower()

  @property
  def slugify(self):
    return slugify(self._name_).replace('_', '-')

  @property
  def value(self):
    return self.id

class Enum(BaseEnum, metaclass=__value_alias_enum_meta__):
  @classmethod
  def switch(cls, value):
    if not isinstance(value, cls.__class__):
      raise InvalidArgument(f'You need to use the {cls.__class__} enum to switch.')
    # cls._value_ = value._value_
    # cls._name_ = value._name_

class Auto(Enum):
  """AutoValue Enum"""
  def __new__(cls):
    obj = object.__new__(cls)
    obj._value_ = len(cls.__members__)# + 1
    return obj

class Named(Enum):
  def __new__(cls, value, display=None):
    """https://github.com/khazhyk/osuapi/blob/89a00b5e38b5742fb7b39213d94565b54fe95200/osuapi/enums.py#L6"""
    obj = object.__new__(cls)
    obj._value_, obj._display_name_ = value, display
    return obj

  def __str__(self):
    return self._display_name_ or camel_case(self._name_, spacing=' ')

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
