from pyrez.enumerations import Tier
from .APIResponse import APIResponse
class Ranked(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.leaves = kwargs.get("Leaves", 0) if kwargs else 0
        self.losses = kwargs.get("Losses", 0) if kwargs else 0
        self.rankedName = kwargs.get("Name", None) if kwargs else None
        self.currentTrumpPoints = kwargs.get("Points", 0) if kwargs else 0
        self.prevRank = kwargs.get("PrevRank", 0) if kwargs else 0
        self.leaderboardIndex = kwargs.get("Rank", 0) if kwargs else 0
        self.rankStatConquest = kwargs.get("Rank_Stat_Conquest", None) if kwargs else None
        self.rankStatDuel = kwargs.get("Rank_Stat_Duel", None) if kwargs else None
        self.rankStatJoust = kwargs.get("Rank_Stat_Joust", None) if kwargs else None
        self.currentSeason = kwargs.get("Season", 0) if kwargs else 0
        self.currentRank = Tier(kwargs.get("Tier", 0)) if kwargs else None
        self.trend = kwargs.get("Trend", 0) if kwargs else 0
        self.wins = kwargs.get("Wins", 0) if kwargs else 0
        self.playerId = kwargs.get("player_id", 0) if kwargs else 0
    def getWinratio(self, decimals=2):
        winratio = self.wins / ((self.wins + self.losses) if self.wins + self.losses > 1 else 1) * 100.0
        return int(winratio) if winratio % 2 == 0 else round(winratio, decimals)
    def hasPlayedRanked(self):
        return self.currentSeason > 0 and self.wins > 0 or self.losses > 0
