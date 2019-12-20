
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class Portal(Enum):
  UNKNOWN = 0
  HIREZ = 1
  HIREZ = '1'
  HIREZ = 'pc'
  HIREZ = 'hirez'
  HIREZ = 'hi-rez'
  STEAM = 5
  STEAM = '5'
  STEAM = 'steam'
  PS4 = 9
  PS4 = '9'
  PS4 = 'ps4'
  PS4 = 'psn'
  PTS = 'pts'
  XBOX = 10
  XBOX = '10'
  XBOX = 'xboxlive'
  XBOX = 'xbox'
  MIXER = 14
  MIXER = '14'
  MIXER = 'mixer'
  NINTENDO_SWITCH = 22
  NINTENDO_SWITCH = '22'
  NINTENDO_SWITCH = 'switch'
  NINTENDO_SWITCH = 'nintendo_switch'
  DISCORD = 25
  DISCORD = '25'
  DISCORD = 'discord'

__all__ = (
  'PortalId',
)
