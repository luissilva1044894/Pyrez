
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .mixins.dict import Dict
class APIResponse(Dict):
	"""Represents a generic Pyrez object. This is a super-class for all Pyrez models.
	Keyword Arguments
	-----------------
	error_msg:
	  The message returned from the API request.
	json:
		The request as JSON, if you prefer.
	"""
	def __init__(self, **kw):
		super().__init__(**kw)
		# self.content
		# self.headers
		# self.status
		self.error_msg = kw.get('ret_msg', kw.get('error', kw.get('errors', None))) or None
	@property
	def json(self):
		return self.to_json()
	@property
	def has_error(self):
		return self.error_msg is not None
