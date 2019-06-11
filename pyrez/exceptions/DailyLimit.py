from .PyrezException import PyrezException
class DailyLimit(PyrezException):
	"""Raised when you've hit a rate limit."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
