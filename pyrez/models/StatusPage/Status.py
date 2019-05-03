from pyrez.models import BaseAPIResponse
class Status(BaseAPIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.indicator = kwargs.get("indicator", None) if kwargs else None
        self.description = kwargs.get("description", None) if kwargs else None
