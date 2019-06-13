class MatchId:
	def __init__(self, **kwargs):
		self.matchId = kwargs.get("Match", kwargs.get("match", kwargs.get("match_id", 0))) or 0
	def __int__(self):
		return int(self.matchId) if str(self.matchId).isnumeric() else -1
	def __repr__(self):
		return "<MatchId {0.matchId}>".format(self)
