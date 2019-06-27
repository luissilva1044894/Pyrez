from .PyrezException import PyrezException
class RateLimitExceeded(PyrezException):
	"""Request rejected due to the rate limit being exceeded."""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
