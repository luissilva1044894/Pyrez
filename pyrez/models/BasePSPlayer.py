from .BasePlayer import BasePlayer
from .MergedPlayer import MergedPlayer
from .Ranked import Ranked
from .Winratio import Winratio
from pyrez.enumerations import Tier
class BasePSPlayer(BasePlayer, Winratio):
    def __init__(self, **kwargs):
        BasePlayer.__init__(self, **kwargs)#super().__init__(**kwargs)
        Winratio.__init__(self, **kwargs)
        self.activePlayerId = kwargs.get("ActivePlayerId", 0) if kwargs else 0
        self.hzGamerTag = kwargs.get("hz_gamer_tag", None) if kwargs else None
        self.hzPlayerName = kwargs.get("hz_player_name", None) if kwargs else None
        self.hoursPlayed = kwargs.get("HoursPlayed", 0) if kwargs else 0
        self.leaves = kwargs.get("Leaves", 0) if kwargs else 0
        self.losses = kwargs.get("Losses", 0) if kwargs else 0
        players = kwargs.get("MergedPlayers", None) if kwargs else None
        self.mergedPlayers = []
        for player in players if players else []:
            obj = MergedPlayer(**player)
            self.mergedPlayers.append(obj)
        self.playedGods = kwargs.get("MasteryLevel", 0) if kwargs else 0
        self.playerStatusMessage = kwargs.get("Personal_Status_Message", None) if kwargs else None
        self.rankedConquest = Ranked(**kwargs.get("RankedConquest", None)) if kwargs else None
        self.teamId = kwargs.get("TeamId", 0) if kwargs else 0
        self.teamName = kwargs.get("Team_Name", None) if kwargs else None
        self.playerRank = Tier(kwargs.get("Tier_Conquest", 0)) if kwargs else 0
        self.totalAchievements = kwargs.get("Total_Achievements", 0) if kwargs else 0
        self.totalXP = kwargs.get("Total_Worshippers", 0) if kwargs else 0
        self.wins = kwargs.get("Wins", 0) if kwargs else 0
