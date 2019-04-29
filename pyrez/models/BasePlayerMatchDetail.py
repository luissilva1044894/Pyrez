from .BaseMatch import BaseMatch
class BasePlayerMatchDetail(BaseMatch):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accountLevel = kwargs.get("Account_Level", 0) if kwargs is not None else 0
        self.masteryLevel = kwargs.get("Mastery_Level", 0) if kwargs is not None else 0
