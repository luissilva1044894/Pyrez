class Winratio:
	def __init__(self, **kwargs):
        self.losses = kwargs.get('Losses', kwargs.get('losses', None)) or 0
        self.wins = kwargs.get('Wins', kwargs.get('wins', None)) or 0
    @property
    def winratio(self):
        _w = self.wins /((self.matches_played) if self.matches_played > 1 else 1) * 100.0
        return int(_w) if _w % 2 == 0 else round(_w, 2)
    @property
    def matches_played(self):
    	return self.wins + self.losses
