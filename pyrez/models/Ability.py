#from .APIResponseBase import APIResponseBase
class Ability:#Ability(APIResponseBase):
    def __init__(self, **kwargs):
    	#super().__init__(**kwargs)
    	self.id = kwargs.get("Id", 0) if kwargs else 0
    	self.summary = kwargs.get("Summary", None) if kwargs else None
    	self.url = kwargs.get("URL", None) if kwargs else None
    def __str__(self):
    	return "ID: {0.id} Summary: {0.summary} Url: {0.url}".format(self)
