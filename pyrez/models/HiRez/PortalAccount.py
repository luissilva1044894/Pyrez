from pyrez.models import APIResponseBase
class PortalAccount(APIResponseBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.portal = kwargs.get("portal", '') or ''
        self.portalUsername = kwargs.get("portalUsername", '') or ''
        self.portalUserId = kwargs.get("portalUserId", 0) or 0
        self.gamerTag = kwargs.get("gamerTag", '') or ''
        self.accessToken = kwargs.get("accessToken", '') or ''
        self.refreshToken = kwargs.get("refreshToken", '') or ''
        self.appId = kwargs.get("appId", '') or ''
        self.linked = kwargs.get("linked", False) or False
