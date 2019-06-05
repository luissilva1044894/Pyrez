class Borg(object):
	"""Subclassing is no problem."""
	_shared_state = {}
	#def __init__(self):
	#	self.__dict__ = self.__shared_state
	def __new__(cls, *args, **kwargs):
		obj = super(Borg, cls).__new__(cls, *args, **kwargs)
		obj.__dict__ = cls._shared_state
		return obj
