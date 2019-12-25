
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Team
class Info(Team):

  @property
  def rating(self):
    from ...utils.num import num_or_string
    return num_or_string(self.json.get('Rating')) or 0
  
  @property
  def losses(self):
    from ...utils.num import num_or_string
    return num_or_string(self.json.get('Losses')) or 0
  
  @property
  def wins(self):
    from ...utils.num import num_or_string
    return num_or_string(self.json.get('Wins')) or 0

  @property
  def winratio(self):
    from ...utils.num import winratio
    return winratio(self.wins, self.wins + self.losses)
