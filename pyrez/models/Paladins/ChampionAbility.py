from pyrez.models import Ability
class ChampionAbility(Ability):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description = kwargs.get("Description", '') or ''
        self.damageType = kwargs.get("damageType", '') or ''
        self.rechargeSeconds = kwargs.get("rechargeSeconds", 0) or 0
