from .APIResponse import APIResponse
class ServerStatus(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entryDateTime = kwargs.get("entry_datetime", '') or ''
        self.environment = kwargs.get("environment", '') or ''
        self.limitedAccess = kwargs.get("limited_access", False) or False
        self.platform = kwargs.get("platform", '') or ''
        self.status = str(kwargs.get("status", '').upper()) == "UP" or False
        self.version = kwargs.get("version", '') or ''
