from pyrez.models import PlayerPS, Ranked
class Player(PlayerPS):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.avatarURL = kwargs.get("Avatar_URL", None) if kwargs else None
        self.rankedConquestController = Ranked(**kwargs.get("RankedConquestController", None)) if kwargs else None
        self.rankedDuel = Ranked(**kwargs.get("RankedDuel", None)) if kwargs else None
        self.rankedDuelController = Ranked(**kwargs.get("RankedDuelController", None)) if kwargs else None
        self.rankedJoust = Ranked(**kwargs.get("RankedJoust", None)) if kwargs else None
        self.rankedJoustController = Ranked(**kwargs.get("RankedJoustController", None)) if kwargs else None
        self.tierJoust = kwargs.get("Tier_Joust", None) if kwargs else None
        self.tierDuel = kwargs.get("Tier_Duel", None) if kwargs else None
