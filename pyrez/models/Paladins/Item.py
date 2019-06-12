from pyrez.enumerations import Champions
from pyrez.models import Item as ItemBase
class Item(ItemBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.itemDescription = kwargs.get("Description", None) if kwargs else None
        try:
            self.godId = Champions(kwargs.get("champion_id"))
        except ValueError:
            self.godId = kwargs.get("champion_id", 0) if kwargs else 0
        self.itemType = kwargs.get("item_type", None) if kwargs else None
        self.rechargeSeconds = kwargs.get("recharge_seconds", 0) if kwargs else 0
        self.talentRewardLevel = kwargs.get("talent_reward_level", 0) if kwargs else 0
