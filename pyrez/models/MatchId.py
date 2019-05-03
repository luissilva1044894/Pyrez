from .APIResponse import APIResponse
class MatchId(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.matchId = kwargs.get("Match", kwargs.get("match", 0)) if kwargs else 0
        self.activeFlag = str(kwargs.get("Active_Flag", kwargs.get("active_flag", None))).lower() == 'y' if kwargs else False
