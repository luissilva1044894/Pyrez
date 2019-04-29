from pyrez.enumerations import Champions, Gods
from .APIResponse import APIResponse
class GodRank(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.assists = kwargs.get("Assists", 0) if kwargs is not None else 0
        self.deaths = kwargs.get("Deaths", 0) if kwargs is not None else 0
        try:
            self.godId = Gods(kwargs.get("god_id")) if kwargs.get("god_id") else Champions(kwargs.get("champion_id"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("god_id", kwargs.get("champion_id", 0)) if kwargs is not None else 0
            self.godName = kwargs.get("god", kwargs.get("champion", None)) if kwargs is not None else None
        self.godLevel = kwargs.get("Rank", 0) if kwargs is not None else 0
        self.gold = kwargs.get("Gold", 0) if kwargs is not None else 0
        self.kills = kwargs.get("Kills", None) if kwargs is not None else None
        self.lastPlayed = kwargs.get("LastPlayed", None) if kwargs is not None else None
        self.losses = kwargs.get("Losses", 0) if kwargs is not None else 0
        self.minionKills = kwargs.get("MinionKills", 0) if kwargs is not None else 0
        self.minutes = kwargs.get("Minutes", 0) if kwargs is not None else 0
        self.wins = kwargs.get("Wins", 0) if kwargs is not None else 0
        self.totalXP = kwargs.get("Worshippers", 0) if kwargs is not None else 0
        self.playerId = kwargs.get("player_id", 0) if kwargs is not None else 0
    def getWinratio(self, decimals=2):
        aux = self.wins + self.losses if self.wins + self.losses > 1 else 1
        winratio = self.wins / aux * 100.0
        return int(winratio) if winratio % 2 == 0 else round(winratio, decimals)
    def getKDA(self, decimals=2):
        deaths = self.deaths if self.deaths > 1 else 1
        kda = ((self.assists / 2) + self.kills) / deaths
        return int(kda) if kda % 2 == 0 else round(kda, decimals)# + "%";
