from .PyrezException import PyrezException
class SessionLimitExceeded(PyrezException):
	"""Raised when the maximum number of active sessions is reached."""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
