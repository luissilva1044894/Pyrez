from .ComponentMixin import ComponentMixin
from .AffectedComponents import AffectedComponents
class IncidentUpdates(ComponentMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status = kwargs.get("status", None) if kwargs else None #resolved
        self.body = kwargs.get("body", None) if kwargs else None
        self.incidentId = kwargs.get("incident_id", None) if kwargs else None
        self.displayAt = kwargs.get("display_at", None) if kwargs else None
        self.affectedComponents = [ AffectedComponents(**_) for _ in (kwargs.get("affected_components", None) or []) ]
        self.deliverNotifications = kwargs.get("deliver_notifications", False) if kwargs else False
        self.customTweet = kwargs.get("custom_tweet", None) if kwargs else None
        self.tweetId = kwargs.get("tweet_id", 0) if kwargs else 0
