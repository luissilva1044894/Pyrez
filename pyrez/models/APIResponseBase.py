from pyrez.models.Mixin import Dict
class APIResponseBase(Dict):
	"""
	The constructor for APIResponseBase class.
	Keyword arguments/Parameters:
		json [dict | list]: The request as JSON, if you prefer.
	"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.json = kwargs or []
