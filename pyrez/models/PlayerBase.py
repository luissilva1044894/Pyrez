from datetime import datetime
from .APIResponse import APIResponse
from pyrez.models.Mixin import Player as PlayerMixin
class PlayerBase(APIResponse, PlayerMixin):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)
        PlayerMixin.__init__(self, **kwargs)
        self.createdDatetime = kwargs.get("Created_Datetime", kwargs.get("created_datetime", None)) or None
        if self.createdDatetime:
            self.createdDatetime = datetime.strptime(self.createdDatetime, "%m/%d/%Y %I:%M:%S %p") # len(self.createdDatetime) > 0 else datetimeX
        self.lastLoginDatetime = kwargs.get("Last_Login_Datetime", kwargs.get("last_login_datetime", None)) or None
        if self.lastLoginDatetime:
            self.lastLoginDatetime = datetime.strptime(self.lastLoginDatetime, "%m/%d/%Y %I:%M:%S %p")
        self.accountLevel = kwargs.get("Level", kwargs.get("level", 0)) or 0
        self.playerRegion = kwargs.get("Region", kwargs.get("region", '')) or ''
    @property
    def last_login(self):
        if self.lastLoginDatetime:
            from ..utils.datetime import get_seen
            return get_seen(self.lastLoginDatetime)
        return self.lastLoginDatetime
