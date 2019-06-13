from pyrez.enumerations import Champions, Gods
from pyrez.models import APIResponse
from pyrez.models.Mixin import Winratio
class GodLeaderboard(APIResponse, Winratio):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)#super().__init__(**kwargs)
        Winratio.__init__(self, **kwargs)
        try:
            self.godId = Champions(kwargs.get("champion_id")) if kwargs.get("champion_id") else Gods(kwargs.get("god_id"))
        except ValueError:
            self.godId = kwargs.get("champion_id", kwargs.get("god_id", 0)) or 0
        self.playerId = kwargs.get("player_id", 0) or 0
        self.playerName = kwargs.get("player_name", '') or ''
        self.playerRanking = kwargs.get("player_ranking", '') or ''
        self.rank = kwargs.get("rank", 0) or 0
