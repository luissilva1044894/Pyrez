from .PyrezException import PyrezException
class LiveMatchException(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
