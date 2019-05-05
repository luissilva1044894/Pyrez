from .Base import Base
from .IncidentInfo import IncidentInfo
class Incidents(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.incidents = [ IncidentInfo(**_) for _ in (kwargs.get("incidents", None) or []) ]
