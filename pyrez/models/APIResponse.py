from .APIResponseBase import APIResponseBase
class APIResponse(APIResponseBase):
	"""Represents a generic Pyrez object. This is a sub-class of :class:`APIResponseBase`.

	Keyword Arguments
	-----------------
    errorMsg : |STR|
    	The message returned from the API request.
	"""
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.errorMsg = kwargs.get("ret_msg", kwargs.get("error", kwargs.get("errors", None))) or None
	@property
	def hasError(self):
		return self.errorMsg is not None
