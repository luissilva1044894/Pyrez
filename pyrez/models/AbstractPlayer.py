from .APIResponse import APIResponse
class AbstractPlayer(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerId = kwargs.get("player_id", kwargs.get("Id", kwargs.get("id", 0))) if kwargs else 0
        self.playerName = kwargs.get("Name", kwargs.get("name", None)) if kwargs else None
    def __repr__(self):
        return "<Player {}>".format(self.playerName)
    def __eq__(self, other):
        return self.playerId == other.playerId

