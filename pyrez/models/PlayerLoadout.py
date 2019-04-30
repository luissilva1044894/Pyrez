from pyrez.enumerations import Champions
from .APIResponse import APIResponse
from .LoadoutItem import LoadoutItem
class PlayerLoadout(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Champions(kwargs.get("ChampionId"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("ChampionId", 0) if kwargs else 0
            self.godName = kwargs.get("ChampionName", None) if kwargs else None
        self.deckId = kwargs.get("DeckId", 0) if kwargs else 0
        self.deckName = kwargs.get("DeckName", None) if kwargs else None
        self.playerId = kwargs.get("playerId", 0) if kwargs else 0
        self.playerName = kwargs.get("playerName", None) if kwargs else None
        cards = kwargs.get("LoadoutItems", None) if kwargs else None
        self.cards = []
        for i in cards if cards else []:
            obj = LoadoutItem(**i)
            self.cards.append(obj)
