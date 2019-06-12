class Menuitem:
    def __init__(self, **kwargs):
        self.description = kwargs.get("Description", None) if kwargs else None
        self.value = kwargs.get("Value", 0) if kwargs else 0
