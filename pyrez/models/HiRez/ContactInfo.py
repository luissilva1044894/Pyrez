from pyrez.models import APIResponseBase
class ContactInfo(APIResponseBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.email = kwargs.get("email", None) if kwargs else None
        self.backupEmail = kwargs.get("backupEmail", None) if kwargs else None
        self.subscriber = kwargs.get("subscriber", False) if kwargs else False
        self.currency = kwargs.get("currency", None) if kwargs else None
        self.country = kwargs.get("country", None) if kwargs else None
