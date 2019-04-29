from .APIResponse import APIResponse
class PlayerIdByX(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerId = kwargs.get("player_id", 0) if kwargs is not None else 0
        self.portalUserId = kwargs.get("portal_userid", 0) if kwargs is not None else 0
        self.portalName = kwargs.get("portal", None) if kwargs is not None else None
        self.portalId = kwargs.get("portal_id", 0) if kwargs is not None else 0
