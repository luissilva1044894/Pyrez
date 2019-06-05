class Singleton(object):
	#def __new__(type):
	#	if not "instance" in type.__dict__:
	#		type.instance = object.__new__(type)
	#	return type.instance
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, "instance"):
			cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
		return cls.instance
