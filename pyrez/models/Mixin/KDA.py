class KDA:
    def __init__(self, **kwargs):
        self.assists = kwargs.get("Assists", 0) or 0
        self.deaths = kwargs.get("Deaths", 0) or 0
        self.kills = kwargs.get("Kills", 0) or 0
    @property
    def kda(self):
        _k = ((self.assists / 2) + self.kills) / (self.deaths if self.deaths > 1 else 1)
        return int(_k) if _k % 2 == 0 else round(_k, 2)# + "%";
