
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

"""
class Platform(Enum):
  WINDOWS = 'WIN'
  MAC = 'MAC'
  PLAYSTATION = 'PSN'
  XBOX = 'XBL'
  SWITCH = 'SWT'
  IOS = 'IOS'
  ANDROID = 'AND'
"""

from . import Enum
class Portal(Enum):
  UNKNOWN = 0
  HIREZ = 1
  HIREZ = 'hi-rez'
  HIREZ = 'pc'
  STEAM = 5
  PLAY_STATION = 9
  PLAY_STATION = 'playstation'
  PLAY_STATION = 'ps4'
  PLAY_STATION = 'psn'
  PTS = 'pts'
  PTS = 'public_test_server'
  XBOX = 10
  XBOX = 'xb'
  XBOX = 'xb1'
  XBOX = 'xbl'
  XBOX = 'xbox_one'
  XBOX = 'xbox1'
  XBOX = 'xboxlive'
  MIXER = 14
  NINTENDO_SWITCH = 22
  NINTENDO_SWITCH = 'switch'
  NINTENDO_SWITCH = 'swt'
  DISCORD = 25
  PALADINS_STRIKE = 'paladinsstrike'
  PALADINS_STRIKE = 'mobile'
  PALADINS_STRIKE = 'ios'
  PALADINS_STRIKE = 'and'
  PALADINS_STRIKE = 'android'
  FACEBOOK = 'facebook'
  FACEBOOK = 'facebookpaladins'
  GOOGLE = 'google'
  TWITCH = 'twitch'

  def icon(self, c=None):
    if self not in [Portal.UNKNOWN, Portal.PTS]:
      __url__ = f'https://hirez-api-docs.herokuapp.com/.assets/logos/{self.name.lower().replace("ps4", "psn").replace("_", "-")}.png'
      if c:
        from ..utils.http import img_download
        return img_download(__url__, c)
      return __url__

  def oauth_url(self, api=None, param=None):
    value = {Portal.FACEBOOK:'facebook', Portal.GOOGLE:'google', Portal.HIREZ:'hirez', Portal.STEAM:'steam', Portal.PLAY_STATION:'playstation', Portal.XBOX:'xbox', Portal.NINTENDO_SWITCH:'switch', Portal.DISCORD:'discord'}.get(self)
    if value:
      from .endpoint import Endpoint
      return f'{api or Endpoint.HIREZ}/oauth/{"" if self == Portal.HIREZ else "out/"}{value}?{"redirect_uri" if self == Portal.HIREZ else "url"}={param or ""}'

__all__ = (
  'Portal',
)
