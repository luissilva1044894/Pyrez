from .APIResponse import APIResponse
from pyrez.models.Mixin import Player as PlayerMixin
class Player(PlayerMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.steamId = kwargs.get("steam_id", 0) if kwargs else 0
