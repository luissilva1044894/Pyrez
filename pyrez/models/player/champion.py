
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ..api_response import APIResponse
#from ...utils import decorators
class Status(APIResponse):
  def __init__(self, *, api=None, **kw):
    super().__init__(**kw)
    self.champion = kw.get('Champion') or None
    self.champion_id = kw.get('ChampionId') or 0
    self.ownership_type = kw.get('OwnershipType') or None # Free | Purchased | From Champions Pack | Trial
    self.player_id = kw.get('PlayerId') or 0
    self.xp = kw.get('XP') or 0
    self.__api__ = api
