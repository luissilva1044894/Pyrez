from .Enum import Enum
class Platform(Enum):
	"""This is to refer to the platform always the same way and to prevent the changes if the api updates."""
	MOBILE = "MOBILE"
	NINTENDO_SWITCH = "Nintendo"
	PC = "HiRez"
	PS4 = "PSN"
	XBOX = "XboxLive"
	STEAM = "Steam"
	#UNKNOWN = "unknown" #XBOX = "xbox" #SWITCH = "switch"
