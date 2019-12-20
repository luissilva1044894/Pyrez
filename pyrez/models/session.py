
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .api_response import APIResponse
class Session(APIResponse):
  def __init__(self, *args, **kw):
    self.session_id = kw.get('session_id') or None
    self.timestamp = kw.get('timestamp') or None
    api = kw.pop('api', None)
    if api:
      self.test_session = api.test_session
    super().__init__(**kw)
  def is_approved(self):
    return 'approved' in self.error_msg.lower()