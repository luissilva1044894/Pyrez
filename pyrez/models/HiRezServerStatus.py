from .APIResponse import APIResponse
class HiRezServerStatus(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entryDateTime = kwargs.get("entry_datetime", None) if kwargs is not None else None
        self.limitedAccess = kwargs.get("limited_access", False) if kwargs is not None else False
        self.platform = kwargs.get("platform", None) if kwargs is not None else None
        self.status = str(kwargs.get("status", None).upper()) == "UP"
        self.version = kwargs.get("version", None) if kwargs is not None else None
    def __str__(self):
        return "entry_datetime: {0} platform: {1} status: {2} version: {3}".format(self.entryDateTime, self.platform, "UP" if self.status else "DOWN", self.version)
