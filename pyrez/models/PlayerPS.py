from .PlayerBase import PlayerBase
from .MergedPlayerMixin import MergedPlayerMixin
from .Ranked import Ranked
from pyrez.models.Mixin import Winratio
from pyrez.enumerations import Tier
class PlayerPS(PlayerBase, MergedPlayerMixin, Winratio):
    def __init__(self, **kwargs):
        PlayerBase.__init__(self, **kwargs)#super().__init__(**kwargs)
        Winratio.__init__(self, **kwargs)
        MergedPlayerMixin.__init__(self, **kwargs)
        self.activePlayerId = kwargs.get("ActivePlayerId", 0) or 0
        self.hzGamerTag = kwargs.get("hz_gamer_tag", '') or ''
        self.hzPlayerName = kwargs.get("hz_player_name", '') or ''
        self.hoursPlayed = kwargs.get("HoursPlayed", 0) or 0
        self.leaves = kwargs.get("Leaves", 0) or 0
        self.playedGods = kwargs.get("MasteryLevel", 0) or 0
        self.playerStatusMessage = kwargs.get("Personal_Status_Message", '') or ''
        self.rankedConquest = kwargs.get("RankedConquest", None)
        if self.rankedConquest and isinstance(self.rankedConquest, dict):
            self.rankedConquest = Ranked(**self.rankedConquest)
        self.teamId = kwargs.get("TeamId", 0) or 0
        self.teamName = kwargs.get("Team_Name", '') or ''
        self.playerRank = Tier(kwargs.get("Tier_Conquest", 0)) or 0
        self.totalAchievements = kwargs.get("Total_Achievements", 0) or 0
        self.totalXP = kwargs.get("Total_Worshippers", 0) or 0
    @property
    def playtime(self):
        from ..utils.datetime import Timedelta
        return str(Timedelta(self.hoursPlayed))
