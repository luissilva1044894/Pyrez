from .PyrezException import PyrezException
class UnauthorizedError(PyrezException):
	"""Raises an error that the current Credentials is invalid or missing"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
