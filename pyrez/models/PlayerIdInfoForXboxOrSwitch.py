from .APIResponse import APIResponse
class PlayerIdInfoForXboxOrSwitch(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerName = kwargs.get("Name", None) if kwargs is not None else None
        self.gamerTag = kwargs.get("gamer_tag", None) if kwargs is not None else None
        self.platform = kwargs.get("platform", None) if kwargs is not None else None#"unknown", "xbox" or "switch"
        self.playerId = kwargs.get("player_id", 0) if kwargs is not None else 0
        self.portalUserId = kwargs.get("portal_userid", 0) if kwargs is not None else 0
