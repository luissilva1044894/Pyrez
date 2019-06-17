from .Enum import Enum
class Platform(Enum):
	"""This is to refer to the platform always the same way and to prevent the changes if the api updates."""
	MOBILE = 'MOBILE'
	NINTENDO_SWITCH = 'Nintendo'
	PC = 'HiRez'#pc
	PS4 = 'PSN'
	XBOX = 'XboxLive'#xbl
	STEAM = 'Steam'
	#UNKNOWN = 'unknown' #XBOX = 'xbox' #SWITCH = 'switch'
