from .APIResponse import APIResponse
class TeamPlayer(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accountLevel = kwargs.get("AccountLevel", 0) if kwargs is not None else 0
        self.joinedDatetime = kwargs.get("JoinedDatetime", None) if kwargs is not None else None
        self.lastLoginDatetime = kwargs.get("LastLoginDatetime", None) if kwargs is not None else None
        self.name = kwargs.get("Name", None) if kwargs is not None else None
