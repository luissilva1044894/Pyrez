from .APIResponse import APIResponse
class Item(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.deviceName = kwargs.get("DeviceName", 0) if kwargs else 0
        self.iconId = kwargs.get("IconId", 0) if kwargs else 0
        self.itemId = kwargs.get("ItemId", 0) if kwargs else 0
        self.itemPrice = kwargs.get("Price", 0) if kwargs else 0
        self.shortDesc = kwargs.get("ShortDesc", None) if kwargs else None
        self.itemIconURL = kwargs.get("itemIcon_URL", None) if kwargs else None
    def __eq__(self, other):
        return self.itemId == other.itemId
