from .APIResponse import APIResponse
class Skin(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.skinId1 = kwargs.get("skin_id1", 0) if kwargs else 0
        self.skinId2 = kwargs.get("skin_id2", 0) if kwargs else 0
        self.skinName = kwargs.get("skin_name", None) if kwargs else None
        self.skinNameEnglish = kwargs.get("skin_name_english", None) if kwargs else None
        self.obtainability = kwargs.get("rarity", kwargs.get("obtainability", None)) if kwargs else None
    def __eq__(self, other):
        return self.skinId1 == other.skinId1 and self.skinId2 == other.skinId2
