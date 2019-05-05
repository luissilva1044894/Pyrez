from .Base import Base
from .IncidentInfo import IncidentInfo
class ScheduledMaintenances(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scheduledMaintenances = [ IncidentInfo(**_) for _ in (kwargs.get("scheduled_maintenances", None) or []) ]
