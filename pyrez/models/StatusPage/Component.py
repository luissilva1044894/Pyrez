from .ComponentMixin import ComponentMixin
class Component(ComponentMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name", None) if kwargs else None
        self.status = kwargs.get("status", None) if kwargs else None
        self.position = kwargs.get("position", 0) if kwargs else 0
        self.description = kwargs.get("description", None) if kwargs else None
        self.showcase = kwargs.get("showcase", False) if kwargs else False
        self.groupId = kwargs.get("group_id", None) if kwargs else None
        self.pageId = kwargs.get("page_id", None) if kwargs else None
        self.group = kwargs.get("group", False) if kwargs else False
        self.onlyShowIfDegraded = kwargs.get("only_show_if_degraded", False) if kwargs else False
        self.components = kwargs.get("components", None) if kwargs else None
