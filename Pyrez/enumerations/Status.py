from enum import Enum

class Status(Enum):
    Offline = 0
    In_Lobby = 1
    God_Selection = 2
    In_Game = 3
    Online = 4
    Not_Found = 5
    def __str__(self):
        return str(self.name.replace("_", " "))
