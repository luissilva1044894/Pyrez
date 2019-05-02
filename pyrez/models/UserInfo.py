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
        linkedPortalAccounts = kwargs.get("linkedPortalAccounts", None) if kwargs else None
        linkedCredentials = kwargs.get("linkedCredentials", None) if kwargs else None
        games = kwargs.get("games", None) if kwargs else None
        self.linkedPortalAccounts, self.linkedCredentials, self.games = [], [], []
        for obj in linkedPortalAccounts if linkedPortalAccounts else []:
            self.linkedPortalAccounts.append(LinkedAccount(**obj))
        for obj in linkedCredentials if linkedCredentials else []:
            self.linkedCredentials.append(LinkedAccount(**obj))
        for obj in games if games else []:
            self.games.append(Game(**obj))
