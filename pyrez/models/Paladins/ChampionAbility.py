from pyrez.models import Ability
class ChampionAbility(Ability):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description = kwargs.get("Description", None) if kwargs else None
        self.damageType = kwargs.get("damageType", None) if kwargs else None
        self.rechargeSeconds = kwargs.get("rechargeSeconds", 0) if kwargs else None
