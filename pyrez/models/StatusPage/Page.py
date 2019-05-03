from pyrez.models import APIResponseBase
class Page(APIResponseBase):
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.id = kwargs.get("id", None) if kwargs else None
    	self.name = kwargs.get("name", None) if kwargs else None
    	self.url = kwargs.get("url", None) if kwargs else None
    	self.timezone = kwargs.get("time_zone", None) if kwargs else None
    	self.updatedAt = kwargs.get("updated_at", None) if kwargs else None
