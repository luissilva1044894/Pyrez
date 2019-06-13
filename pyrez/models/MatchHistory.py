from .BaseMatchDetail import BaseMatchDetail
from .InGameItem import InGameItem
from pyrez.enumerations import Champions, Gods
class MatchHistory(BaseMatchDetail):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.items = []
        self.loadout = []
        for i in range(1, 5):
            obj = InGameItem(kwargs.get("ActiveId{}".format(i)), kwargs.get("Active_{}".format(i)), kwargs.get("ActiveLevel{}".format(i)))
            self.items.append(obj)
        for i in range(1, 7):
            obj = InGameItem(kwargs.get("ItemId{}".format(i)), kwargs.get("Item_{}".format(i)), kwargs.get("ItemLevel{}".format(i)))
            self.loadout.append(obj)
        self.assists = kwargs.get("Assists")
        try:
            self.godId = Champions(kwargs.get("ChampionId")) if kwargs.get("ChampionId") else Gods(kwargs.get("GodId"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("ChampionId", kwargs.get("GodId", 0)) or 0
            self.godName = kwargs.get("Champion", kwargs.get("God", '')) or ''
        self.creeps = kwargs.get("Creeps", 0) or 0
        self.damage = kwargs.get("Damage", 0) or 0
        self.credits = kwargs.get("Gold", 0) or 0#creditsEarned
        self.kills = kwargs.get("Kills", 0) or 0
        self.level = kwargs.get("Level", 0) or 0
        self.queueId = kwargs.get("Match_Queue_Id", 0) or 0
        self.matchTime = kwargs.get("Match_Time", 0) or 0
        self.queue = kwargs.get("Queue", '') or ''
