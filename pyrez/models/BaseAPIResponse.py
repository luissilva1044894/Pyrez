from .DictMixin import DictMixin
class BaseAPIResponse(DictMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.json = kwargs if kwargs else None
    """
    def __getitem__(self, key):
        try:
            return self.json[key]
        except KeyError:
            return None
    def __str__(self):
        import json
        return json.dumps(self.json) if self.json else None
    """
