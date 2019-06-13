from .APIResponse import APIResponse
class LeagueSeason(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.leagueCompleted = kwargs.get("complete", False) or False
        self.leagueId = kwargs.get("id", 0) or 0
        self.leagueDescription = kwargs.get("league_description", '') or ''
        self.leagueName = kwargs.get("name", '') or ''
        self.leagueSplit = kwargs.get("round", 0) or 0
        self.leagueSeason = kwargs.get("season", 0) or 0
