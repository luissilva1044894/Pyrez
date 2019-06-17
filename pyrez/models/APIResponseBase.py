from pyrez.models.Mixin import Dict
class APIResponseBase(Dict):
	"""Superclass for all Pyrez models.

	Keyword Arguments
	-----------------
	json : |DICT| or |LIST|
		The request as JSON, if you prefer.
	"""
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.json = kwargs or []
