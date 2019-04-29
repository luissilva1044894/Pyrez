from .BasePSPlayer import BasePSPlayer
from .Ranked import Ranked
class SmitePlayer(BasePSPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.avatarURL = kwargs.get("Avatar_URL", None) if kwargs is not None else None
        self.rankStatConquest = kwargs.get("Rank_Stat_Conquest", None) if kwargs is not None else None
        self.rankStatDuel = kwargs.get("Rank_Stat_Duel", None) if kwargs is not None else None
        self.rankStatJoust = kwargs.get("Rank_Stat_Joust", None) if kwargs is not None else None
        self.rankedDuel = Ranked(**kwargs.get("RankedDuel", None)) if kwargs is not None else None
        self.rankedJoust = Ranked(**kwargs.get("RankedJoust", None)) if kwargs is not None else None
        self.tierJoust = kwargs.get("Tier_Joust", None) if kwargs is not None else None
        self.tierDuel = kwargs.get("Tier_Duel", None) if kwargs is not None else None
