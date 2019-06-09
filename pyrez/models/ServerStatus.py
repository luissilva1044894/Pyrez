from .APIResponse import APIResponse
class ServerStatus(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entryDateTime = kwargs.get('entry_datetime', None) if kwargs else None
        self.environment = kwargs.get('environment', None) if kwargs else None
        self.limitedAccess = kwargs.get('limited_access', False) if kwargs else False
        self.platform = kwargs.get("platform", None) if kwargs else None
        self.status = str(kwargs.get('status', None).upper()) == 'UP' if kwargs else False
        self.version = kwargs.get('version', None) if kwargs else None
