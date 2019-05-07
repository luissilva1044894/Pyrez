from pyrez.enumerations import Tier
from .APIResponse import APIResponse
from pyrez.models.Mixin import Player as PlayerMixin, Winratio
class Ranked(APIResponse, PlayerMixin, Winratio):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)#super().__init__(**kwargs)
        PlayerMixin.__init__(self, **kwargs)
        Winratio.__init__(self, **kwargs)
        self.leaves = kwargs.get("Leaves", 0) if kwargs else 0
        self.rankedName = kwargs.get("Name", None) if kwargs else None
        self.currentTrumpPoints = kwargs.get("Points", 0) if kwargs else 0
        self.prevRank = kwargs.get("PrevRank", 0) if kwargs else 0
        self.leaderboardIndex = kwargs.get("Rank", 0) if kwargs else 0
        self.rankStat = kwargs.get("Rank_Stat", 0) if kwargs else 0#mmr
        self.currentSeason = kwargs.get("Season", 0) if kwargs else 0
        self.currentRank = Tier(kwargs.get("Tier", 0)) if kwargs else None
        self.trend = kwargs.get("Trend", 0) if kwargs else 0
    def hasPlayedRanked(self):
        return self.currentSeason > 0 and self.wins > 0 or self.losses > 0
