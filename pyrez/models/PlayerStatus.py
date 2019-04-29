from pyrez.enumerations import PaladinsQueue, SmiteQueue, RealmRoyaleQueue, Status
from .APIResponse import APIResponse
class PlayerStatus(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.matchId = kwargs.get("Match", kwargs.get("match_id", 0)) if kwargs is not None else 0
        try:
            self.queueId = PaladinsQueue(kwargs.get("match_queue_id"))
        except ValueError:
            try:
                self.queueId = SmiteQueue(kwargs.get("match_queue_id"))
            except ValueError:
                try:
                    self.queueId = RealmRoyaleQueue(kwargs.get("match_queue_id"))
                except ValueError:
                    self.queueId = kwargs.get("match_queue_id", 0) if kwargs is not None else 0
        try:
            self.status = Status(kwargs.get("status_id", kwargs.get("status")))
        except ValueError:
            self.status = kwargs.get("status_id", kwargs.get("status", 0)) if kwargs is not None else 0
        self.statusMessage = kwargs.get("personal_status_message", None) if kwargs is not None else None
        self.statusString = kwargs.get("status_string", kwargs.get("status", None)) if kwargs is not None else None
