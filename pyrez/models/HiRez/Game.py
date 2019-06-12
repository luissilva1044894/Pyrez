from pyrez.models import APIResponseBase
from pyrez.models.Mixin import Avatar, Player
from .LinkedAccount import LinkedAccount
class Game(APIResponseBase, Avatar, Player):
    def __init__(self, **kwargs):
        APIResponseBase.__init__(self, **kwargs)
        Avatar.__init__(self, **kwargs)
        Player.__init__(self, **kwargs)
        self.game = kwargs.get("game", None) if kwargs else None
        self.gameId = kwargs.get("gameId", 0) if kwargs else 0
        self.currency = kwargs.get("currency", None) if kwargs else None
        self.xp = kwargs.get("xp", 0) if kwargs else 0
        self.vip = kwargs.get("vip", False) if kwargs else False
        self.linkedXboxAccount = LinkedAccount(**kwargs.get("linkedXboxAccount", None)) if kwargs and kwargs.get("linkedXboxAccount", None) else None
        self.linkedPsnAccount = LinkedAccount(**kwargs.get("linkedPsnAccount", None)) if kwargs and kwargs.get("linkedXboxAccount", None) else None
        self.ownedFeaturedItems = kwargs.get("ownedFeaturedItems", None) if kwargs else None
    def __repr__(self):
        return "<Game {0.game} - {0.gameId} | Player {0.playerName} - {0.playerId}>".format(self)
