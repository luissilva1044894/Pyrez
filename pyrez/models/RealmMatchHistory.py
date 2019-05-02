from .APIResponse import APIResponse
from .RealmMatch import RealmMatch
class RealmMatchHistory(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerId = kwargs.get("id", 0) if kwargs else 0
        self.playerName = kwargs.get("name", None) if kwargs else None
        self.matches = []
        for obj in kwargs.get("matches") if kwargs.get("matches", None) else []:
            self.matches.append(RealmMatch(**obj))
        self.matches = mats
