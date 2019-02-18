from enum import Enum, IntFlag

class BaseEnum(Enum):
    def __str__(self):
        return str(self.value) # return str(self.name)

