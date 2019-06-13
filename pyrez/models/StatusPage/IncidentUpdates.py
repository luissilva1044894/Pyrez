from .ComponentMixin import ComponentMixin
from .AffectedComponents import AffectedComponents
class IncidentUpdates(ComponentMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status = kwargs.get("status", '') or '' #resolved
        self.body = kwargs.get("body", '') or ''
        self.incidentId = kwargs.get("incident_id", '') or ''
        self.displayAt = kwargs.get("display_at", '') or ''
        self.affectedComponents = [ AffectedComponents(**_) for _ in (kwargs.get("affected_components", None) or []) ]
        self.deliverNotifications = kwargs.get("deliver_notifications", False) or False
        self.customTweet = kwargs.get("custom_tweet", '') or ''
        self.tweetId = kwargs.get("tweet_id", 0) or 0
