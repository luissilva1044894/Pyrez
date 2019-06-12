class Winratio:
    def __init__(self, **kwargs):
        self.losses = kwargs.get("Losses", kwargs.get("losses", 0)) if kwargs else 0
        self.wins = kwargs.get("Wins", kwargs.get("wins", 0)) if kwargs else 0
    def getWinratio(self, decimals=2):
        winratio = self.wins /((self.wins + self.losses) if self.wins + self.losses > 1 else 1) * 100.0
        return int(winratio) if winratio % 2 == 0 else round(winratio, decimals)
