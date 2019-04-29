from .APIResponse import APIResponse
from .RealmMatch import RealmMatch
class RealmMatchHistory(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerId = kwargs.get("id", 0) if kwargs is not None else 0
        self.playerName = kwargs.get("name", None) if kwargs is not None else None
        mats = kwargs.get("matches", None) if kwargs is not None else None
        self.matches = []
        for i in mats if mats else []:
            obj = RealmMatch(**i)
            self.matches.append(obj)
        self.matches = mats
