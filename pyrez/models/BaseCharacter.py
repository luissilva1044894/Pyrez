from .APIResponse import APIResponse
class BaseCharacter(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.abilitys = []
        self.cons = kwargs.get("Cons", None) if kwargs is not None else None
        self.health = kwargs.get("Health", 0) if kwargs is not None else 0
        self.lore = kwargs.get("Lore", None) if kwargs is not None else None
        self.onFreeRotation = str(kwargs.get("OnFreeRotation", None)).lower() == 'y'
        self.pantheon = kwargs.get("Pantheon", None) if kwargs is not None else None
        self.pros = kwargs.get("Pros", None) if kwargs is not None else None
        self.roles = kwargs.get("Roles", None) if kwargs is not None else None
        self.speed = kwargs.get("Speed", 0) if kwargs is not None else 0
        self.title = kwargs.get("Title", None) if kwargs is not None else None
        self.type = kwargs.get("Type", None) if kwargs is not None else None
        self.latestGod = str(kwargs.get("latestChampion", kwargs.get("latestGod", None))).lower() == 'y'
