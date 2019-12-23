
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class OwnershipType(Enum):
  UNKNOWN = 0
  FREE = 1
  FREE = 'free'
  FROM_CHAMPIONS_PACK = 2
  FROM_CHAMPIONS_PACK = 'from_champions_pack'
  TRIAL = 3
  TRIAL = 'trial'
  PURCHASED = 4
  PURCHASED = 'purchased'

__all__ = (
  'OwnershipType',
)
