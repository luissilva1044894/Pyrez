from .BaseEnum import BaseEnum
class Queue(BaseEnum):
    def isLiveMatch(self):
        return "live" in self.getName().lower()
    def isPraticeMatch(self):
        return "pratice" in self.getName().lower()
    def isRanked(self):
        return "competitive" in self.getName().lower()
