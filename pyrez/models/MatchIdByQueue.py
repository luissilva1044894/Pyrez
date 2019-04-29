from .APIResponse import APIResponse
class MatchIdByQueue(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.matchId = kwargs.get("Match", 0) or kwargs.get("match", 0) if kwargs is not None else 0
        self.activeFlag = str(kwargs.get("Active_Flag", kwargs.get("active_flag", None))).lower() == 'y' if kwargs is not None else False
