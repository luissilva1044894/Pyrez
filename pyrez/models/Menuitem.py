class Menuitem:
    def __init__(self, **kwargs):
        self.description = kwargs.get("Description", None) if kwargs is not None else None
        self.value = kwargs.get("Value", 0) if kwargs is not None else 0
