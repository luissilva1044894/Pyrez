from pyrez.models import APIResponse
from pyrez.models.Mixin import Winratio
class Info(APIResponse, Winratio):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)
        Winratio.__init__(self, **kwargs)
        self.teamFounder = kwargs.get("Founder", '') or ''
        self.teamFounderId = kwargs.get("FounderId", 0) or 0
        self.teamName = kwargs.get("Name", '') or ''
        self.players = kwargs.get("Players", 0) or 0
        self.rating = kwargs.get("Rating", 0) or 0
        self.teamTag = kwargs.get("Tag", '') or ''
        self.teamId = kwargs.get("TeamId", 0) or 0
