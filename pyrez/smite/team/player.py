
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ...models.api_response import APIResponse
class Player(APIResponse):
  @property
  def level(self):
    from ...utils.num import num_or_string
    return num_or_string(self.get('AccountLevel')) or 0
  @property
  def joined_at(self):
    return self.get('JoinedDatetime') or None
  @property
  def last_login(self):
    return self.get('LastLoginDatetime') or None
  @property
  def name(self):
    return self.get('Name') or None
