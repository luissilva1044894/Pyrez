
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .mixins.dict import Dict
class Base(Dict):
	"""Superclass for all Pyrez models.
	Keyword Arguments
	-----------------
	json:
		The request as JSON, if you prefer.
	"""
	def __init__(self, **kw):
		super().__init__(**kw)

	@property
	def json(self):
		return self.__kwargs__ or {}

class APIResponse(Base):
	"""Represents a generic Pyrez object. This is a sub-class of :class:`APIResponseBase`.
	Keyword Arguments
	-----------------
	error_msg:
	  The message returned from the API request.
	"""
	def __init__(self, **kw):
		super().__init__(**kw)
		self.error_msg = kw.get('ret_msg', kw.get('error', kw.get('errors', None))) or None
	@property
	def has_error(self):
		return self.error_msg is not None
