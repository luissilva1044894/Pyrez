
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
  """Represents Platforms supported by the API.
  
  It is best to assume that only the following Portals are allowed for fetching players' stats:
    - Smite: 1, 5, 6, 7, 8, 9, 10 & 22.
    - Paladins: 1, 5, 9, 10, 22 & 25.
    - Realm Royale: 1, 5, 9, 10, 22 & 25 (28 somehow).
  """
  UNKNOWN = 0
  AERIA = 11
  AMAZON = 4
  APPLE = 24
  APPLE = 'ios'
  DISCORD = 25
  EPIC_GAMES = 28
  FACEBOOK = 12
  FACEBOOK = 'facebook'
  FACEBOOK_HAND_OF_THE_GODS = 21
  FACEBOOK_HAND_OF_THE_GODS = 'facebook - hand of the gods'
  FACEBOOK_PALADINS = 20
  FACEBOOK_PALADINS = 'facebookpaladins'
  FACEBOOK_PALADINS = 'facebook - paladins'
  FACEBOOK_SMITE = 19
  FACEBOOK_SMITE = 'facebook - smite'
  GAMERS_FIRST = 2
  GAMERS_FIRST = 'gamersfirst'
  GOOGLE = 13
  GOOGLE = 'gmail'
  HIREZ = 1
  HIREZ = 'hi-rez'
  HIREZ = 'pc'
  HIREZ = 'pc'
  KONGREGATE = 3
  LEVEL_UP_BRAZIL = 8
  LEVEL_UP_BRAZIL = 'levelup_brazil'
  LEVEL_UP_LATAM = 7
  LEVEL_UP_LATAM = 'levelup_latam'
  MIXER = 14
  NINTENDO_ACCOUNT_ID = 26
  NINTENDO_ACCOUNT_ID = 'nintendo_accountid'
  NINTENDO_ACCOUNT_ID = 'naid'
  NINTENDO_SWITCH = 22
  NINTENDO_SWITCH = 'nintendo'
  NINTENDO_SWITCH = 'switch'
  NINTENDO_SWITCH = 'swt'
  PALADINS_STRIKE = 17
  PALADINS_STRIKE = 'paladinsstrike'
  PALADINS_STRIKE = 'paladins_strike_mobile'
  PALADINS_STRIKE = 'mobile'
  PALADINS_STRIKE = 'and'
  PALADINS_STRIKE = 'android'
  PLAY_STATION = 9
  PLAY_STATION = 'playstation'
  PLAY_STATION = 'ps4'
  PLAY_STATION = 'psn'
  PTS = 'pts'
  PTS = 'public_test_server'
  SMITE_RIVALS = 15
  SMITE_BLITZ = 18
  SMITE_BLITZ = 'smite_blitz_mobile'
  STEAM = 5
  TUNE = 23
  TWITCH = 16
  XBOX = 10
  XBOX = 'xb'
  XBOX = 'xb1'
  XBOX = 'xbl'
  XBOX = 'xbox_one'
  XBOX = 'xbox1'
  XBOX = 'xboxlive'

  def __bool__(self):
    return self.is_supported and super().__bool__()

  def is_supported(self):
    return self in [Portal.DISCORD, Portal.HIREZ, Portal.NINTENDO_SWITCH, Portal.PLAY_STATION, Portal.STEAM, Portal.XBOX]

  def icon(self, c=None):
    if self not in [Portal.UNKNOWN, Portal.PTS]:
      __url__ = f'https://hirez-api-docs.herokuapp.com/.assets/logos/{self.slugify}.png'
      if c:
        from ..utils.http import img_download
        return img_download(__url__, c)
      return __url__

  def oauth_url(self, api=None, redirect_uri=None):
    value = {Portal.FACEBOOK:'facebook', Portal.GOOGLE:'google', Portal.TWITCH:'twitch', Portal.HIREZ:'hirez', Portal.STEAM:'steam', Portal.PLAY_STATION:'playstation', Portal.XBOX:'xbox', Portal.MIXER:'mixer', Portal.NINTENDO_SWITCH:'nintendo', Portal.DISCORD:'discord'}.get(self)
    if value:
      from .endpoint import Endpoint
      if not redirect_uri:
        redirect_uri = 'https://my.hirezstudios.com/linked-accounts'
      return f'{api or Endpoint.HIREZ}/oauth/{"" if self == Portal.HIREZ else "out/"}{value}?{"redirect_uri" if self == Portal.HIREZ else "action=link&url"}={redirect_uri}'

__all__ = (
  'Portal',
)
