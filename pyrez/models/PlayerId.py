from .APIResponse import APIResponse
from pyrez.models.Mixin import Player as PlayerMixin
class PlayerId(APIResponse, PlayerMixin):
	#The playerId returned is expected to be used in various other endpoints to represent the player/individual regardless of platform.
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)
        PlayerMixin.__init__(self, **kwargs)
        self.gamerTag = kwargs.get("gamer_tag", '') or ''
        self.platform = kwargs.get("platform", '') or ''#"unknown", "xbox" or "switch"
        self.portalId = kwargs.get("portal_id", 0) or 0
        self.portalName = kwargs.get("portal", '') or ''
        self.portalUserId = kwargs.get("portal_userid", 0) or 0
        self.privacyFlag = kwargs.get("privacy_flag", "") == "y"
