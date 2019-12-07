
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class PortalId(Enum):
	Unknown = 0
	HiRez = 1
	Steam = 5
	PS4 = 9
	PS4 = "PSN"
	Xbox = 10
	Xbox = "XboxLive"
	Mixer = 14
	Switch = 22
	Discord = 25

__all__ = (
	'PortalId',
)
