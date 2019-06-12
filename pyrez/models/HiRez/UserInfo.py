from pyrez.models import APIResponseBase
from .ContactInfo import ContactInfo
from .LinkedAccount import LinkedAccount
from .PortalAccount import PortalAccount
from .Game import Game
class UserInfo(APIResponseBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accountId = kwargs.get("accountId", 0) if kwargs else 0
        self.contactInfo = ContactInfo(**kwargs.get("contactInfo", None)) if kwargs else None
        self.name = kwargs.get("name", None) if kwargs else None
        self.createdDate = kwargs.get("createdDate", None) if kwargs else None
        self.verifiedDate = kwargs.get("verifiedDate", None) if kwargs else None
        self.verified = kwargs.get("verified", False) if kwargs else False
        self.banned = kwargs.get("banned", False) if kwargs else False
        self.gameAccessFlags = kwargs.get("gameAccessFlags", 0) if kwargs else 0
        self.isAffiliate = kwargs.get("isAffiliate", False) if kwargs else False
        self.language = kwargs.get("language", None) if kwargs else None
        self.languageId = kwargs.get("languageId", 0) if kwargs else 0
        self.region = kwargs.get("region", False) if kwargs else False
        self.vip = kwargs.get("vip", False) if kwargs else False
        self.linkedPortalAccounts = [ PortalAccount(**_) for _ in (kwargs.get("linkedPortalAccounts", None) or []) ]
        self.linkedCredentials = [ LinkedAccount(**_) for _ in (kwargs.get("linkedCredentials", None) or []) ]
        self.games = [ Game(**_) for _ in (kwargs.get("games", None) or []) ]
