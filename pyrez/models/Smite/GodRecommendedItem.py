from pyrez.models import APIResponse
from pyrez.enumerations import Gods
class GodRecommendedItem(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Gods(kwargs.get("god_id"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("god_id", 0) or 0
            self.godName = kwargs.get("god_name", '') or ''
        self.category = kwargs.get("Category", '') or ''
        self.item = kwargs.get("Item", '') or ''
        self.role = kwargs.get("Role", '') or ''
        self.categoryValueId = kwargs.get("category_value_id", 0) or 0
        self.iconId = kwargs.get("icon_id", 0) or 0
        self.itemId = kwargs.get("item_id", 0) or 0
        self.roleValueId = kwargs.get("role_value_id", 0) or 0
