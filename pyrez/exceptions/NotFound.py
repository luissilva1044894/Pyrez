from .PyrezException import PyrezException
class NotFound(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
