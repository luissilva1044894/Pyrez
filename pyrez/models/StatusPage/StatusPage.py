from .Base import Base
from .Status import Status
class StatusPage(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status = Status(**kwargs.get("status", None)) if kwargs else None
