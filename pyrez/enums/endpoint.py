
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
  SMITE = 'http://api.smitegame.com/smiteapi.svc'
  HIREZ = 'https://api.hirezstudios.com'
  STATUS_PAGE = 'https://stk4xr7r1y0r.statuspage.io'
  STATUS_PAGE = 'https://status.hirezstudios.com'

  def _get(self, params=()):
    return '/'.join([self.value, '/'.join(params)])
    #return '{}{}'.format(self.id, '/{}'.format(params) if params else '')

__all__ = (
  'Endpoint',
)
