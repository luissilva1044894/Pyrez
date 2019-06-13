from pyrez.models import APIResponseBase
class LinkedAccount(APIResponseBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accountId = kwargs.get("accountId", 0) or 0
        self.copied = kwargs.get("copied", False) or False
        self.gamerTag = kwargs.get("gamerTag", '') or ''
        self.platform = kwargs.get("platform", '') or ''
