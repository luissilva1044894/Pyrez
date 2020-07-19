
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class OwnershipType(Enum):
  UNKNOWN = 0
  LOCKED = UNKNOWN
  FREE = 10148
  FREE = 'free'
  FROM_CHAMPIONS_PACK = 2
  FROM_CHAMPIONS_PACK = 'from_champions_pack'
  TRIAL = 10147
  TRIAL = 'trial'
  PURCHASED = 10145
  PURCHASED = 'purchased'
  RENTED = 10146
  RENTED = 'rented'

__all__ = (
  'OwnershipType',
)
