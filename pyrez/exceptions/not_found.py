
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .no_result import NoResult
class NotFound(NoResult):
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)

__all__ = (
  'NotFound',
)
