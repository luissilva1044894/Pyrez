from .APIResponse import APIResponse
from pyrez.models.Mixin import MatchId as MixinMatchId
class MatchId(APIResponse, MixinMatchId):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)
        MixinMatchId.__init__(self, **kwargs)
        self.activeFlag = str(kwargs.get("Active_Flag", kwargs.get("active_flag", None))).lower() == 'y' if kwargs else False
