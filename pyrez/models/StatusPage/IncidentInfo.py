from .ComponentMixin import ComponentMixin
from .IncidentUpdates import IncidentUpdates
from .Component import Component
class IncidentInfo(ComponentMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name", None) if kwargs else None
        self.status = kwargs.get("status", None) if kwargs else None
        self.monitoringAt = kwargs.get("monitoring_at", None) if kwargs else None
        self.resolvedAt = kwargs.get("resolved_at", None) if kwargs else None
        self.impact = kwargs.get("impact", None) if kwargs else None
        self.shortlink = kwargs.get("shortlink", None) if kwargs else None
        self.startedAt = kwargs.get("started_at", None) if kwargs else None
        self.pageId = kwargs.get("page_id", None) if kwargs else None
        self.incidentUpdates = [ IncidentUpdates(**_) for _ in (kwargs.get("incident_updates", None) or []) ]
        self.components = [ Component(**_) for _ in (kwargs.get("components", None) or []) ]
