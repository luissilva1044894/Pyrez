from pyrez.models import APIResponseBase
class AffectedComponents(APIResponseBase):
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.code = kwargs.get("code", '') or ''
    	self.name = kwargs.get("name", '') or ''
    	self.oldStatus = kwargs.get("old_status", '') or ''
    	self.newStatus = kwargs.get("new_status", '') or ''
