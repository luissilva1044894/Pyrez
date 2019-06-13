from .APIResponse import APIResponse
from pyrez.models.Mixin import MatchId as MixinMatchId
class MatchId(APIResponse, MixinMatchId):
	"""
	“activeFlag” means that there is no match information/stats for the corresponding match.
	Usually due to a match being in-progress, though there could be other reasons.
	"""
	def __init__(self, **kwargs):
		APIResponse.__init__(self, **kwargs)
		MixinMatchId.__init__(self, **kwargs)
		self.activeFlag = str(kwargs.get("Active_Flag", kwargs.get("active_flag", ''))).lower() == 'y' or False
