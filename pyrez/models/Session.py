from datetime import datetime
from .APIResponse import APIResponse
class Session(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sessionId = kwargs.get("session_id", None) if kwargs else None
        self.timeStamp = kwargs.get("timestamp", None) if kwargs else None
        if self.timeStamp:
            self.timeStamp = datetime.strptime(self.timeStamp, "%m/%d/%Y %H:%M:%S %p")
    def isApproved(self):
        return str(self.json).lower().find("approved") != -1
