class Dict:
    def __init__(self, **kwargs):
        self.__kwargs = kwargs or []
    def __getitem__(self, key):
        try:
            return self.__kwargs[key]
        except KeyError:
            return None
    def __str__(self):
        import json
        return json.dumps(self.__kwargs, sort_keys=True, indent=2) if self.__kwargs else '' #return str(self.__kwargs).replace("'", "\"") if self.__kwargs else None
