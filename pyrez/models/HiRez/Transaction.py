from pyrez.models import APIResponseBase
class Transaction(APIResponseBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.creationDate = kwargs.get("creation_dt", '') or ''
        self.orderNum = kwargs.get("order_no", '') or ''
        self.ipAddress = kwargs.get("ip_address", '') or ''
        self.itemName = kwargs.get("item_name", '') or ''
        self.currency = kwargs.get("currency_cd", '') or ''
        self.price = kwargs.get("price", '') or ''
        self.giftPlayer = kwargs.get("gift_recipient_player", '') or ''
        self.giftSender = kwargs.get("gift_sender_name", '') or ''
        self.giftMessage = kwargs.get("gift_message", '') or ''
