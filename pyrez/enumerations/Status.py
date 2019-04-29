from .BaseEnum import BaseEnum
class Status(BaseEnum):
    Offline = 0
    In_Lobby = 1
    God_Selection = 2
    In_Game = 3
    Online = 4
    Not_Found = 5
    def isOnline(self):
        return self != Status.Offline and self != Status.Not_Found
    def isInGame(self):
        return self == Status.In_Game
