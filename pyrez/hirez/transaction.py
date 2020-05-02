
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

from ...models.api_response import APIResponse
from ...utils.num import num_or_string
from ...utils.time import iso_or_string

class Transaction(APIResponse):
  def __init__(self, **kw):
    super().__init__(**kw)
    self.creation_date = iso_or_string(kw.get('creation_dt')) or None
    self.order_num = num_or_string(kw.get('order_no')) or 0
    self.ip_address = kw.get('ip_address') or None
    self.item_name = kw.get('item_name') or None
    self.currency = kw.get('currency_cd') or None
    self.price = num_or_string(kw.get('price')) or 0
    self.gift_player = kw.get('gift_recipient_player') or None
    self.gift_sender = kw.get('gift_sender_name') or None
    self.gift_message = kw.get('gift_message') or None
