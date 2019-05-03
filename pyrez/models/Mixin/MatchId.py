class MatchId:
    def __init__(self, **kwargs):
        self.matchId = kwargs.get("Match", kwargs.get("match", kwargs.get("match_id", 0))) if kwargs else 0
