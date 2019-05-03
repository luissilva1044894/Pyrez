from pyrez.models import APIResponseBase
from .LinkedAccount import LinkedAccount
class Game(APIResponseBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game = kwargs.get("game", None) if kwargs else None
        self.gameId = kwargs.get("gameId", 0) if kwargs else 0
        self.playerName = kwargs.get("playerName", None) if kwargs else None
        self.playerId = kwargs.get("playerId", 0) if kwargs else 0
        self.currency = kwargs.get("currency", None) if kwargs else None
        self.xp = kwargs.get("xp", 0) if kwargs else 0
        self.avatarId = kwargs.get("avatarId", 0) if kwargs else 0
        self.avatarURL = kwargs.get("avatarURL", None) if kwargs else None
        self.vip = kwargs.get("vip", False) if kwargs else False
        self.linkedXboxAccount = LinkedAccount(**kwargs.get("linkedXboxAccount", None)) if kwargs and kwargs.get("linkedXboxAccount", None) else None
        self.linkedPsnAccount = LinkedAccount(**kwargs.get("linkedPsnAccount", None)) if kwargs and kwargs.get("linkedXboxAccount", None) else None
        self.ownedFeaturedItems = kwargs.get("ownedFeaturedItems", None) if kwargs else None
