
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .unauthorized_error import UnauthorizedError
class RateLimitExceeded(UnauthorizedError):
  """Request rejected due to the rate limit being exceeded."""
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)

__all__ = (
  'RateLimitExceeded',
)
