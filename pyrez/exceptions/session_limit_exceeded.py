
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .rate_limit_exceeded import RateLimitExceeded
class SessionLimitExceeded(RateLimitExceeded):
  """Raised when the maximum number of active sessions is reached."""
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)

__all__ = (
  'SessionLimitExceeded',
)
