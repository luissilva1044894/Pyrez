class PyrezException(Exception):
	"""Generic error class, catch-all for most Pyrez issues.
	It's the base class for all other Pyrez exceptions.
	"""
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)
	def __str__(self):
		return str(self.args[1]) if self.args else "An error has occured within Pyrez"
