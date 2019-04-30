from .BaseSkin import BaseSkin
from pyrez.enumerations import Gods
class GodSkin(BaseSkin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Gods(kwargs.get("god_id"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("god_id", 0) if kwargs else 0
            self.godName = kwargs.get("god_name", None) if kwargs else None
        self.godIconURL = kwargs.get("godIcon_URL", None) if kwargs else None
        self.godSkinURL = kwargs.get("godSkin_URL", None) if kwargs else None
        self.priceFavor = kwargs.get("price_favor", 0) if kwargs else 0
        self.priceGems = kwargs.get("price_gems", 0) if kwargs else 0
