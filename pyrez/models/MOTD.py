from .APIResponse import APIResponse
class MOTD(APIResponse):#class MatchOfTheDay
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description = kwargs.get("description", '') or ''
        self.gameMode = kwargs.get("gameMode", '') or ''
        self.maxPlayers = kwargs.get("maxPlayers", 0) or 0
        self.name = kwargs.get("name", '') or ''
        self.startDateTime = kwargs.get("startDateTime", '') or ''
        self.team1GodsCSV = kwargs.get("team1GodsCSV", '') or ''
        self.team2GodsCSV = kwargs.get("team2GodsCSV", '') or ''
        self.title = kwargs.get("title", '') or ''
