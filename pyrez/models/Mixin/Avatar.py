class Avatar:
    __slots__ = ("avatarId", "avatarURL")

    def __init__(self, **kwargs):
        self.avatarId = kwargs.get("avatarId",  kwargs.get("AvatarId", 0)) if kwargs else 0
        self.avatarURL = kwargs.get("avatarURL", kwargs.get("Avatar_URL", None)) if kwargs else None
    def __repr__(self):
        return "<Avatar {0.avatarId}>".format(self)
    #def __hash__(self):
        #return hash(self.avatarId)
    def __eq__(self, other):
        return self.avatarId == other.avatarId
