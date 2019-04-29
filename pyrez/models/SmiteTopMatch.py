from .APIResponse import APIResponse
class SmiteTopMatch(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ban1Id = kwargs.get("Ban1Id", 0) if kwargs is not None else 0
        self.ban1Name = kwargs.get("Ban1", None) if kwargs is not None else None
        self.ban2Id = kwargs.get("Ban2Id", 0) if kwargs is not None else 0
        self.ban2Name = kwargs.get("Ban2", None) if kwargs is not None else None
        self.entryDatetime = kwargs.get("Entry_Datetime", None) if kwargs is not None else None
        self.liveSpectators = kwargs.get("LiveSpectators", 0) if kwargs is not None else 0
        self.matchId = kwargs.get("Match", 0) if kwargs is not None else 0
        self.matchTime = kwargs.get("Match_Time", 0) if kwargs is not None else 0
        self.offlineSpectators = kwargs.get("OfflineSpectators", 0) if kwargs is not None else 0
        self.queueName = kwargs.get("Queue", None) if kwargs is not None else None
        self.recordingFinished = kwargs.get("RecordingFinished", None) if kwargs is not None else None
        self.recordingStarted = kwargs.get("RecordingStarted", None) if kwargs is not None else None
        self.team1AvgLevel = kwargs.get("Team1_AvgLevel", 0) if kwargs is not None else 0
        self.team1Gold = kwargs.get("Team1_Gold", 0) if kwargs is not None else 0
        self.team1Kills = kwargs.get("Team1_Kills", 0) if kwargs is not None else 0
        self.team1Score = kwargs.get("Team1_Score", 0) if kwargs is not None else 0
        self.team2AvgLevel = kwargs.get("Team2_AvgLevel", 0) if kwargs is not None else 0
        self.team2Gold = kwargs.get("Team2_Gold", 0) if kwargs is not None else 0
        self.team2Kills = kwargs.get("Team2_Kills", 0) if kwargs is not None else 0
        self.team2Score = kwargs.get("Team2_Score", 0) if kwargs is not None else 0
        self.winningTeam = kwargs.get("WinningTeam", 0) if kwargs is not None else 0
