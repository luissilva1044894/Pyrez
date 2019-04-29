from .APIResponse import APIResponse
class BaseMatch(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.matchId = kwargs.get("Match", 0) if kwargs is not None else 0
        self.skin = kwargs.get("Skin", None) if kwargs is not None else None
        self.skinId = kwargs.get("SkinId", 0) if kwargs is not None else 0
        self.taskForce = kwargs.get("taskForce", kwargs.get("TaskForce", 0)) if kwargs is not None else 0
