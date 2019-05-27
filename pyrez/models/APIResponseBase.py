from pyrez.models.Mixin import Dict
class APIResponseBase(Dict):
	"""Represents a generic Pyrez object.

	Keyword Arguments
	-----------------
    json : |DICT| or |LIST|
    	The request as JSON, if you prefer.
	"""
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.json = kwargs or []
