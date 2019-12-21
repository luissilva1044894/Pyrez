
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class Portal(Enum):
  UNKNOWN = 0
  HIREZ = 1
  HIREZ = 'hi-rez'
  HIREZ = 'hirez'
  HIREZ = 'pc'
  STEAM = 5
  STEAM = 'steam'
  PS4 = 9
  PS4 = 'playstation'
  PS4 = 'ps4'
  PS4 = 'psn'
  PTS = 'pts'
  XBOX = 10
  XBOX = 'xb'
  XBOX = 'xbox'
  XBOX = 'xbox_one'
  XBOX = 'xbox1'
  XBOX = 'xboxlive'
  MIXER = 14
  MIXER = 'mixer'
  NINTENDO_SWITCH = 22
  NINTENDO_SWITCH = 'nintendo_switch'
  NINTENDO_SWITCH = 'switch'
  DISCORD = 25
  DISCORD = 'discord'

  def icon(self, c=None):
    if self not in [Portal.UNKNOWN, Portal.PTS]:
      __url__ = f'https://hirez-api-docs.herokuapp.com/.assets/logos/{self.name.lower().replace("ps4", "psn").replace("_", "-")}.png'
      if c:
        from ..utils.http import img_download
        return img_download(__url__, c)
      return __url__

__all__ = (
  'Portal',
)
