from pyrez.models import APIResponseBase
from .Page import Page
class Base(APIResponseBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.page = Page(**kwargs.get("page", None)) if kwargs.get("page", None) else None
