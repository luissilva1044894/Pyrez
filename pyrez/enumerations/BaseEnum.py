from enum import Enum

class BaseEnum(Enum):
    def __str__(self):#str(BaseEnum)
        return str(self.getId())
    def __hash__(self):#[BaseEnum]
        return hash(self.getId())
    def __eq__(self, other):#BaseEnum==3
        if isinstance(other, type(self)):
            return self.getId() == other.getId()
        try:
            return other == type(other)(self.getId())
        except ValueError:
            return False
    def getName(self):
        return str(self.name.replace('_', ' '))
    def getId(self):
        return int(self.value) if str(self.value).isnumeric() else str(self.value)
