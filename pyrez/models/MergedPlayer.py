from .APIResponseBase import APIResponseBase
from pyrez.models.Mixin import Player as PlayerMixin
class MergedPlayer(APIResponseBase, PlayerMixin):
    def __init__(self, **kwargs):
        APIResponseBase.__init__(self, **kwargs)
        PlayerMixin.__init__(self, **kwargs)
        self.mergeDatetime = kwargs.get("merge_datetime", None) if kwargs else None
        self.portalId = kwargs.get("portalId", 0) if kwargs else 0
    #def __repr__(self):
        #return "<MergedPlayer {}>".format(self.playerId)
    