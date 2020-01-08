
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .deprecated import Deprecated
class NotSupported(Deprecated):
  """Indicates a feature or method is not supported."""
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)

__all__ = (
  'NotSupported',
)
