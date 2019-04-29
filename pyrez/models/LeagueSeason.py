from .APIResponse import APIResponse
class LeagueSeason(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.leagueCompleted = kwargs.get("complete", False) if kwargs is not None else False
        self.leagueId = kwargs.get("id", 0) if kwargs is not None else 0
        self.leagueDescription = kwargs.get("league_description", None) if kwargs is not None else None
        self.leagueName = kwargs.get("name", None) if kwargs is not None else None
        self.leagueSplit = kwargs.get("round", 0) if kwargs is not None else 0
        self.leagueSeason = kwargs.get("season", 0) if kwargs is not None else 0
