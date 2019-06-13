from .APIResponse import APIResponse
class God(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.abilitys = []
        self.cons = kwargs.get("Cons", '') or ''
        self.health = kwargs.get("Health", 0) or 0
        self.lore = kwargs.get("Lore", '') or ''
        self.onFreeRotation = str(kwargs.get("OnFreeRotation", '')).lower() == 'y' or False
        self.pantheon = kwargs.get("Pantheon", '') or ''
        self.pros = kwargs.get("Pros", '') or ''
        self.roles = kwargs.get("Roles", '') or ''
        self.speed = kwargs.get("Speed", 0) or 0
        self.title = kwargs.get("Title", '') or ''
        self.type = kwargs.get("Type", '') or ''
        self.latestGod = str(kwargs.get("latestChampion", kwargs.get("latestGod", ''))).lower() == 'y' or False
