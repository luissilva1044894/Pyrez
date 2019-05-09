from pyrez.models.Mixin import Dict
class APIResponseBase(Dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.json = kwargs or []
