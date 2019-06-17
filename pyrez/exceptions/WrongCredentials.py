from .PyrezException import PyrezException
class WrongCredentials(PyrezException):
	"""Raised when an invalid or blocked Credentials is passed."""
	def __init__(self, *args, **kwargs):#you try to access a resource and it fails due to some issue with your authentication
		super().__init__(*args, **kwargs)
