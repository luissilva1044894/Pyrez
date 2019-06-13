from .Enum import Enum
class Queue(Enum):
    @property
    def isLiveMatch(self):
        return "live" in self.getName().lower()
    @property
    def isPraticeMatch(self):
        return "pratice" in self.getName().lower()
    @property
    def isRanked(self):
        return "competitive" in self.getName().lower()
