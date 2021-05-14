from .Enum import Enum
class Endpoint(Enum):
    """Representing an endpoint that you want to access to retrieve information from."""
    PALADINS = "https://api.paladins.com/paladinsapi.svc"
    REALM_ROYALE = "https://api.realmroyale.com/realmapi.svc"
    SMITE = "https://api.smitegame.com/smiteapi.svc"
    STATUS_PAGE = "https://stk4xr7r1y0r.statuspage.io" #http://status.hirezstudios.com

    def switch(self, endpoint):
        if not isinstance(endpoint, self.__class__):
            from ..exceptions.InvalidArgument import InvalidArgument
            raise InvalidArgument('You need to use the Endpoint enum to switch endpoints')
        self.value = endpoint
    def getEndpoint(self, _endpoint=None):
        return "{}{}".format(self.getId(), "/{}".format(_endpoint) if _endpoint else "")
