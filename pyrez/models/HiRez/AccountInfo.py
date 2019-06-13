from pyrez.models import APIResponseBase
from .UserInfo import UserInfo
class AccountInfo(APIResponseBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = kwargs.get("user", '') or ''
        self.webToken = kwargs.get("webToken", '') or ''
        self.expiration = kwargs.get("expiration", '') or ''
        self.region = kwargs.get("region", '') if kwargs else ''
        self.userInfo = UserInfo(**kwargs.get("userInfo", None)) or None
        self.host = kwargs.get("host", '') or ''
        self.origin = kwargs.get("origin", '') or ''
