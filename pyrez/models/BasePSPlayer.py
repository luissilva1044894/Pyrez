from .BasePlayer import BasePlayer
from .MergedPlayer import MergedPlayer
from .Ranked import Ranked
from .MixinWinratio import MixinWinratio
from .MixinMergedPlayers import MixinMergedPlayers
from pyrez.enumerations import Tier
class BasePSPlayer(BasePlayer, MixinWinratio, MixinMergedPlayers):
    def __init__(self, **kwargs):
        BasePlayer.__init__(self, **kwargs)#super().__init__(**kwargs)
        MixinWinratio.__init__(self, **kwargs)
        self.activePlayerId = kwargs.get("ActivePlayerId", 0) if kwargs else 0
        self.hzGamerTag = kwargs.get("hz_gamer_tag", None) if kwargs else None
        self.hzPlayerName = kwargs.get("hz_player_name", None) if kwargs else None
        self.hoursPlayed = kwargs.get("HoursPlayed", 0) if kwargs else 0
        self.leaves = kwargs.get("Leaves", 0) if kwargs else 0
        self.playedGods = kwargs.get("MasteryLevel", 0) if kwargs else 0
        self.playerStatusMessage = kwargs.get("Personal_Status_Message", None) if kwargs else None
        self.rankedConquest = Ranked(**kwargs.get("RankedConquest", None)) if kwargs else None
        self.teamId = kwargs.get("TeamId", 0) if kwargs else 0
        self.teamName = kwargs.get("Team_Name", None) if kwargs else None
        self.playerRank = Tier(kwargs.get("Tier_Conquest", 0)) if kwargs else 0
        self.totalAchievements = kwargs.get("Total_Achievements", 0) if kwargs else 0
        self.totalXP = kwargs.get("Total_Worshippers", 0) if kwargs else 0
