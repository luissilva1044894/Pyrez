
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ..api_response import APIResponse
class Player(APIResponse):
	def __init__(self, **kw):
		super().__init__(**kw)
		self.level = kw.get('AccountLevel') or 0
		self.joined_at = kw.get('JoinedDatetime') or None
		self.last_login = kw.get('LastLoginDatetime') or None
		self.name = kw.get('Name') or None
