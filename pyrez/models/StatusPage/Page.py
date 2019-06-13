from pyrez.models import APIResponseBase
class Page(APIResponseBase):
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.id = kwargs.get("id", '') or ''
    	self.name = kwargs.get("name", '') or ''
    	self.url = kwargs.get("url", '') or ''
    	self.timezone = kwargs.get("time_zone", '') or ''
    	self.updatedAt = kwargs.get("updated_at", '') or ''
