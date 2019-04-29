from pyrez.enumerations import Champions
from .BaseSkin import BaseSkin
class ChampionSkin(BaseSkin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Champions(kwargs.get("champion_id"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("champion_id", 0) if kwargs is not None else 0
            self.godName = kwargs.get("champion_name", None) if kwargs is not None else None
