
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class Endpoint(Enum):
  """Representing an endpoint that you want to access to retrieve information from."""
  PALADINS = 'http://api.paladins.com/paladinsapi.svc'
  REALM_ROYALE = 'http://api.realmroyale.com/realmapi.svc'
  REALM_ROYALE = 'realm'
  REALM_ROYALE = 'realmroyale'
  REALM_ROYALE = 'realm_royale_pc'
  REALM_ROYALE = 'realm_royale_ps4'
  REALM_ROYALE = 'realm_royale_switch'
  REALM_ROYALE = 'realm_royale_xbox'
  ROGUE_COMPANY = 'http://api.roguecompany.com/RoCoApi.svc'
  SMITE = 'http://api.smitegame.com/smiteapi.svc'
  SMITE = '300'
  SMITE = 'smite_pc'
  SMITE = 'smite_ps4'
  SMITE = 'smite_switch'
  SMITE = 'smite_xbox'
  HIREZ = 'https://api.hirezstudios.com'
  HIREZ = 'hirez_public_apis'
  STATUS_PAGE = 'https://stk4xr7r1y0r.statuspage.io'
  STATUS_PAGE = 'https://status.hirezstudios.com'

  def _get(self, params=()):
    return '/'.join([self.value, '/'.join(params)])
    #return '{}{}'.format(self.id, '/{}'.format(params) if params else '')

  @property
  def refer_a_friend(self):
    if self == Endpoint.SMITE:
      return 'https://smitegame.com/play-for-free?ref='
    if self == Endpoint.PALADINS:
      return 'https://paladins.com/play-for-free?ref='

__all__ = (
  'Endpoint',
)
