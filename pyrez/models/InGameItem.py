class InGameItem:
    def __init__(self, itemID, itemName, itemLevel):
        self.itemId = itemID
        self.itemName = itemName
        self.itemLevel = itemLevel
    def __str__(self):
        return self.itemName
