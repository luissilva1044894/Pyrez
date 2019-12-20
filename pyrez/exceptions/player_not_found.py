
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .unknown_player import UnknownPlayer 
class PlayerNotFound(UnknownPlayer):
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)

__all__ = (
  'PlayerNotFound',
)
