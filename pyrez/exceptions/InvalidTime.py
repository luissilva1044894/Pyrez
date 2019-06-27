from .PyrezException import PyrezException
class InvalidTime(PyrezException):
	"""Invalid timestamp"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
