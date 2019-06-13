from pyrez.models import APIResponseBase
class LeaderboardDetails(APIResponseBase):
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.matches = kwargs.get("matches") or None
    	self.playerId = kwargs.get("player_id", 0) or 0
    	self.playerName = kwargs.get("player_name") or None
    	self.rank = kwargs.get("rank") or None
    	self.teamAVGPlacement = kwargs.get("team_avg_placement") or None
    	self.teamWins = kwargs.get("team_wins") or None
    	self.winPercentage = kwargs.get("win_percentage") or None
