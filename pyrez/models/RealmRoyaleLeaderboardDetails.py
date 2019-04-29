class RealmRoyaleLeaderboardDetails:
    def __init__(self, **kwargs):
        self.matches = kwargs.get("matches") if kwargs is not None else None
        self.playerId = kwargs.get("player_id", 0) if kwargs is not None else 0
        self.playerName = kwargs.get("player_name") if kwargs is not None else None
        self.rank = kwargs.get("rank") if kwargs is not None else None
        self.teamAVGPlacement = kwargs.get("team_avg_placement") if kwargs is not None else None
        self.teamWins = kwargs.get("team_wins") if kwargs is not None else None
        self.winPercentage = kwargs.get("win_percentage") if kwargs is not None else None
