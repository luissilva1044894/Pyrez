class Dict:
    def __init__(self, **kwargs):
        self.__kwargs__ = kwargs or []
    def __getitem__(self, key):
        try:
            return self.__kwargs__[key]
        except KeyError:
            return None
    def __iter__(self):
        return (key for key in self.__kwargs__) #return (self.__kwargs__[key] for key in self.__kwargs__)
        #for item in self._items:
            #yield item
    #def __copy__(self):
        #return self.__kwargs__
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        import json
        return json.dumps(self.__kwargs__, ensure_ascii=True, sort_keys=True, indent=2) if self.__kwargs__ else None #return str(self.__kwargs__).replace("'", "\"") if self.__kwargs__ else None
    #def __contains__(self, key):
        #v = None
        #try:
            #v = self[key]
        #except KeyError:
            #return False
        #else:
            #return v is None
    #def __getitem__(self, key):
        # Support index operators.
        #if isinstance(key, int):
            #if abs(key) <= len(self._items):
                #return self._items[key]
        #v = self.get(key)
        #if v is None:
            #raise KeyError(key)
        #return v
