from .APIResponse import APIResponse
class PatchInfo(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gameVersion = kwargs.get("version_string", kwargs.get("version", None)) if kwargs else None
        self.gameVersionCode = kwargs.get("version_code", None) if kwargs else None
        self.gameVersionId = kwargs.get("version_id", 0) if kwargs else 0
