from pyrez.models import APIResponseBase
class LeaderboardDetails(APIResponseBase):
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.matches = kwargs.get("matches") if kwargs else None
    	self.playerId = kwargs.get("player_id", 0) if kwargs else 0
    	self.playerName = kwargs.get("player_name") if kwargs else None
    	self.rank = kwargs.get("rank") if kwargs else None
    	self.teamAVGPlacement = kwargs.get("team_avg_placement") if kwargs else None
    	self.teamWins = kwargs.get("team_wins") if kwargs else None
    	self.winPercentage = kwargs.get("win_percentage") if kwargs else None
