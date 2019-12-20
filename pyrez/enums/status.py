
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class Status(Enum):
  """Represents player status as follows:
    - 0: Offline,
    - 1: In Lobby,
    - 2: God Selection,
    - 3: In Game,
    - 4: Online,
    - 5: Player not found
  """
  UNKNOWN = 5
  OFFLINE = 0
  IN_LOBBY = 1
  CHARACTER_SELECTION = 2
  CHARACTER_SELECTION = 'god_selection'
  IN_MATCH = 3
  IN_MATCH = 'in_game'
  ONLINE = 4

  @property
  def online(self):
    return self not in [ Status.OFFLINE, Status.UNKNOWN ]

  @property
  def in_game(self):
    return self == Status.IN_MATCH

__all__ = (
  'Status',
)
