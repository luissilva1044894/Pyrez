from pyrez.models import APIResponse
class Search(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.teamFounder = kwargs.get("Founder", None) if kwargs else None
        self.teamName = kwargs.get("Name", None) if kwargs else None
        self.players = kwargs.get("Players", 0) if kwargs else 0
        self.teamTag = kwargs.get("Tag", None) if kwargs else None
        self.teamId = kwargs.get("TeamId", 0) if kwargs else 0
