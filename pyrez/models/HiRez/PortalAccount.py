from pyrez.models import APIResponseBase
class PortalAccount(APIResponseBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.portal = kwargs.get("portal", None) if kwargs else None
        self.portalUsername = kwargs.get("portalUsername", None) if kwargs else None
        self.portalUserId = kwargs.get("portalUserId", 0) if kwargs else 0
        self.gamerTag = kwargs.get("gamerTag", None) if kwargs else None
        self.accessToken = kwargs.get("accessToken", None) if kwargs else None
        self.refreshToken = kwargs.get("refreshToken", None) if kwargs else None
        self.appId = kwargs.get("appId", None) if kwargs else None
        self.linked = kwargs.get("linked", False) if kwargs else False
