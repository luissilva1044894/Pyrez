from .Enum import Enum
class Status(Enum):
    """Represents player status as follows:
        - 0: Offline,
        - 1: In Lobby,
        - 2: God Selection,
        - 3: In Game,
        - 4: Online,
        - 5: Player not found
    """
    Offline = 0
    In_Lobby = 1
    God_Selection = 2
    In_Game = 3
    Online = 4
    Not_Found = 5
    @property
    def isOnline(self):
        return self != Status.Offline and self != Status.Not_Found # self in [ Status.Offline, Status.Not_Found ]
    @property
    def isInGame(self):
        return self == Status.In_Game
