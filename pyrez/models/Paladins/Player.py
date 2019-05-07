from pyrez.models import PlayerPS
from pyrez.models import Ranked
from pyrez.enumerations import Tier
class Player(PlayerPS):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.platform = kwargs.get("Platform", None) if kwargs else None
        self.rankedController = Ranked(**kwargs.get("RankedController", None)) if kwargs else None
        self.rankedKeyboard = Ranked(**kwargs.get("RankedKBM", None)) if kwargs else None
        self.playerRankController = Tier(kwargs.get("Tier_RankedController", 0)) if kwargs else None
        self.playerRankKeyboard = Tier(kwargs.get("Tier_RankedKBM", 0)) if kwargs else None
