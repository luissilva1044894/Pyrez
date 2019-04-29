from .BaseCharacter import BaseCharacter
from pyrez.enumerations import Gods
class God(BaseCharacter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Gods(kwargs.get("id"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("id", 0) if kwargs is not None else 0
            self.godName = kwargs.get("Name", None) if kwargs is not None else None
