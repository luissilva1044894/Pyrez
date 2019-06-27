from .PyrezException import PyrezException
class UnauthorizedError(PyrezException):
	"""Raised when the current Credentials is invalid, blocked or missing"""
	def __init__(self, *args, **kwargs):#you try to access a resource and it fails due to some issue with your authentication
		super().__init__(*args, **kwargs)
