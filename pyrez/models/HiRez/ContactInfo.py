from pyrez.models import APIResponseBase
class ContactInfo(APIResponseBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.email = kwargs.get("email", '') or ''
        self.backupEmail = kwargs.get("backupEmail", '') or ''
        self.subscriber = kwargs.get("subscriber", False) or False
        self.currency = kwargs.get("currency", '') or ''
        self.country = kwargs.get("country", '') or ''
