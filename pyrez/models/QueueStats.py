from datetime import datetime
from .APIResponse import APIResponse
from pyrez.enumerations import Champions, Gods
from pyrez.models.Mixin import KDA, Player as PlayerMixin, Winratio
class QueueStats(APIResponse, KDA, PlayerMixin, Winratio):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)#super().__init__(**kwargs)
        KDA.__init__(self, **kwargs)
        PlayerMixin.__init__(self, **kwargs)
        Winratio.__init__(self, **kwargs)
        try:
            self.godId = Champions(kwargs.get("ChampionId")) if kwargs.get("ChampionId") else Gods(kwargs.get("GodId"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("GodId", kwargs.get("ChampionId", 0)) or 0
            self.godName = kwargs.get("God", kwargs.get("Champion", '')) or ''
        self.gold = kwargs.get("Gold", 0) or 0
        self.lastPlayed = kwargs.get("LastPlayed", None) or None
        if self.lastPlayed:
            self.lastPlayed = datetime.strptime(self.lastPlayed, "%m/%d/%Y %I:%M:%S %p")
        self.matches = kwargs.get("Matches", 0) or 0
        self.minutes = kwargs.get("Minutes", 0) or 0
        self.queue = kwargs.get("Queue", '') or ''
