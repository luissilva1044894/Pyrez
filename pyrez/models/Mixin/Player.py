class Player:
    def __init__(self, **kwargs):
        self.playerId = kwargs.get("player_id", kwargs.get("Id", kwargs.get("id", kwargs.get("playerId", 0)))) if kwargs else 0
        self.playerName = kwargs.get("player_name", kwargs.get("Name", kwargs.get("name", kwargs.get("playerName", None)))) if kwargs else None
    def __repr__(self):
        return "<Player {} ({})>".format(self.playerName, self.playerId)
    #def __hash__(self):
        #return hash(self.playerId)
    def __eq__(self, other):
        return self.playerId == other.playerId
