from .APIResponse import APIResponse
class EsportProLeague(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.awayTeamClanId = kwargs.get("away_team_clan_id", 0) if kwargs else 0
        self.awayTeamName = kwargs.get("away_team_name", None) if kwargs else None
        self.awayTeamTagName = kwargs.get("away_team_tagname", None) if kwargs else None
        self.homeTeamClanId = kwargs.get("home_team_clan_id", 0) if kwargs else 0
        self.homeTeamName = kwargs.get("home_team_name", None) if kwargs else None
        self.homeTeamTagName = kwargs.get("home_team_tagname", None) if kwargs else None
        self.mapInstanceId = kwargs.get("map_instance_id", 0) if kwargs else 0
        self.matchDate = kwargs.get("match_date", None) if kwargs else None # Datetime
        self.matchNumber = kwargs.get("match_number", 0) if kwargs else 0
        self.matchStatus = kwargs.get("match_status", None) if kwargs else None
        self.matchupId = kwargs.get("matchup_id", 0) if kwargs else 0
        self.region = kwargs.get("region", None) if kwargs else None
        self.tournamentName = kwargs.get("tournament_name", None) if kwargs else None
        self.winningTeamClanId = kwargs.get("winning_team_clan_id", 0) if kwargs else 0
