from .APIResponse import APIResponse
from pyrez.models.Mixin import Player as PlayerMixin
class Player(APIResponse, PlayerMixin):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)
        PlayerMixin.__init__(self, **kwargs)
        self.steamId = kwargs.get("steam_id", 0) if kwargs else 0
