from datetime import datetime
from pyrez.enumerations import Tier, Champions, Gods, QueuePaladins, QueueSmite
from .MatchBase import MatchBase
from pyrez.models.Mixin import Player as PlayerMixin
class LiveMatch(MatchBase, PlayerMixin):
    def __init__(self, **kwargs):
        MatchBase.__init__(self, **kwargs)
        PlayerMixin.__init__(self, **kwargs)
        self.accountLevel = kwargs.get("Account_Level", 0) or 0
        self.masteryLevel = kwargs.get("Mastery_Level", 0) or 0
        self.mapName = kwargs.get("mapGame", '') or ''
        self.playerCreated = kwargs.get("playerCreated", None) or None
        self.playerRegion = kwargs.get("playerRegion", '') or ''
        if self.playerCreated:
            self.playerCreated = datetime.strptime(self.playerCreated, "%m/%d/%Y %I:%M:%S %p")
        try:
            self.tier = Tier(kwargs.get("Tier"))
        except ValueError:
            self.tier = kwargs.get("Tier", 0) or 0
        self.tierLosses = kwargs.get("tierLosses", 0) or 0
        self.tierWins = kwargs.get("tierWins", 0) or 0
        try:
            self.godId = Champions(kwargs.get("ChampionId")) if kwargs.get("ChampionId") else Gods(kwargs.get("GodId"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("ChampionId", kwargs.get("GodId", 0)) or 0
            self.godName = kwargs.get("ChampionName", kwargs.get("GodName", '')) or ''
        try:
            self.queue = QueuePaladins(kwargs.get("Queue")) if kwargs.get("ChampionId") else QueueSmite(kwargs.get("Queue"))
        except ValueError:
            self.queue = kwargs.get("Queue", 0) or 0
    def getMapName(self, _clear=False):
        return self.mapName.replace("LIVE ", '').replace("Practice ", '').replace(" (Onslaught)", '').replace(" (Onslaught) ", '').replace(" (TDM)", '').replace(" (TDM) ", '').replace("Ranked ", '') if self.mapName and _clear else self.mapName#.replace("'", '')
    @property
    def region(self):
        return str(self.playerRegion)[:2] if self.playerRegion and len(str(self.playerRegion)) >= 2 else self.playerRegion
