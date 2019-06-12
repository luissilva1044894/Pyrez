from pyrez.enumerations import Champions
from pyrez.models import God as BaseCharacter
from .ChampionAbility import ChampionAbility
class Champion(BaseCharacter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Champions(kwargs.get("id"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("id", 0) if kwargs else 0
            self.godName = kwargs.get("Name", None) if kwargs else None
        for i in range(0, 5):
            obj = ChampionAbility(**kwargs.get("Ability_" + str(i + 1), None))
            self.abilitys.append(obj)
        self.onFreeWeeklyRotation = str(kwargs.get("OnFreeWeeklyRotation", None)).lower() == 'y' if kwargs else False
        self.godCardURL = kwargs.get("ChampionCard_URL", None) if kwargs else None
        self.godIconURL = kwargs.get("ChampionIcon_URL", None) if kwargs else None
