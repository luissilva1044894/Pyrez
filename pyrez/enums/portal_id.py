
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class PortalId(Enum):
	Unknown = -1
	Unknown = ''
	Unknown = None
	HiRez = 1
	Steam = 5
	PS4 = 9
	Xbox = 10
	Mixer = 14
	Switch = 22
	Discord = 25

__all__ = (
	'PortalId',
)
