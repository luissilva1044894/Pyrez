from .APIResponse import APIResponse
from pyrez.models.Mixin import Player as PlayerMixin
class Friend(APIResponse, PlayerMixin):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)
        PlayerMixin.__init__(self, **kwargs)
        self.accountId = kwargs.get("account_id", 0) if kwargs else 0
        self.avatarURL = kwargs.get("avatar_url", None) if kwargs else None
