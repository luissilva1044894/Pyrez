from .PyrezException import PyrezException
class Deprecated(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
