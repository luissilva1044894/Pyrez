from pyrez.models import APIResponseBase
class Status(APIResponseBase):
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.indicator = kwargs.get("indicator", '') or ''
    	self.description = kwargs.get("description", '') or ''
