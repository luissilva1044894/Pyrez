from pyrez.enumerations import Champions, Gods
from datetime import datetime
from .APIResponse import APIResponse
class QueueStats(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.assists = kwargs.get("Assists", 0) if kwargs is not None else 0
        try:
            self.godId = Champions(kwargs.get("ChampionId")) if kwargs.get("ChampionId") else Gods(kwargs.get("GodId"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("GodId", kwargs.get("ChampionId", 0)) if kwargs is not None else 0
            self.godName = kwargs.get("God", kwargs.get("Champion", None))
        self.deaths = kwargs.get("Deaths", 0) if kwargs is not None else 0
        self.gold = kwargs.get("Gold", 0) if kwargs is not None else 0
        self.kills = kwargs.get("Kills", 0) if kwargs is not None else 0
        self.lastPlayed = kwargs.get("LastPlayed", None) if kwargs is not None else None
        if self.lastPlayed:
            self.lastPlayed = datetime.strptime(self.lastPlayed, "%m/%d/%Y %H:%M:%S %p")
        self.losses = kwargs.get("Losses", 0) if kwargs is not None else 0
        self.matches = kwargs.get("Matches", 0) if kwargs is not None else 0
        self.minutes = kwargs.get("Minutes", 0) if kwargs is not None else 0
        self.queue = kwargs.get("Queue", None) if kwargs is not None else None
        self.wins = kwargs.get("Wins", 0) if kwargs is not None else 0
        self.playerId = kwargs.get("player_id", 0) if kwargs is not None else 0
