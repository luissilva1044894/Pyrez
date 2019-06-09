class Winratio:
    def __init__(self, **kwargs):
        self.losses = kwargs.get('Losses', kwargs.get('losses', 0)) if kwargs else 0
        self.wins = kwargs.get('Wins', kwargs.get('wins', 0)) if kwargs else 0
    @property
    def winratio(self):
        _w = self.wins /((self.wins + self.losses) if self.wins + self.losses > 1 else 1) * 100.0
        return int(_w) if _w % 2 == 0 else round(_w, 2)
