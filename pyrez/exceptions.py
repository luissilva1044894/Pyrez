class PyrezException(Exception):
    """
    Base class for all other Pyrez exceptions.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
    def __str__(self):
        return str(self.args[1]) if self.args else "An error has occured within Pyrez"
class DailyLimit(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class Deprecated(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class IdOrAuthEmpty(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class InvalidArgument(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class LiveMatchException(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class NoResultError(PyrezException):
    def __init__(self, *args, **kwargs):
        PyrezException.__init__(self, *args, **kwargs)
class NotFound(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class NotSupported(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class PaladinsOnly(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class PlayerNotFound(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class RealmRoyaleOnly(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class RequestError(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class SessionLimit(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class SmiteOnly(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class UnexpectedException(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class WrongCredentials(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
