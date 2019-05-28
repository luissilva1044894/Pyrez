class Dict:
    def __init__(self, **kwargs):
        self.__kwargs__ = kwargs or []
    def __getitem__(self, key):
        try:
            return self.__kwargs__[key]
        except KeyError:
            return None
    def __iter__(self):
        return (self.__kwargs__[key] for key in self.__kwargs__)
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        import json
        return json.dumps(self.__kwargs__, sort_keys=True, indent=2) if self.__kwargs__ else None #return str(self.__kwargs__).replace("'", "\"") if self.__kwargs__ else None
