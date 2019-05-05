from .APIResponse import APIResponse
class ServerStatus(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entryDateTime = kwargs.get("entry_datetime", None) if kwargs else None
        self.limitedAccess = kwargs.get("limited_access", False) if kwargs else False
        self.platform = kwargs.get("platform", None) if kwargs else None
        self.status = str(kwargs.get("status", None).upper()) == "UP" if kwargs else False
        self.version = kwargs.get("version", None) if kwargs else None
    def __str__(self):
        return "entry_datetime: {0.entryDateTime} platform: {0.platform} status: {1} version: {0.version}".format(self, "UP" if self.status else "DOWN")
