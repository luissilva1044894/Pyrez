from .APIResponse import APIResponse
from .UserInfo import UserInfo
class AccountInfo(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = kwargs.get("user", None) if kwargs else None
        self.webToken = kwargs.get("webToken", None) if kwargs else None
        self.expiration = kwargs.get("expiration", None) if kwargs else None
        self.region = kwargs.get("region", None) if kwargs else None
        self.userInfo = UserInfo(**kwargs.get("userInfo", None)) if kwargs else None
        self.host = kwargs.get("host", None) if kwargs else None
        self.origin = kwargs.get("origin", None) if kwargs else None
