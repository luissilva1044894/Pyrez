from pyrez.models import APIResponse
class Player(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accountLevel = kwargs.get("AccountLevel", 0) if kwargs else 0
        self.joinedDatetime = kwargs.get("JoinedDatetime", None) if kwargs else None
        self.lastLoginDatetime = kwargs.get("LastLoginDatetime", None) if kwargs else None
        self.name = kwargs.get("Name", None) if kwargs else None
