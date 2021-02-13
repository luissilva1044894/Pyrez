
from pyrez.enumerations import Champions
from pyrez.models import APIResponse
class BountyItem(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Champions(kwargs.get('champion_id'))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get('champion_id') or 0
            self.godName = kwargs.get('champion_name') or ''
        self.active = str(kwargs.get('active', '')).lower() == 'y'
        self.bountyItemId1 = kwargs.get('bounty_item_id1') or 0
        self.bountyItemId2 = kwargs.get('bounty_item_id2') or 0
        self.bountyItemName = kwargs.get('bounty_item_name') or ''
        self.finalPrice = kwargs.get('final_price') or 0
        self.initialPrice = kwargs.get('initial_price') or 0
        self.saleEndDatetime = kwargs.get('sale_end_datetime')
        self.saleType = kwargs.get('sale_type')
