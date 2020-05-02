
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ....enums.champion import Champion
from ....enums.ownership_type import OwnershipType
from ...models.api_response import APIResponse
from ....utils.num import num_or_string

class Base(APIResponse):
  def __init__(self, **kw):
    super().__init__(**kw)

  @property
  def god(self):
    return Champion(self.god_id)

  @property
  def god_id(self):
    return num_or_string(self.json.get('ChampionId') or self.json.get('champion_id')) or 0

  @property
  def god_name(self):
    if self.god:
      return str(self.god)
    return self.json.get('Champion') or self.json.get('ChampionName') or self.json.get('champion_name') or None

class Champion(Base):
  def __int__(self):
    return int(self.god)

  @property
  def ownership_type(self):
    return OwnershipType(self.get('OwnershipType')) or self.get('OwnershipType') or 0

  @property
  def player_id(self):
    return num_or_string(self.get('PlayerId')) or 0

  @property
  def xp(self):
    return num_or_string(self.get('XP')) or 0
