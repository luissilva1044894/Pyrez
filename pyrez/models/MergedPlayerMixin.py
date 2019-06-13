from .MergedPlayer import MergedPlayer
#https://stackoverflow.com/questions/11276037/resolving-metaclass-conflicts
#http://www.phyast.pitt.edu/~micheles/python/metatype.html
#https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/
#https://stackoverflow.com/questions/6557407/triple-inheritance-causes-metaclass-conflict-sometimes
class MergedPlayerMixin:
	def __init__(self, **kwargs):
		self.mergedPlayers = [ MergedPlayer(**_) for _ in (kwargs.get("MergedPlayers", None) or []) ]
