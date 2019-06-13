from .APIResponse import APIResponse
class PatchInfo(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gameVersion = kwargs.get("version_string", kwargs.get("version", '')) or ''
        self.gameVersionCode = kwargs.get("version_code", '') or ''
        self.gameVersionId = kwargs.get("version_id", 0) or 0
