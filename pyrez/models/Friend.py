from .APIResponse import APIResponse
class Friend(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accountId = kwargs.get("account_id", 0) if kwargs else 0
        self.avatarURL = kwargs.get("avatar_url", None) if kwargs else None
        self.playerId = kwargs.get("player_id", 0) if kwargs else 0
        self.playerName = kwargs.get("name", None) if kwargs else None
    def __str__(self):
        return "<Player {} ({})>".format(self.playerName, self.playerId)
    #def __hash__(self):
        #return hash(self.playerId)
    def __eq__(self, other):
        return self.playerId == other.playerId
