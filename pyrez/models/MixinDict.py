class MixinDict:
    def __init__(self, **kwargs):
        self.__kwargs = kwargs if kwargs else None
    def __getitem__(self, key):
        try:
            return self.__kwargs[key]
        except KeyError:
            return None
    def __str__(self):
        import json
        return json.dumps(self.__kwargs) if self.__kwargs else None #return str(self.__kwargs).replace("'", "\"") if self.__kwargs else None
