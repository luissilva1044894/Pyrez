from pyrez.models import APIResponse
class Search(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.teamFounder = kwargs.get("Founder", '') or ''
        self.teamName = kwargs.get("Name", '') or ''
        self.players = kwargs.get("Players", 0) or 0
        self.teamTag = kwargs.get("Tag", '') or ''
        self.teamId = kwargs.get("TeamId", 0) or 0
