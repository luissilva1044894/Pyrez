from .PyrezException import PyrezException
class WrongCredentials(PyrezException):
	"""Raised when you try to access a resource and it fails due to some issue with your authentication."""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
