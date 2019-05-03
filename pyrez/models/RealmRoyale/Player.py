from pyrez.models import BasePlayer
class Player(BasePlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.steamId = kwargs.get("steam_id", 0) if kwargs else 0
        self.portal = kwargs.get("portal", None) if kwargs else None
        self.portalId = kwargs.get("portal_id", 0) if kwargs else 0
        self.portalUserId = kwargs.get("portal_userid", 0) if kwargs else 0
