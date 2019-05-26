from .APIResponse import APIResponse
from pyrez.models.Mixin import Player as PlayerMixin
class PlayerId(APIResponse, PlayerMixin):
	#The playerId returned is expected to be used in various other endpoints to represent the player/individual regardless of platform.
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)
        PlayerMixin.__init__(self, **kwargs)
        self.gamerTag = kwargs.get("gamer_tag", None) if kwargs else None
        self.platform = kwargs.get("platform", None) if kwargs else None#"unknown", "xbox" or "switch"
        self.portalId = kwargs.get("portal_id", 0) if kwargs else 0
        self.portalName = kwargs.get("portal", None) if kwargs else None
        self.portalUserId = kwargs.get("portal_userid", 0) if kwargs else 0
