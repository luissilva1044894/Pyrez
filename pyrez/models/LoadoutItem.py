class LoadoutItem:
    def __init__(self, **kwargs):
        self.itemId = kwargs.get("ItemId", 0) if kwargs is not None else 0
        self.itemName = kwargs.get("ItemName", None) if kwargs is not None else None
        self.points = kwargs.get("Points", 0) if kwargs is not None else 0
    def __str__(self):
        return "{0}({1})".format(self.itemName, self.points)
