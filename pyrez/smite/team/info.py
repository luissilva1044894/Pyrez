
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Team
from ...utils.num import (
  num_or_string,
  winratio,
)

class Info(Team):

  @property
  def rating(self):
    return num_or_string(self.json.get('Rating')) or 0
  
  @property
  def losses(self):
    return num_or_string(self.json.get('Losses')) or 0
  
  @property
  def wins(self):
    return num_or_string(self.json.get('Wins')) or 0

  @property
  def winratio(self):
    return winratio(self.wins, self.wins + self.losses)
