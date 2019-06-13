from pyrez.models import Item as ItemBase, ItemDescription
class Item(ItemBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.activeFlag = str(kwargs.get("ActiveFlag", '')).lower() == 'y' or False
        self.childItemId = kwargs.get("ChildItemId", 0) or 0
        self.itemDescription = ItemDescription(**kwargs.get("ItemDescription", None)) or None#Need to improve
        self.itemTier = kwargs.get("ItemTier", '') or ''
        self.rootItemId = kwargs.get("RootItemId", 0) or 0
        self.startingItem = kwargs.get("StartingItem", '') or ''
        self.type = kwargs.get("Type", '') or ''
