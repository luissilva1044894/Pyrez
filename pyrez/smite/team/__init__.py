
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ...models.api_response import APIResponse
class Team(APIResponse):
  #def __init__(self, *, api=None, **kw):
  #  APIResponse.__init__(self, **kw)

  def __int__(self):
    return self.team_id

  def __len__(self):
    return self.players

  def __bool__(self):
    return self.team_id != 0

  def founder(self, **kw):
    if self and self.founder_id and hasattr(self, '__api__'):
      return self.__api__.player(self.founder_id, **kw)

  @property
  def founder_id(self):
    from ...utils.num import num_or_string
    return num_or_string(self.json.get('FounderId')) or 0

  @property
  def founder_name(self):
    return self.json.get('Founder')

  @property
  def name(self):
    return self.json.get('Name')

  @property
  def players(self):
    from ...utils.num import num_or_string
    return num_or_string(self.json.get('Players')) or 0

  @property
  def tag(self):
    return self.json.get('Tag')

  @property
  def team_id(self):
    """clan_id"""
    from ...utils.num import num_or_string
    return num_or_string(self.json.get('TeamId')) or 0

  def details(self, **kw):
    if self and hasattr(self, '__api__'):
      return self.__api__.team_details(self.team_id, **kw)

  def team_players(self, **kw):
    if self and hasattr(self, '__api__'):
      return self.__api__.team_players(self.team_id, **kw)

__all__ = (
  'Team',
  'info',
  'player',
)
