from pyrez.enumerations import QueuePaladins, QueueSmite, QueueRealmRoyale, Status
from .APIResponse import APIResponse
class PlayerStatus(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.matchId = kwargs.get("Match", kwargs.get("match_id", 0)) or 0
        try:
            self.queueId = QueuePaladins(kwargs.get("match_queue_id"))
        except ValueError:
            try:
                self.queueId = QueueSmite(kwargs.get("match_queue_id"))
            except ValueError:
                try:
                    self.queueId = QueueRealmRoyale(kwargs.get("match_queue_id"))
                except ValueError:
                    self.queueId = kwargs.get("match_queue_id", 0) or 0
        try:
            self.status = Status(kwargs.get("status_id", kwargs.get("status")))
        except ValueError:
            self.status = kwargs.get("status_id", kwargs.get("status", 0)) or 0
        self.statusMessage = kwargs.get("personal_status_message", '') or ''
        self.statusString = kwargs.get("status_string", kwargs.get("status", '')) or ''
