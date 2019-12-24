
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ..api_response import APIResponse
from ...utils import decorators
class _Base(APIResponse):
  def __init__(self, **kw):
    #APIResponse.__init__(self, api=kw.pop('api', None), **kw)
    super().__init__(**kw)
    if kw.get('status') and str(kw.get('status', '')).lower() in ['blocked', 'friend']:
      self.blocked = kw.get('status') == 'blocked'
    if kw.get('friend_flags'):
      from ...utils.num import num_or_string
      from ...enums.friend_flag import FriendFlag
      self.friend_flag = FriendFlag(num_or_string(kw.get('friend_flags'))) or kw.get('friend_flags')

  def __eq__(self, other):
    if self.public:
      if hasattr(other, 'player_id'):
        return int(self) == other.player_id
      if hasattr(other, 'id'):
        return int(self) == other.id
    return int(self) == other
  
  def __hash__(self):
    return hash(self.player_id)
  
  def __int__(self):
    return self.player_id or 0

  def __repr__(self):
    return f'<{self.__class__.__name__ if str(self.__class__.__name__).lower() not in ["_base", "base"] else "Player"} {self.player_name} ({self.player_id})>'

  @property
  def account_id(self):
    from ...utils.num import num_or_string
    return num_or_string(self.json.get('account_id')) or 0

  '''
  @property
  def id(self):
    return self.player_id

  @property
  def name(self):
    return self.player_name
  '''
  
  @property
  def player(self):
    return self

  @property
  def player_id(self):
    from ...utils.num import num_or_string
    return num_or_string(self.json.get('player_id') or self.json.get('Id') or self.json.get('id') or self.json.get('playerId')) or 0

  @property
  def player_name(self):
    player_name = self.json.get('player_name') or self.json.get('playerName') or self.json.get('hz_player_name') or self.json.get('hz_gamer_tag') or self.json.get('Name') or self.json.get('name') or None
    if player_name:
      return str(player_name)

  @property
  def portal(self):
    from ...enums.portal import Portal
    return Portal(self.portal_id)

  @property
  def portal_id(self):
    from ...utils.num import num_or_string
    return num_or_string(self.json.get('portal_id') or self.json.get('playerPortalId') or self.json.get('platform')) or 0

  @property
  def portal_user_id(self):
    from ...utils.num import num_or_string
    return num_or_string(self.json.get('playerPortalUserId')) or 0

  @property
  def public(self):
    """hidden_profile"""
    return self.player_id != 0

  @decorators.is_public
  def expand(self, **kw): #info | profile
    if isinstance(self, (_Base, Base)):#isinstance(self, Player) and self.__class__.__name__ == Player.__name__:
      return self.__api__.player(self.player_id, api=self.__api__, **kw)
    return self

  @decorators.is_public
  def achievements(self, **kw):
    return self.__api__.player_achievements(self.player_id, api=self.__api__, **kw)

  @decorators.is_public
  def friends(self, **kw):
    return self.__api__.friends(self.player_id, api=self.__api__, **kw)

  @decorators.is_public
  def match_history(self, **kw):
    return self.__api__.match_history(self.player_id, api=self.__api__, **kw)

  @decorators.is_public
  def queue_stats(self, queue_id, **kw):
    return self.__api__.queue_stats(self.player_id, queue_id, api=self.__api__, **kw)

  @decorators.is_public
  def status(self, **kw):
    return self.__api__.player_status(self.player_id, api=self.__api__, **kw)

class Base(_Base):
  def __init__(self, **kw):
    super().__init__(**kw)

  @property
  def created_at(self):
    from ...utils.time import iso_or_string
    return iso_or_string(self.json.get('Created_Datetime') or self.json.get('created_datetime')) or  None

  @property
  def last_login(self):
    from ...utils.time import iso_or_string
    return iso_or_string(self.json.get('Last_Login_Datetime') or self.json.get('last_login_datetime')) or None

  @property
  def level(self):
    """account_level"""
    from ...utils.num import num_or_string
    return num_or_string(self.json.get('Level') or self.json.get('Account_Level') or self.json.get('level')) or 0

  @property
  def region(self):
    from ...enums.region import Region
    return Region(self.json.get('Region') or self.json.get('region'))

class Player(Base):

  @property
  def avatar(self):
    from ...enums.avatar_id import AvatarId
    return AvatarId(self.avatar_id)

  @property
  def avatar_id(self):
    from ...utils.num import num_or_string
    return num_or_string(self.json.get('avatarId') or self.json.get('AvatarId')) or 0

  @property
  def avatar_url(self):
    return self.json.get('avatarURL') or self.json.get('Avatar_URL') or None

  @property
  def steam_id(self):
    from ...utils.num import num_or_string
    return num_or_string(self.json.get('steam_id')) or 0

__all__ = (
  'Player',
  'Base',
)
