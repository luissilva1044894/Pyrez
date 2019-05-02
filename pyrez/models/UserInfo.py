from .APIResponse import APIResponse
from .ContactInfo import ContactInfo
from .LinkedAccount import LinkedAccount
from .Game import Game
class UserInfo(APIResponse):
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
        self.linkedPortalAccounts = [ LinkedAccount(**obj) for obj in (kwargs.get("linkedPortalAccounts") if kwargs.get("linkedPortalAccounts", None) else []) ]
        self.linkedCredentials = [ LinkedAccount(**obj) for obj in (kwargs.get("linkedCredentials") if kwargs.get("linkedCredentials", None) else []) ]
        self.games = [ Game(**obj) for obj in (kwargs.get("games") if kwargs.get("games", None) else []) ]
