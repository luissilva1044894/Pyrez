from .BaseAbility import BaseAbility
class ChampionAbility(BaseAbility):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description = kwargs.get("Description", None) if kwargs is not None else None
        self.damageType = kwargs.get("damageType", None) if kwargs is not None else None
        self.rechargeSeconds = kwargs.get("rechargeSeconds", 0) if kwargs is not None else None
