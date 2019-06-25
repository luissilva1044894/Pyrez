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
    def __contains__(self, key):
        return key in self.__kwargs__
    def __dir__(self):
        if isinstance(self.__kwargs__, dict):
            return self.__kwargs__.keys()
        return []
    def __len__(self):
        return len(self.__kwargs__)
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        from ...utils.json import to_json
        return to_json(self.__kwargs__)
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
