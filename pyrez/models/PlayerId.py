from .APIResponse import APIResponse
class PlayerId(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gamerTag = kwargs.get("gamer_tag", None) if kwargs else None
        self.platform = kwargs.get("platform", None) if kwargs else None#"unknown", "xbox" or "switch"
        self.playerId = kwargs.get("player_id", 0) if kwargs else 0
        self.playerName = kwargs.get("Name", None) if kwargs else None
        self.portalId = kwargs.get("portal_id", 0) if kwargs else 0
        self.portalName = kwargs.get("portal", None) if kwargs else None
        self.portalUserId = kwargs.get("portal_userid", 0) if kwargs else 0
