from .APIResponse import APIResponse
class TeamSearch(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.teamFounder = kwargs.get("Founder", None) if kwargs is not None else None
        self.teamName = kwargs.get("Name", None) if kwargs is not None else None
        self.players = kwargs.get("Players", 0) if kwargs is not None else 0
        self.teamTag = kwargs.get("Tag", None) if kwargs is not None else None
        self.teamId = kwargs.get("TeamId", 0) if kwargs is not None else 0
