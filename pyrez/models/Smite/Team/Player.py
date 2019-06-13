from pyrez.models import APIResponse
class Player(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accountLevel = kwargs.get("AccountLevel", 0) or 0
        self.joinedDatetime = kwargs.get("JoinedDatetime", '') or ''
        self.lastLoginDatetime = kwargs.get("LastLoginDatetime", '') or ''
        self.name = kwargs.get("Name", '') or ''
