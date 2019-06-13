from pyrez.enumerations import Champions, Gods
from pyrez.models import APIResponse
from pyrez.models.Mixin import Winratio, KDA
class GodRank(APIResponse, Winratio, KDA):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)#super().__init__(**kwargs)
        Winratio.__init__(self, **kwargs)
        KDA.__init__(self, **kwargs)
        try:
            self.godId = Gods(kwargs.get("god_id")) if kwargs.get("god_id") else Champions(kwargs.get("champion_id"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("god_id", kwargs.get("champion_id", 0)) or 0
            self.godName = kwargs.get("god", kwargs.get("champion", '')) or ''
        self.godLevel = kwargs.get("Rank", 0) or 0
        self.gold = kwargs.get("Gold", 0) or 0
        self.lastPlayed = kwargs.get("LastPlayed", '') or ''
        self.minionKills = kwargs.get("MinionKills", 0) or 0
        self.minutes = kwargs.get("Minutes", 0) or 0
        self.totalXP = kwargs.get("Worshippers", 0) or 0
        self.playerId = kwargs.get("player_id", 0) or 0
