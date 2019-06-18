from .PyrezException import PyrezException
class WrongCredentials(PyrezException):
	"""Raised when an invalid or blocked Credentials is passed."""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
