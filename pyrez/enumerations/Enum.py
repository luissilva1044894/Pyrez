import enum

__all__ = (
    'Enum',
)

class Enum(enum.Enum):
    """Represents a generic enum object. This is a sub-class of :class:`enum.Enum`.

    Supported Operations:

    +-----------+---------------------------------------------+
    | Operation |                 Description                 |
    +===========+=============================================+
    | x == y    | Checks if two Enum are equal.               |
    +-----------+---------------------------------------------+
    | x != y    | Checks if two Enum are not equal.           |
    +-----------+---------------------------------------------+
    | hash(x)   | Return the Enum's hash.                     |
    +-----------+---------------------------------------------+
    | str(x)    | Returns the Enum's name with discriminator. |
    +-----------+---------------------------------------------+
    | int(x)    | Return the Enum's value as int.             |
    +-----------+---------------------------------------------+
    """
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
        if os.environ.get('READTHEDOCS', None) == 'True':
            return '{}.{}'.format(self.__class__.__name__, str(self.name))
        return '{}({})'.format(str(self.name), self.getId())
    def getName(self):
        return str(self.name.replace('_', ' '))
    def getId(self):
        return int(self) if str(self.value).isnumeric() else str(self.value)
'''
#http://xion.io/post/code/python-enums-are-ok.html
@property
def foo(self):
    return self._foo
from enum import Enum
from collections import namedtuple

Color = namedtuple('Color', ['value', 'displayString'])

class Colors(Enum):

    @property
    def displayString(self):
        return self.value.displayString

    yellow = Color(1, 'Yellow')
    green = Color(2, 'Green')

print(Colors.yellow.displayString)


import enum
class ColorEnumMeta(enum.EnumMeta):
    def __new__(mcs, name, bases, attrs):
        obj = super().__new__(mcs, name, bases, attrs)
        obj._value2member_map_ = {}
        for m in obj:
            value, display_string = m.value
            m._value_ = value
            m.display_string = display_string
            obj._value2member_map_[value] = m

        return obj
class Color(enum.Enum, metaclass=ColorEnumMeta):
    yellow = 1, 'Yellow'
    green = 2, 'Green'
print(Color.yellow.display_string)  # 'Yellow'


#https://www.notinventedhere.org/articles/python/how-to-use-strings-as-name-aliases-in-python-enums.html
from enum import Enum

class Station(Enum):
    wien_westbahnhof = 1
    st_poelten = 2
    linz = 3
    wels = 4

    @classmethod
    def from_name(cls, name):
        for station, station_name in STATIONS.items():
            if station_name == name:
                return station
        raise ValueError('{} is not a valid station name'.format(name))

    def to_name(self):
        return STATIONS[self.value]

#https://docs.python.org/3/library/enum.html#planet
'''
