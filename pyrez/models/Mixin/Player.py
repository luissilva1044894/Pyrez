class Player:
    def __init__(self, **kwargs):
        self.playerId = kwargs.get("player_id", kwargs.get("Id", kwargs.get("id", kwargs.get("playerId", 0)))) or 0
        self.playerName = kwargs.get("player_name", kwargs.get("Name", kwargs.get("name", kwargs.get("playerName", '')))) or ''
        self.portalId = kwargs.get("portal_id", 0) or 0
    def __repr__(self):
        return "<Player {0.playerName} ({0.playerId})>".format(self)
    def __eq__(self, other):
        if not self.hidden_profile and isinstance(other, self.__class__):
            return self.playerId == other.playerId
        return False
    @property
    def hidden_profile(self):
        return self.playerId == 0
