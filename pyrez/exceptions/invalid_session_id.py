
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .unauthorized_error import UnauthorizedError
class InvalidSessionId(UnauthorizedError):
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)

__all__ = (
  'InvalidSessionId',
)
