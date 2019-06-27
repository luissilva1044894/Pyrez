from .PyrezException import PyrezException
from .RateLimitExceeded import RateLimitExceeded
from .Deprecated import Deprecated
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
from .SessionLimitExceeded import SessionLimitExceeded
from .SmiteOnly import SmiteOnly
from .UnexpectedException import UnexpectedException
from .UnauthorizedError import UnauthorizedError

__all__ = (
	'PyrezException',
	'Deprecated',
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
	'SessionLimitExceeded',
	'SmiteOnly',
	'UnexpectedException',
	'UnauthorizedError',
)
#https://docs.python.org/3/library/exceptions.html#DeprecationWarning
