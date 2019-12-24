
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
class __enum_meta__(__enum__.EnumMeta):
  def __call__(cls, value, *args, **kw):
    if isinstance(value, str):
      value = value.lower().replace(' ', '_')
    if value not in cls._value2member_map_:
      from ..utils import slugify
      value = (cls._value_aliases_ if hasattr(cls, '_value_aliases_') else {}).get(slugify(value)) or {**{_.name.lower().replace('_', ''): _.value for _ in cls}, **{str(_.value): _.value for _ in cls if str(_.value).isnumeric()}}.get(slugify(value).replace('-', '').replace('_', ''), next(iter(cls)).value)
    try:
      if isinstance(value, tuple):
        return super().__call__(value[0], *args, **kw)
      return super().__call__(value, *args, **kw)
    except ValueError:
      return super().__call__(next(iter(cls)).value, *args, **kw)
class __value_alias_enum_meta__(__enum_meta__):
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
  def __eq__(self, other):
    #https://docs.python.org/3.8/library/operator.html#module-operator
    #if hasattr(other, 'value'):#`RecursionError` here
    #  return other.value == self.value and other.name == self.name
    if isinstance(other, int) or str(other).isnumeric():
      return int(other) == int(self)
    if isinstance(other, str):
      #slugify
      return str(other).lower() == str(self).lower()
    return self.id == other
    #return super().__eq__(other)#self == other
  def __add__(self, other):
    if isinstance(other, int) or str(other).isnumeric():
      return int(other) + int(self)
    return super().__add__(other)
  def __ge__(self, other):
    if isinstance(other, int) or str(other).isnumeric():
      return int(other) >= int(self)
    return super().__ge__(other)
  def __gt__(self, other):
    if isinstance(other, int) or str(other).isnumeric():
      return int(other) > int(self)
    return super().__gt__(other)
  def __le__(self, other):
    if isinstance(other, int) or str(other).isnumeric():
      return int(other) <= int(self)
    return super().__le__(other)
  def __lt__(self, other):
    if isinstance(other, int) or str(other).isnumeric():
      return int(other) < int(self)
    return super().__lt__(other)
  def __ne__(self, other):
    if isinstance(other, int) or str(other).isnumeric():
      return int(other) != int(self)
    return super().__ne__(other)
  def equal(self, other):
    return self.__eq__(other)
  def __bool__(self):
    if int(self) != -1:
      return int(self) != 0
    return super().__bool__()
  def __hash__(self):
    return hash(self.id)
  def __int__(self):
    try:
      return int(self._value_)
    except ValueError:
      pass
    return 0
  def __repr__(self):
    import os
    from boolify import boolify
    if boolify(os.environ.get('READTHEDOCS')):
      return f'{self.__class__.__name__}.{str(self._name_)}'
    return f'<{self.name}: {self.id}>'
    #return f'{self.__class__.__name__}.{str(self._name_)}'
  def __str__(self):
    return str(self.id)
  def equal(self, other):
    return self.__eq__(other)
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
  @property
  def id(self):
    if str(self._value_).isnumeric():
      return int(self)
    return str(self._value_)
  """
  @property
  def name(self):
    return str(self._name_.replace('_', ' '))
  """
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
  def __new__(cls, value, display=None):
    """https://github.com/khazhyk/osuapi/blob/89a00b5e38b5742fb7b39213d94565b54fe95200/osuapi/enums.py#L6"""
    obj = object.__new__(cls)
    obj._value_, obj._display_name_ = value, display
    return obj
  @property
  def slugify(self):
    from ..utils import slugify
    return slugify(self._display_name_)

  def __str__(self):
    return self._display_name_ or ' '.join(str(_).title() for _ in self._name_.split('_'))

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
