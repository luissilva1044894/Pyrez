from .ComponentMixin import ComponentMixin
class Component(ComponentMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name", '') or ''
        self.status = kwargs.get("status", '') or ''
        self.position = kwargs.get("position", 0) or 0
        self.description = kwargs.get("description", '') or ''
        self.showcase = kwargs.get("showcase", False) or False
        self.groupId = kwargs.get("group_id", '') or ''
        self.pageId = kwargs.get("page_id", '') or ''
        self.group = kwargs.get("group", False) or False
        self.onlyShowIfDegraded = kwargs.get("only_show_if_degraded", False) or False
        self.components = kwargs.get("components", '') or ''
