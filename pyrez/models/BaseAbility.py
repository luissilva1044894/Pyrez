class BaseAbility:#class Ability
    def __init__(self, **kwargs):
        self.id = kwargs.get("Id", 0) if kwargs is not None else 0
        self.summary = kwargs.get("Summary", None) if kwargs is not None else None
        self.url = kwargs.get("URL", None) if kwargs is not None else None
    def __str__(self):
        return "ID: {0} Description: {1} Summary: {2} Url: {3}".format(self.id, self.description, self.summary, self.url)
