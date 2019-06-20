from .PyrezException import PyrezException
class PlayerNotFound(PyrezException):#UnknownPlayer
	"""Raises an error when a player does not exist via the API"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)#The specified player was not found
