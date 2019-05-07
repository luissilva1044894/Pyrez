from pyrez.models import PlayerPS, Ranked
class Player(PlayerPS):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.avatarURL = kwargs.get("Avatar_URL", None) if kwargs else None
        self.mmrConquest = kwargs.get("Rank_Stat_Conquest", None) if kwargs else None #self.rankStatConquest
        self.mmrDuel = kwargs.get("Rank_Stat_Duel", None) if kwargs else None #self.rankStatDuel
        self.mmrJoust = kwargs.get("Rank_Stat_Joust", None) if kwargs else None #self.rankStatJoust
        self.mmrConquestController = kwargs.get("Rank_Stat_Conquest_Controller", None) if kwargs else None #self.rankStatConquestController
        self.mmrDuelController = kwargs.get("Rank_Stat_Duel_Controller", None) if kwargs else None #self.rankStatDuelController
        self.mmrJoustController = kwargs.get("Rank_Stat_Joust_Controller", None) if kwargs else None #self.rankStatJoustController
        self.rankedDuel = Ranked(**kwargs.get("RankedDuel", None)) if kwargs else None
        self.rankedJoust = Ranked(**kwargs.get("RankedJoust", None)) if kwargs else None
        self.tierJoust = kwargs.get("Tier_Joust", None) if kwargs else None
        self.tierDuel = kwargs.get("Tier_Duel", None) if kwargs else None
