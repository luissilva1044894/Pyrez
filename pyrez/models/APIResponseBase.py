from .DictMixin import DictMixin
class APIResponseBase(DictMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.json = kwargs if kwargs else None
