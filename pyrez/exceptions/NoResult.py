from .PyrezException import PyrezException
class NoResult(PyrezException):
    def __init__(self, *args, **kwargs):
        PyrezException.__init__(self, *args, **kwargs)
