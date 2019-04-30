from .BaseItem import BaseItem
from .ItemDescription import ItemDescription
class SmiteItem(BaseItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.activeFlag = str(kwargs.get("ActiveFlag", None)).lower() == 'y' if kwargs else False
        self.childItemId = kwargs.get("ChildItemId", 0) if kwargs else 0
        self.itemDescription = ItemDescription(**kwargs.get("ItemDescription", None))
        self.itemTier = kwargs.get("ItemTier", None) if kwargs else None
        self.rootItemId = kwargs.get("RootItemId", 0) if kwargs else 0
        self.startingItem = kwargs.get("StartingItem", None) if kwargs else None
        self.type = kwargs.get("Type", None) if kwargs else None
        self.itemDescription = ItemDescription(**kwargs.get("ItemDescription", None)) if kwargs else None #Need to improve
