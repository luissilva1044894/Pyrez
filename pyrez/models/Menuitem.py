class Menuitem:
    def __init__(self, **kwargs):
        self.description = kwargs.get("Description", '') or ''
        self.value = kwargs.get("Value", 0) or 0
