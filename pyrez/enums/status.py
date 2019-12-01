
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
	Offline = 0
	Offline = None
	In_Lobby = 1
	God_Selection = 2
	In_Game = 3
	Online = 4
	Not_Found = 5

	@property
	def online(self):
		return self not in [ Status.Offline, Status.Not_Found ]
	@property
	def in_game(self):
		return self == Status.In_Game

__all__ = (
  'Status',
)
