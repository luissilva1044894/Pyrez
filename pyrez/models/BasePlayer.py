from datetime import datetime
from .AbstractPlayer import AbstractPlayer
class BasePlayer(AbstractPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.createdDatetime = kwargs.get("Created_Datetime", kwargs.get("created_datetime", None)) if kwargs else None
        if self.createdDatetime:
            self.createdDatetime = datetime.strptime(self.createdDatetime, "%m/%d/%Y %H:%M:%S %p") # len(self.createdDatetime) > 0 else datetimeX
        self.lastLoginDatetime = kwargs.get("Last_Login_Datetime", kwargs.get("last_login_datetime", None)) if kwargs else None
        if self.lastLoginDatetime:
            self.lastLoginDatetime = datetime.strptime(self.lastLoginDatetime, "%m/%d/%Y %H:%M:%S %p")
        self.accountLevel = kwargs.get("Level", kwargs.get("level", 0)) if kwargs else 0
        self.playerRegion = kwargs.get("Region", kwargs.get("region", None)) if kwargs else None
