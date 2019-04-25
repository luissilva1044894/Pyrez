class PyrezException(Exception):
    """
    Base class for all other Pyrez exceptions.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
    def __str__(self):
        return str(self.args[1]) if self.args else "An error has occured within Pyrez"
class DeprecatedException(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class DailyLimitException(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class InvalidArgumentException(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class IdOrAuthEmptyException(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class NotFoundException(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class NotSupported(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class SessionLimitException(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class WrongCredentials(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class PaladinsOnlyException(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class SmiteOnlyException(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class RealmRoyaleOnlyException(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class PlayerNotFound(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class LiveMatchDetailsException(PyrezException):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
class UnexpectedError(PyrezException):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
class RequestError(PyrezException):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
class NoResult(PyrezException):
    def __init__(self, *args, **kwargs):
        PyrezException.__init__(self, *args, **kwargs)
