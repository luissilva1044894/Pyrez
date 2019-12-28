
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ...models import player
from ...utils import decorators
class Player(player.Player):
  def __init__(self, *, api=None, **kw):
    super().__init__(api=api, **kw)

  @decorators.is_public
  def loadouts(self, **kw):
    return self.__api__.player_loadouts(self.id, api=self.__api__, **kw)

  @decorators.is_public
  def gods(self, **kw):
    return self.__api__.player_gods(self.id, api=self.__api__, **kw)

  @decorators.is_public
  def gods_ranks(self, god_id, **kw):
    from ...enums.champions import Champion
    return self.__api__.god_ranks(self.id, Champion(god_id), api=self.__api__, **kw)
  
__all__ = (
  'Player',
)
