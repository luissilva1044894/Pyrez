
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class Region(Enum):
	AUSTRALIA = 'Australia'
	BRAZIL = 'Brazil'
	EUROPE = 'Europe'
	LATIN_AMERICA_NORTH = 'Latin America North'
	NORTH_AMERICA = 'North America'
	SOUTHEAST_ASIA = 'Southeast Asia'
	UNKNOWN = ''

__all__ = (
	'Region',
)
