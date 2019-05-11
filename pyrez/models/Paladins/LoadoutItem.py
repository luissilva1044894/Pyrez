from pyrez.models import APIResponseBase
class LoadoutItem(APIResponseBase):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.itemId = kwargs.get("ItemId", 0) if kwargs else 0
		self.itemName = kwargs.get("ItemName", None) if kwargs else None
		self.points = kwargs.get("Points", 0) if kwargs else 0
	def __str__(self):
		return "{0.itemName} ({0.points})".format(self)
	def getCard(self):
		return "https://web2.hirez.com/paladins/champion-cards/{}.jpg".format(self.itemName.lower().replace(' ', '-'))
	def getFrame(self):
		return "https://web2.hirez.com/paladins/cards/frame-{}.png".format(self.points)
