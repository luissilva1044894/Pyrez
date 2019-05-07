
#from .HandOfTheGods import HandOfTheGods
#from .PaladinsStrike import PaladinsStrike

from .API import API
from .APIBase import APIBase
from .BaseSmitePaladins import BaseSmitePaladins
from .HiRez import HiRez
from .Paladins import Paladins
from .RealmRoyale import RealmRoyale
from .Smite import Smite
from .StatusPage import StatusPage
#Cyclic import ^

__all__ = (
	"API",
	"APIBase",
	"BaseSmitePaladins",
	"HiRez",
	"Paladins",
	"RealmRoyale",
	"Smite",
	"StatusPage",
	#"HandOfTheGods",
	#"PaladinsStrike",
)
