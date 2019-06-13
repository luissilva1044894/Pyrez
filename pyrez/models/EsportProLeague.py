from .APIResponse import APIResponse
class EsportProLeague(APIResponse):
    """An important return value is “matchStatus” which represents a match being:
        - scheduled (1),
        - in-progress (2),
        - complete (3)
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.awayTeamClanId = kwargs.get("away_team_clan_id", 0) or 0
        self.awayTeamName = kwargs.get("away_team_name", '') or ''
        self.awayTeamTagName = kwargs.get("away_team_tagname", '') or ''
        self.homeTeamClanId = kwargs.get("home_team_clan_id", 0) or 0
        self.homeTeamName = kwargs.get("home_team_name", '') or ''
        self.homeTeamTagName = kwargs.get("home_team_tagname", '') or ''
        self.mapInstanceId = kwargs.get("map_instance_id", 0) or 0
        self.matchDate = kwargs.get("match_date", '') or '' #Datetime
        self.matchNumber = kwargs.get("match_number", 0) or 0
        self.matchStatus = kwargs.get("match_status", '') or ''
        self.matchupId = kwargs.get("matchup_id", 0) or 0
        self.region = kwargs.get("region", '') or ''
        self.tournamentName = kwargs.get("tournament_name", '') or ''
        self.winningTeamClanId = kwargs.get("winning_team_clan_id", 0) or 0
