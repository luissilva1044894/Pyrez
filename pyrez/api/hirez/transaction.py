
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ...models.api_response import APIResponse
class Transaction(APIResponse):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    from ...utils.time import iso_or_string
    from ...utils.num import num_or_string
    self.creation_date = iso_or_string(kwargs.get('creation_dt')) or None
    self.order_num = num_or_string(kwargs.get('order_no')) or 0
    self.ip_address = kwargs.get('ip_address') or None
    self.item_name = kwargs.get('item_name') or None
    self.currency = kwargs.get('currency_cd') or None
    self.price = num_or_string(kwargs.get('price')) or 0
    self.gift_player = kwargs.get('gift_recipient_player') or None
    self.gift_sender = kwargs.get('gift_sender_name') or None
    self.gift_message = kwargs.get('gift_message') or None
