from .PyrezException import (
	PyrezException,
	InvalidTime,
)
from .DailyLimit import DailyLimit
from .Deprecated import Deprecated
from .IdOrAuthEmpty import IdOrAuthEmpty
from .InvalidArgument import InvalidArgument
from .MatchException import MatchException
from .NoResult import NoResult
from .NotFound import NotFound
from .NotSupported import NotSupported
from .PaladinsOnly import PaladinsOnly
from .PlayerNotFound import PlayerNotFound
from .PrivatePlayer import PrivatePlayer
from .RealmRoyaleOnly import RealmRoyaleOnly
from .RequestError import RequestError
from .ServiceUnavailable import ServiceUnavailable
from .SessionLimit import SessionLimit
from .SmiteOnly import SmiteOnly
from .UnexpectedException import UnexpectedException
from .WrongCredentials import WrongCredentials

__all__ = (
	"PyrezException",
	'InvalidTime',
	"DailyLimit",
	"Deprecated",
	"IdOrAuthEmpty",
	"InvalidArgument",
	"MatchException",
	"NoResult",
	"NotFound",
	"NotSupported",
	"PaladinsOnly",
	"PlayerNotFound",
	"PrivatePlayer",
	"RealmRoyaleOnly",
	"RequestError",
	"SessionLimit",
	"SmiteOnly",
	"UnexpectedException",
	"WrongCredentials",
)
#https://docs.python.org/3/library/exceptions.html#DeprecationWarning
