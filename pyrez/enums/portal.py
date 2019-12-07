
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class PortalId(Enum):
	Unknown = 0
	Unknown = 'unknown'
	HiRez = 1
	HiRez = 'pc'
	HiRez = 'Hirez'
	Hirez = 'Hi-Rez'
	Steam = 5
	Steam = 'Steam'
	PS4 = 9
	PS4 = 'ps4'
	PS4 = 'PSN'
	Xbox = 10
	Xbox = 'XboxLive'
	Xbox = 'xbox'
	Mixer = 14
	Switch = 22
	Switch = 'switch'
	Switch = 'nintendo_switch'
	Discord = 25
	Discord = 'Discord'

__all__ = (
	'PortalId',
)
