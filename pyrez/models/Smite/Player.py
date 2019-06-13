from pyrez.models import PlayerPS, Ranked
class Player(PlayerPS):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.avatarURL = kwargs.get("Avatar_URL", '') or ''
        self.rankedConquestController = Ranked(**kwargs.get("RankedConquestController", None)) or None
        self.rankedDuel = Ranked(**kwargs.get("RankedDuel", None)) or None
        self.rankedDuelController = Ranked(**kwargs.get("RankedDuelController", None)) or None
        self.rankedJoust = Ranked(**kwargs.get("RankedJoust", None)) or None
        self.rankedJoustController = Ranked(**kwargs.get("RankedJoustController", None)) or None
        self.tierJoust = kwargs.get("Tier_Joust", '') or ''
        self.tierDuel = kwargs.get("Tier_Duel", '') or ''
