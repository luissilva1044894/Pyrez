
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ..api_response import APIResponse
#from ...utils import decorators
class Status(APIResponse):
  def __init__(self, *, api=None, **kw):
    super().__init__(**kw)
    from ...enums import status
    self.match_id = kw.get('Match') or kw.get('match_id') or 0
    self.queue_id = kw.get('match_queue_id') or 0
    self.status = status.Status(kw.get('status_id') or kw.get('status') or 5)
    self.status_message = kw.get('personal_status_message') or None
    self.status_string = kw.get('status_string') or kw.get('status') or None
    self.__api__ = api
  @property
  def in_match(self):
    return self.match_id > 0
  #@decorators.has_match_id
  def get_match_details(self):
    if self.in_match:
      return self.__api__.match(self.match_id, is_live=True)
  def get_players_from_match(self):
    if self.in_match:
      return self.__api__.players_from_match(self.match_id)
