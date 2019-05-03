from .PyrezException import PyrezException
class RealmRoyaleOnly(PyrezException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
