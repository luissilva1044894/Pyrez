class KDA:
    def __init__(self, **kwargs):
        self.assists = kwargs.get("Assists", 0) if kwargs else 0
        self.deaths = kwargs.get("Deaths", 0) if kwargs else 0
        self.kills = kwargs.get("Kills", None) if kwargs else None
    def getKDA(self, decimals=2):
        kda = ((self.assists / 2) + self.kills) / (self.deaths if self.deaths > 1 else 1)
        return int(kda) if kda % 2 == 0 else round(kda, decimals)# + "%";
