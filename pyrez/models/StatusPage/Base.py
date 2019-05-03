from pyrez.models import BaseAPIResponse
from .Page import Page
class Base(BaseAPIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.page = Page(**kwargs.get("page", None)) if kwargs.get("page", None) else None
