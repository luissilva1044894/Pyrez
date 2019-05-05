from pyrez.enumerations import QueueRealmRoyale
from pyrez.models import APIResponse
from .LeaderboardDetails import LeaderboardDetails
class Leaderboard(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lastUpdated = kwargs.get("last_updated", None) if kwargs else None
        try:
            self.queueId = QueueRealmRoyale(kwargs.get("queue_id"))
        except ValueError:
            self.queueId = kwargs.get("queue_id", 0) if kwargs else 0
        self.queueName = kwargs.get("queue", None) if kwargs else None
        self.leaderboards = [ LeaderboardDetails(**_) for _ in (kwargs.get("leaderboard_details", None) or []) ]
