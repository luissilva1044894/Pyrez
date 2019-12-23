
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ....models.api_response import APIResponse
class Champion(APIResponse):
  def __init__(self, **kw):
    super().__init__(**kw)

  @property
  def champion(self):
    from ....enums.champion import Champion
    return Champion(self.get('ChampionId')) or self.get('ChampionId') or 0

  @property
  def champion_id(self):
    return int(self.champion)

  @property
  def champion_name(self):
    if self.champion != 0:
      return str(self.champion)
    return self.get('Champion')

  @property
  def ownership_type(self):
    from ....enums.ownership_type import OwnershipType
    return OwnershipType(self.get('OwnershipType')) or self.get('OwnershipType') or 0

  @property
  def player_id(self):
    from ....utils.num import num_or_string
    return num_or_string(self.get('PlayerId')) or 0

  @property
  def xp(self):
    from ....utils.num import num_or_string
    return num_or_string(self.get('XP')) or 0
