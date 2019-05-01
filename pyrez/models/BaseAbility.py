class BaseAbility:#class Ability
    def __init__(self, **kwargs):
        self.id = kwargs.get("Id", 0) if kwargs else 0
        self.summary = kwargs.get("Summary", None) if kwargs else None
        self.url = kwargs.get("URL", None) if kwargs else None
    def __str__(self):
        return "ID: {} Description: {} Summary: {} Url: {}".format(self.id, self.summary, self.url)
