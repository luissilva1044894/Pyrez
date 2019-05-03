from pyrez.enumerations import RealmRoyaleQueue
from .APIResponse import APIResponse
from .RealmRoyaleLeaderboardDetails import RealmRoyaleLeaderboardDetails
class RealmRoyaleLeaderboard(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lastUpdated = kwargs.get("last_updated", None) if kwargs else None
        try:
            self.queueId = RealmRoyaleQueue(kwargs.get("queue_id"))
        except ValueError:
            self.queueId = kwargs.get("queue_id", 0) if kwargs else 0
        self.queueName = kwargs.get("queue", None) if kwargs else None
        self.leaderboards = [ RealmRoyaleLeaderboardDetails(**_) for _ in (kwargs.get("leaderboard_details") if kwargs.get("leaderboard_details", None) else []) ]
