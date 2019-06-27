from .PyrezException import PyrezException
from .RateLimitExceeded import RateLimitExceeded
from .Deprecated import Deprecated
from .UnauthorizedError import UnauthorizedError
from .InvalidArgument import InvalidArgument
from .InvalidSessionId import InvalidSessionId
from .InvalidTime import InvalidTime
from .MatchException import MatchException
from .NoResult import NoResult
from .NotFound import NotFound
from .NotSupported import NotSupported
from .PaladinsOnly import PaladinsOnly
from .PlayerNotFound import PlayerNotFound
from .RealmRoyaleOnly import RealmRoyaleOnly
from .RequestError import RequestError
from .SessionLimit import SessionLimit
from .SmiteOnly import SmiteOnly
from .UnexpectedException import UnexpectedException
from .WrongCredentials import WrongCredentials

__all__ = (
	'PyrezException',
	'Deprecated',
	'UnauthorizedError',
	'InvalidArgument',
	'InvalidTime',
	'MatchException',
	'NoResult',
	'NotFound',
	'NotSupported',
	'PaladinsOnly',
	'PlayerNotFound',
	'RateLimitExceeded',
	'RealmRoyaleOnly',
	'RequestError',
	'SessionLimit',
	'SmiteOnly',
	'UnexpectedException',
	'WrongCredentials',
)
#https://docs.python.org/3/library/exceptions.html#DeprecationWarning
