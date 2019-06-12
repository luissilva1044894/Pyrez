from .APIResponse import APIResponse
from pyrez.models.Mixin import MatchId
class MatchBase(APIResponse, MatchId):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)
        MatchId.__init__(self, **kwargs)
        self.skin = kwargs.get("Skin", None) if kwargs else None
        self.skinId = kwargs.get("SkinId", 0) if kwargs else 0
        self.taskForce = kwargs.get("taskForce", kwargs.get("TaskForce", 0)) if kwargs else 0
