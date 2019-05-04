from .MergedPlayer import MergedPlayer
class MergedPlayerMixin:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mergedPlayers = [ MergedPlayer(**_) for _ in (kwargs.get("MergedPlayers") if kwargs.get("MergedPlayers", None) else []) ]