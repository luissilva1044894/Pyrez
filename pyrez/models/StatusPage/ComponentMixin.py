from pyrez.models import APIResponseBase
class ComponentMixin(APIResponseBase):
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.id = kwargs.get("id", '') or ''
    	self.createAt = kwargs.get("created_at", '') or ''
    	self.updatedAt = kwargs.get("updated_at", '') or ''
