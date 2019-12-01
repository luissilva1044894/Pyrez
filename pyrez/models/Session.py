
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .api_response import APIResponse
class Session(APIResponse):
	def __init__(self, *, api=None, **kw):
		super().__init__(**kw)
		self.session_id = kw.get('session_id') or None
		self.timestamp = kw.get('timestamp') or None
		if api:
			self.test_session = api.test_session
	def is_approved(self):
		return self.error_msg.lower().find('approved') != -1
