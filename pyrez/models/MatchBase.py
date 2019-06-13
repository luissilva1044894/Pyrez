from .APIResponse import APIResponse
from pyrez.models.Mixin import MatchId
class MatchBase(APIResponse, MatchId):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)
        MatchId.__init__(self, **kwargs)
        self.skin = kwargs.get("Skin", '') or ''
        self.skinId = kwargs.get("SkinId", 0) or 0
        self.taskForce = kwargs.get("taskForce", kwargs.get("TaskForce", 0)) or 0
