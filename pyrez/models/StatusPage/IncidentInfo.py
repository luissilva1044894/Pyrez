from .ComponentMixin import ComponentMixin
from .IncidentUpdates import IncidentUpdates
from .Component import Component
class IncidentInfo(ComponentMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name", '') or ''
        self.status = kwargs.get("status", '') or ''
        self.monitoringAt = kwargs.get("monitoring_at", '') or ''
        self.resolvedAt = kwargs.get("resolved_at", '') or ''
        self.impact = kwargs.get("impact", '') or ''
        self.shortlink = kwargs.get("shortlink", '') or ''
        self.startedAt = kwargs.get("started_at", '') or ''
        self.pageId = kwargs.get("page_id", '') or ''
        self.incidentUpdates = [ IncidentUpdates(**_) for _ in (kwargs.get("incident_updates", None) or []) ]
        self.components = [ Component(**_) for _ in (kwargs.get("components", None) or []) ]
