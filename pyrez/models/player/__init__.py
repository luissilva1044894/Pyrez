
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ..api_response import APIResponse
from ...utils import decorators
class _Base(APIResponse):
  def __init__(self, *, api=None, **kw):
    #APIResponse.__init__(self, **kw)
    super().__init__(**kw)
    from ...utils.num import num_or_string
    self.id = num_or_string(kw.get('player_id') or kw.get('Id') or kw.get('id') or kw.get('playerId') or 0)
    self.name = kw.get('player_name') or kw.get('Name') or kw.get('name') or kw.get('playerName') or None
    if self.name:
      self.name = str(self.name)
    from ...enums.portal import Portal
    self.portal = Portal(kw.get('portal_id') or 0)#platform
    # account_id = kw.get('account_id') or 0
    self.__api__ = api
  def __repr__(self):
    return f'<Player {self.name} ({self.id})>'
  def __eq__(self, other):
    if not self.private and isinstance(other, self.__class__):
      return self.id == other.id
    return False
  def __hash__(self):
    return hash(self.id)
  def __int__(self):
    return self.id or -1
  @property
  def public(self): #hidden_profile
    return self.id > 0
  @decorators.is_public
  def expand(self, **kw): #info | profile
    if isinstance(self, (_Base, Base)):#isinstance(self, Player) and self.__class__.__name__ == Player.__name__:
      return self.__api__.player(self.id, api=self.__api__, **kw)
    return self
  @decorators.is_public
  def achievements(self, **kw):
    return self.__api__.player_achievements(self.id, api=self.__api__, **kw)
  @decorators.is_public
  def friends(self, **kw):
    return self.__api__.friends(self.id, api=self.__api__, **kw)
  @decorators.is_public
  def match_history(self, **kw):
    return self.__api__.match_history(self.id, api=self.__api__, **kw)
  @decorators.is_public
  def queue_stats(self, queue_id, **kw):
    return self.__api__.queue_stats(self.id, queue_id, api=self.__api__, **kw)
  @decorators.is_public
  def status(self, **kw):
    return self.__api__.player_status(self.id, api=self.__api__, **kw)

class Base(_Base):
  def __init__(self, *, api=None, **kw):
    super().__init__(api=api, **kw)
    self.created = kw.get('Created_Datetime') or kw.get('created_datetime') or  None
    self.last_login = kw.get('Last_Login_Datetime') or kw.get('last_login_datetime') or None
    self.level = kw.get('Level') or kw.get('level') or 0 #account_level
    self.region = kw.get('Region') or kw.get('region') or None

class Player(Base):
  def __init__(self, *, api=None, **kw):
    super().__init__(api=api, **kw)
    self.steam_id = kw.get('steam_id') or 0

__all__ = (
  'Player',
  'Base',
)
