from pyrez.enumerations import Champions
from pyrez.models import APIResponse
from .LoadoutItem import LoadoutItem
class Loadout(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Champions(kwargs.get("ChampionId"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("ChampionId", 0) or 0
            self.godName = kwargs.get("ChampionName", '') or ''
        self.deckId = kwargs.get("DeckId", 0) or 0
        self.deckName = kwargs.get("DeckName", '') or ''
        self.playerId = kwargs.get("playerId", 0) or 0
        self.playerName = kwargs.get("playerName", '') or ''
        self.cards = [ LoadoutItem(**_) for _ in (kwargs.get("LoadoutItems", None) or []) ]
