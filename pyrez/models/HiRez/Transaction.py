from pyrez.models import APIResponseBase
class Transaction(APIResponseBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.creationDate = kwargs.get("creation_dt", None) if kwargs else None
        self.orderNum = kwargs.get("order_no", None) if kwargs else None
        self.ipAddress = kwargs.get("ip_address", None) if kwargs else None
        self.itemName = kwargs.get("item_name", None) if kwargs else None
        self.currency = kwargs.get("currency_cd", None) if kwargs else None
        self.price = kwargs.get("price", None) if kwargs else None
        self.giftPlayer = kwargs.get("gift_recipient_player", None) if kwargs else None
        self.giftSender = kwargs.get("gift_sender_name", None) if kwargs else None
        self.giftMessage = kwargs.get("gift_message", None) if kwargs else None
