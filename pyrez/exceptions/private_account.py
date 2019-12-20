
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .unknown_player import UnknownPlayer 
class PrivateAccount(UnknownPlayer):
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)

__all__ = (
  'PrivateAccount',
)
