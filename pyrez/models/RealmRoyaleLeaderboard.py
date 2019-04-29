from pyrez.enumerations import RealmRoyaleQueue
from .APIResponse import APIResponse
from .RealmRoyaleLeaderboardDetails import RealmRoyaleLeaderboardDetails
class RealmRoyaleLeaderboard(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lastUpdated = kwargs.get("last_updated", None) if kwargs is not None else None
        try:
            self.queueId = RealmRoyaleQueue(kwargs.get("queue_id"))
        except ValueError:
            self.queueId = kwargs.get("queue_id", 0) if kwargs is not None else 0
        self.queueName = kwargs.get("queue", None) if kwargs is not None else None
        leaderboardDetails = kwargs.get("leaderboard_details", None) if kwargs is not None else None
        self.leaderboards = []
        for i in leaderboardDetails if leaderboardDetails else []:
            obj = RealmRoyaleLeaderboardDetails(**i)
            self.leaderboards.append(obj)
