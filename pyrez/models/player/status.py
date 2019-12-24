
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ..match.id import _Base
#from ...utils import decorators
class Status(_Base):

  @property
  def in_match(self):
    return self.match_id != 0 or self.status == 3

  def match_details(self, **kw):
    if self.in_match:
      return super().match_details(self.match_id, is_live=True, **kw)

  @property
  def queue_id(self):
    from ...utils.num import num_or_string
    return num_or_string(self.get('match_queue_id')) or 0

  @property
  def status(self):
    from ...enums import status
    from ...utils.num import num_or_string
    return status.Status(num_or_string(self.get('status_id') or self.get('status')) or 0) or 5

  @property
  def status_message(self):
    return self.get('personal_status_message') or None

  @property
  def status_string(self):
    return self.get('status_string') or kw.get('status') or None
