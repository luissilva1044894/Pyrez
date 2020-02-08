from pyrez.models import PlayerPS, Ranked
class Player(PlayerPS):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.avatarURL = kwargs.get("Avatar_URL", '') or ''

        self.rankedConquestController = kwargs.get("RankedConquestController", None)
        if self.rankedConquestController and isinstance(self.rankedConquestController, dict):
            self.rankedConquestController = Ranked(**self.rankedConquestController)

        self.rankedDuel = kwargs.get("RankedDuel", None)
        if self.rankedDuel and isinstance(self.rankedDuel, dict):
            self.rankedDuel = Ranked(**self.rankedDuel)

        self.rankedDuelController = kwargs.get("RankedDuelController", None)
        if self.rankedDuelController and isinstance(self.rankedDuelController, dict):
            self.rankedDuelController = Ranked(**self.rankedDuelController)

        self.rankedJoust = kwargs.get("RankedJoust", None)
        if self.rankedJoust and isinstance(self.rankedJoust, dict):
            self.rankedJoust = Ranked(**self.rankedJoust)
        
        self.rankedJoustController = kwargs.get("RankedJoustController", None)
        if self.rankedJoustController and isinstance(self.rankedJoustController, dict):
            self.rankedJoustController = Ranked(**self.rankedJoustController)
        
        self.tierJoust = kwargs.get("Tier_Joust", '') or ''
        self.tierDuel = kwargs.get("Tier_Duel", '') or ''
