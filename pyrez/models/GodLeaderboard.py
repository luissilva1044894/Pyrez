from pyrez.enumerations import Champions, Gods
from .APIResponse import APIResponse
class GodLeaderboard(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Champions(kwargs.get("champion_id")) if kwargs.get("champion_id") else Gods(kwargs.get("god_id"))
        except ValueError:
            self.godId = kwargs.get("champion_id", kwargs.get("god_id", 0)) if kwargs else 0
        self.losses = kwargs.get("losses", 0) if kwargs else 0
        self.playerId = kwargs.get("player_id", 0) if kwargs else 0
        self.playerName = kwargs.get("player_name", None) if kwargs else None
        self.playerRanking = kwargs.get("player_ranking", None) if kwargs else None
        self.rank = kwargs.get("rank", 0) if kwargs else 0
        self.wins = kwargs.get("wins", 0) if kwargs else 0
    def getWinratio(self, decimals=2):
        winratio = self.wins /((self.wins + self.losses) if self.wins + self.losses > 1 else 1) * 100.0
        return int(winratio) if winratio % 2 == 0 else round(winratio, decimals)
