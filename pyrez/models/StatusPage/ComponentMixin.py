from pyrez.models import APIResponseBase
class ComponentMixin(APIResponseBase):
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.id = kwargs.get("id", None) if kwargs else None
    	self.createAt = kwargs.get("created_at", None) if kwargs else None
    	self.updatedAt = kwargs.get("updated_at", None) if kwargs else None
