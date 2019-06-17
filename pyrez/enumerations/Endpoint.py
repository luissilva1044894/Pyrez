from .Enum import Enum
class Endpoint(Enum):
    """Representing an endpoint that you want to access to retrieve information from."""
    PALADINS = 'http://api.paladins.com/paladinsapi.svc'
    REALM_ROYALE = 'http://api.realmroyale.com/realmapi.svc'
    SMITE = 'http://api.smitegame.com/smiteapi.svc'
    HIREZ = 'https://api.hirezstudios.com'
    STATUS_PAGE = 'https://stk4xr7r1y0r.statuspage.io' #http://status.hirezstudios.com

    HAND_OF_THE_GODS = 'http://api.handofthegods.com/handofthegodsapi.svc'
    PALADINS_STRIKE = 'http://api.paladinsstrike.com/paladinsstrike.svc'

    def switch(self, endpoint):
        if not isinstance(endpoint, self):
            from ..exceptions.InvalidArgument import InvalidArgument
            raise InvalidArgument('You need to use the Endpoint enum to switch endpoints')
        self.value = endpoint
    def getEndpoint(self, _endpoint=None):
        return '{}{}'.format(self.getId(), '/{}'.format(_endpoint) if _endpoint else '')
