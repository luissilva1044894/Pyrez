import enum

__all__ = (
    "Enum",
)

class Enum(enum.Enum):
    #Unknown = -1#None
    def __str__(self):#str(Enum)
        return str(self.getId())
    def __hash__(self):#[Enum]
        return hash(self.getId())
    def equal(self, other):#Enum==3
        return self.__eq__(other)
    def __eq__(self, other):#Enum==3
        if isinstance(other, type(self)):
            return self.getId() == other.getId()
        try:
            return other == type(other)(self.getId())
        except ValueError:
            return False
    def __int__(self):
        return int(self.value) if str(self.value).isnumeric() else -1
    def __repr__(self):#self.__class__ > <type 'Enum'>
        import os
        if os.environ.get("READTHEDOCS", None) == "True":
            return "{}.{}".format(self.__class__.__name__, str(self.name))
        return "<{} '{}/{}'>".format(self.__class__.__name__, str(self.name), self.getId())
    def getName(self):
        return str(self.name.replace('_', ' '))
    def getId(self):
        return int(self) if str(self.value).isnumeric() else str(self.value)
