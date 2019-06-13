from pyrez.enumerations import Tier
from .APIResponse import APIResponse
from pyrez.models.Mixin import Player as PlayerMixin, Winratio
class Ranked(APIResponse, PlayerMixin, Winratio):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)#super().__init__(**kwargs)
        PlayerMixin.__init__(self, **kwargs)
        Winratio.__init__(self, **kwargs)
        self.leaves = kwargs.get("Leaves", 0) or 0
        self.rankedName = kwargs.get("Name", '') or ''
        self.currentTrumpPoints = kwargs.get("Points", 0) or 0
        self.prevRank = kwargs.get("PrevRank", 0) or 0
        self.leaderboardIndex = kwargs.get("Rank", 0) or 0
        self.rankStat = kwargs.get("Rank_Stat", 0) or 0#mmr
        self.currentSeason = kwargs.get("Season", 0) or 0
        self.currentRank = Tier(kwargs.get("Tier", 0)) or None
        self.trend = kwargs.get("Trend", 0) or 0
    @property
    def matches_played(self):
        return self.wins + self.losses
    @property
    def hasPlayed(self):
        return self.currentSeason > 0 and self.matches_played > 0
