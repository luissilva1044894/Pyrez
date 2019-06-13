from pyrez.models import APIResponseBase
from .ContactInfo import ContactInfo
from .LinkedAccount import LinkedAccount
from .PortalAccount import PortalAccount
from .Game import Game
class UserInfo(APIResponseBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accountId = kwargs.get("accountId", 0) or 0
        self.contactInfo = ContactInfo(**kwargs.get("contactInfo", None)) or None
        self.name = kwargs.get("name", '') or ''
        self.createdDate = kwargs.get("createdDate", '') if kwargs else ''
        self.verifiedDate = kwargs.get("verifiedDate", '') if kwargs else ''
        self.verified = kwargs.get("verified", False) or False
        self.banned = kwargs.get("banned", False) or False
        self.gameAccessFlags = kwargs.get("gameAccessFlags", 0) or 0
        self.isAffiliate = kwargs.get("isAffiliate", False) or False
        self.language = kwargs.get("language", '') or ''
        self.languageId = kwargs.get("languageId", 0) or 0
        self.region = kwargs.get("region", '') or ''
        self.vip = kwargs.get("vip", False) or False
        self.linkedPortalAccounts = [ PortalAccount(**_) for _ in (kwargs.get("linkedPortalAccounts", None) or []) ]
        self.linkedCredentials = [ LinkedAccount(**_) for _ in (kwargs.get("linkedCredentials", None) or []) ]
        self.games = [ Game(**_) for _ in (kwargs.get("games", None) or []) ]
