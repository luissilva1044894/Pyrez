from .BaseItem import BaseItem
from .ItemDescription import ItemDescription
class SmiteItem(BaseItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.activeFlag = str(kwargs.get("ActiveFlag", None)).lower() == 'y'
        self.childItemId = kwargs.get("ChildItemId", 0) if kwargs is not None else 0
        self.itemDescription = ItemDescription(**kwargs.get("ItemDescription", None))
        self.itemTier = kwargs.get("ItemTier", None) if kwargs is not None else None
        self.rootItemId = kwargs.get("RootItemId", 0) if kwargs is not None else 0
        self.startingItem = kwargs.get("StartingItem", None) if kwargs is not None else None
        self.type = kwargs.get("Type", None) if kwargs is not None else None
        self.itemDescription = ItemDescription(**kwargs.get("ItemDescription", None)) if kwargs is not None else None #Need to improve
