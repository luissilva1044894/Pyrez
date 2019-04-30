from .APIResponse import APIResponse
class LeagueLeaderboard(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.leaves = kwargs.get("Leaves", 0) if kwargs else 0
        self.losses = kwargs.get("Losses", 0) if kwargs else 0
        self.playerName = kwargs.get("Name", None) if kwargs else None
        self.points = kwargs.get("Points", 0) if kwargs else 0
        self.prevRank = kwargs.get("PrevRank", 0) if kwargs else 0
        self.rank = kwargs.get("Rank", 0) if kwargs else 0
        self.rankStatConquest = kwargs.get("Rank_Stat_Conquest", 0) if kwargs else 0
        self.rankStatDuel = kwargs.get("Rank_Stat_Duel", 0) if kwargs else 0
        self.rankStatJoust = kwargs.get("Rank_Stat_Joust", 0) if kwargs else 0
        self.leagueSeason = kwargs.get("Season", 0) if kwargs else 0
        self.tier = kwargs.get("Tier", 0) if kwargs else 0
        self.trend = kwargs.get("Trend", 0) if kwargs else 0
        self.wins = kwargs.get("Wins", 0) if kwargs else 0
        self.playerId = kwargs.get("player_id", 0) if kwargs else 0
