from .RequestError import RequestError
class ServiceUnavailable(RequestError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
