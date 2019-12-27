
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .not_supported import NotSupported
class SmiteOnly(NotSupported):
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)

__all__ = (
  'SmiteOnly',
)
