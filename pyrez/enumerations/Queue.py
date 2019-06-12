from .Enum import Enum
class Queue(Enum):
    def isLiveMatch(self):
        return "live" in self.getName().lower()
    def isPraticeMatch(self):
        return "pratice" in self.getName().lower()
    def isRanked(self):
        return "competitive" in self.getName().lower()
