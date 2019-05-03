from .APIResponse import APIResponse
from pyrez.models.Mixin import MatchId
class DemoDetails(APIResponse, MatchId):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)
        MatchId.__init__(self, **kwargs)
        self.banId1 = kwargs.get("BanId1", 0) if kwargs else 0
        self.banId2 = kwargs.get("BanId2", 0) if kwargs else 0
        self.banId3 = kwargs.get("BanId3", 0) if kwargs else 0
        self.banId4 = kwargs.get("BanId4", 0) if kwargs else 0
        self.entryDatetime = kwargs.get("Entry_Datetime", None) if kwargs else None
        self.matchTime = kwargs.get("Match_Time", 0) if kwargs else 0
        self.offlineSpectators = kwargs.get("Offline_Spectators", 0) if kwargs else 0
        self.queueId = kwargs.get("Queue", 0) if kwargs else 0
        self.realtimeSpectators = kwargs.get("Realtime_Spectators", 0) if kwargs else 0
        self.recordingEnded = kwargs.get("Recording_Ended", None) if kwargs else None
        self.recordingStarted = kwargs.get("Recording_Started", None) if kwargs else None
        self.team1AvgLevel = kwargs.get("Team1_AvgLevel", 0) if kwargs else 0
        self.team1Gold = kwargs.get("Team1_Gold", 0) if kwargs else 0
        self.team1Kills = kwargs.get("Team1_Kills", 0) if kwargs else 0
        self.team1Score = kwargs.get("Team1_Score", 0) if kwargs else 0
        self.team2AvgLevel = kwargs.get("Team2_AvgLevel", 0) if kwargs else 0
        self.team2Gold = kwargs.get("Team2_Gold", 0) if kwargs else 0
        self.team2Kills = kwargs.get("Team2_Kills", 0) if kwargs else 0
        self.team2Score = kwargs.get("Team2_Score", 0) if kwargs else 0
        self.winningTeam = kwargs.get("Winning_Team", 0) if kwargs else 0
