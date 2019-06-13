from pyrez.models import APIResponse
class Talent(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.categoryName = kwargs.get("category_name", '') or ''
        self.itemId = kwargs.get("item_id", 0) or 0
        self.lootTableItemId = kwargs.get("loot_table_item_id", 0) or 0
        self.talentDescription = kwargs.get("talent_description", '') or ''
        self.talentName = kwargs.get("talent_name", '') or ''
