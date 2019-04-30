from .AbstractPlayer import AbstractPlayer
class Player(AbstractPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.steamId = kwargs.get("steam_id", 0) if kwargs else 0
