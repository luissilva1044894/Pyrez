
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class Region(Enum):
  UNKNOWN = ''
  AUSTRALIA = 1
  AUSTRALIA = 'au'
  AUSTRALIA = 'aus'
  AUSTRALIA = 'oce'
  AUSTRALIA = 'oceania'
  BRAZIL = 2
  BRAZIL = 'br'
  BRAZIL = 'bra'
  BRAZIL = 'brasil'
  EUROPE = 3
  EUROPE = 'eu'
  LATIN_AMERICA_NORTH = 4
  LATIN_AMERICA_NORTH = 'latam'
  NORTH_AMERICA = 5
  NORTH_AMERICA = 'na'
  SOUTHEAST_ASIA = 6
  SOUTHEAST_ASIA = 'sea'
  SOUTHEAST_ASIA = 'asia'
  JAPAN = 7
  JAPAN = 'japan'
  JAPAN = 'jp'
  JAPAN = 'jpn'

  #NAEAST  = 'NAE'
  #NAWEST  = 'NAW'
  #CHINA   = 'CN'
  #MIDDLEEAST = 'ME'

__all__ = (
  'Region',
)
