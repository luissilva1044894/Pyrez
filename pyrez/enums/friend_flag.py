
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

from . import Enum
class FriendFlag(Enum):
  """FRIEND_FLAGS"""
  UNKNOWN = 0
  FRIEND = 1 << 0
  FRIENDSHIP_REQUESTED = 1 << 1
  """We rejected the incoming friend request, but has yet to be acknowledged. Seems to be Refereed Friends also."""
  FRIENDSHIP_DECLINED = 1 << 2
  BLOCKED = 1 << 5 #34 | 36 | 38
  """Means they are an acknowledge "friend" but you block them... you could unblock them and they'd be a friend again"""
  FRIENDSHIP_BLOCKED = 33

  @property
  def is_blocked(self):
    return self in [FriendFlag.BLOCKED, FriendFlag.FRIEND_BLOCKED]

  @property
  def is_friend(self):
    return self == FriendFlag.FRIEND

__all__ = (
  'FriendFlag',
)
