from .APIResponse import APIResponse
class MergedPlayer(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mergeDatetime = kwargs.get("merge_datetime", None) if kwargs else None
        self.playerId = kwargs.get("playerId", 0) if kwargs else 0
        self.portalId = kwargs.get("portalId", 0) if kwargs else 0
