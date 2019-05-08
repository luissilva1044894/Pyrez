
#from .HandOfTheGodsAPI import HandOfTheGodsAPI
#from .PaladinsStrikeAPI import PaladinsStrikeAPI

from .API import API
from .APIBase import APIBase
from .BaseSmitePaladins import BaseSmitePaladins
from .HiRezAPI import HiRezAPI
from .PaladinsAPI import PaladinsAPI
from .RealmRoyaleAPI import RealmRoyaleAPI
from .SmiteAPI import SmiteAPI
from .StatusPageAPI import StatusPageAPI
#Cyclic import ^

__all__ = (
	"API",
	"APIBase",
	"HiRezAPI",
	"PaladinsAPI",
	"RealmRoyaleAPI",
	"SmiteAPI",
	"StatusPageAPI",
	#"HandOfTheGodsAPI",
	#"PaladinsStrikeAPI",
)
