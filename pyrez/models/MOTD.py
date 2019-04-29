from .APIResponse import APIResponse
class MOTD(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description = kwargs.get("description", None) if kwargs is not None else None
        self.gameMode = kwargs.get("gameMode", None) if kwargs is not None else None
        self.maxPlayers = kwargs.get("maxPlayers", 0) if kwargs is not None else 0
        self.name = kwargs.get("name", None) if kwargs is not None else None
        self.startDateTime = kwargs.get("startDateTime", None) if kwargs is not None else None
        self.team1GodsCSV = kwargs.get("team1GodsCSV", None) if kwargs is not None else None
        self.team2GodsCSV = kwargs.get("team2GodsCSV", None) if kwargs is not None else None
        self.title = kwargs.get("title", None) if kwargs is not None else None
