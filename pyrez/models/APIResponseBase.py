from .MixinDict import MixinDict
class APIResponseBase(MixinDict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.json = kwargs if kwargs else None
