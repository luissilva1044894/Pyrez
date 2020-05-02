
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from boolify import boolify

from ..api_response import APIResponse
from ...utils.num import num_or_string

class _Base(APIResponse):
  @property
  def match_id(self):
    return num_or_string(self.json.get('Match') or self.json.get('match') or self.json.get('match_id')) or 0

  def __int__(self):
    return self.match_id or 0

  def __repr__(self):
    return f'<MatchId {int(self)}>'

  def match_details(self, **kw):
    if self.match_id and hasattr(self, '__api__'):
      return self.__api__.match(self.match_id, **kw)

class Base(_Base):
  def match_players(self, **kw):
    if self.match_id and hasattr(self, '__api__'):
      return self.__api__.players_from_match(self.match_id, **kw)

class Id(Base):
  @property
  def active_flag(self):
    '''“activeFlag” means that there is no match information/stats for the corresponding match.
    Usually due to a match being in-progress, though there could be other reasons.'''
    return boolify(self.get('Active_Flag') or self.get('active_flag'))
