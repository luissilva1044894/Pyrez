from pyrez.enumerations import Champions, Gods
from pyrez.models import MixinWinratio, APIResponse
class GodLeaderboard(APIResponse, MixinWinratio):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)#super().__init__(**kwargs)
        MixinWinratio.__init__(self, **kwargs)
        try:
            self.godId = Champions(kwargs.get("champion_id")) if kwargs.get("champion_id") else Gods(kwargs.get("god_id"))
        except ValueError:
            self.godId = kwargs.get("champion_id", kwargs.get("god_id", 0)) if kwargs else 0
        self.playerId = kwargs.get("player_id", 0) if kwargs else 0
        self.playerName = kwargs.get("player_name", None) if kwargs else None
        self.playerRanking = kwargs.get("player_ranking", None) if kwargs else None
        self.rank = kwargs.get("rank", 0) if kwargs else 0
