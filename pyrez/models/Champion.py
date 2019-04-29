from pyrez.enumerations import Champions
from .BaseCharacter import BaseCharacter
from .ChampionAbility import ChampionAbility
class Champion(BaseCharacter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Champions(kwargs.get("id"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("id", 0) if kwargs is not None else 0
            self.godName = kwargs.get("Name", None) if kwargs is not None else None
        for i in range(0, 5):
            obj = ChampionAbility(**kwargs.get("Ability_" + str(i + 1), None))
            self.abilitys.append(obj)
        self.onFreeWeeklyRotation = str(kwargs.get("OnFreeWeeklyRotation", None)).lower() == 'y'
        self.godCardURL = kwargs.get("ChampionCard_URL", None) if kwargs is not None else None
        self.godIconURL = kwargs.get("ChampionIcon_URL", None) if kwargs is not None else None
    def __str__(self):
        st = "Name: {0} ID: {1} Health: {2} Roles: {3} Title: {4}".format(self.godName, self.godId.getId() if isinstance(self.godId, Champions) else self.godId, self.health, self.roles, self.title)
        for i in range(0, len(self.abilitys)):
            st +=(" Ability {0}: {1}").format(i + 1, self.abilitys [i])
        st += "CardUrl: {0} IconUrl: {1} ".format(self.godCardURL, self.godIconURL)
        return st
