from pyrez.models import APIResponseBase
class AffectedComponents(APIResponseBase):
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.code = kwargs.get("code", None) if kwargs else None
    	self.name = kwargs.get("name", None) if kwargs else None
    	self.oldStatus = kwargs.get("old_status", None) if kwargs else None
    	self.newStatus = kwargs.get("new_status", None) if kwargs else None
