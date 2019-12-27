
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .invalid_argument import InvalidArgument
class InvalidTime(InvalidArgument):
  """Invalid timestamp"""
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)

__all__ = (
  'InvalidTime',
)
