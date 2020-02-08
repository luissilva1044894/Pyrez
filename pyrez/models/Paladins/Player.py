from pyrez.models import PlayerPS
from pyrez.models import Ranked
from pyrez.enumerations import Tier
class Player(PlayerPS):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.platform = kwargs.get("Platform", '') or ''
        self.rankedController = kwargs.get("RankedController", None)
        if self.rankedController and isinstance(self.rankedController, dict):
            self.rankedController = Ranked(**self.rankedController)
        self.rankedKeyboard = kwargs.get("RankedKBM", None)
        if self.rankedKeyboard and isinstance(self.rankedKeyboard, dict):
            self.rankedKeyboard = Ranked(**self.rankedKeyboard)
        self.playerRankController = Tier(kwargs.get("Tier_RankedController", 0)) or None
        self.playerRankKeyboard = Tier(kwargs.get("Tier_RankedKBM", 0)) or None
