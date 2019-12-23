
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Team
class Info(Team):
  def __init__(self, *, api=None, **kw):
    super().__init__(api=api, **kw)
    self.rating = kw.get('Rating') or 0
