class BaseAPIResponse:
    def __init__(self, **kwargs):
        self.json = kwargs if kwargs is not None else None
    def __getitem__(self, key):
        try:
            return self.json[key]
        except KeyError:
            return None
    def __str__(self):
        import json
        return json.dumps(self.json) if self.json is not None else None #return str(self.json).replace("'", "\"") if self.json is not None else None
