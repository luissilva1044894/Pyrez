class Dict:
    def __init__(self, **kwargs):
        self.__kwargs__ = kwargs or []
    def __getattr__(self, key):
        if key not in self.__dict__:
            return self.__kwargs__.get(key)
    def __getitem__(self, key):
        try:
            return self.__kwargs__[key]
        except KeyError:
            return None
    def __contains__(self, key):
        return key in self.__kwargs__
    def __dir__(self):
        if isinstance(self.__kwargs__, dict):
            return self.__kwargs__.keys()
        return []
    def __len__(self):
        return len(self.__kwargs__)
    def __iter__(self):
        return (key for key in self.__kwargs__) #return (self.__kwargs__[key] for key in self.__kwargs__)
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        import json
        return json.dumps(self.__kwargs__, ensure_ascii=True, sort_keys=True, indent=2) if self.__kwargs__ else None #return str(self.__kwargs__).replace("'", "\"") if self.__kwargs__ else None
