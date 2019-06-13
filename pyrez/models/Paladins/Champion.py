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
            self.godId = kwargs.get("id", 0) or 0
            self.godName = kwargs.get("Name", '') or ''
        for i in range(0, 5):
            obj = ChampionAbility(**kwargs.get("Ability_" + str(i + 1), None))
            self.abilitys.append(obj)
        self.onFreeWeeklyRotation = str(kwargs.get("OnFreeWeeklyRotation", '')).lower() == 'y' or False
        self.godCardURL = kwargs.get("ChampionCard_URL", '') or ''
        self.godIconURL = kwargs.get("ChampionIcon_URL", '') or ''
