
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

class PyrezException(Exception):
  """Base exception for this library, catch-all for most Pyrez issues."""
  def __init__(self, *args, **kw):
    Exception.__init__(self, *args, **kw)
  def __str__(self):
    if self.args:
      return str(self.args[-1])
    return 'An unknown error has occured within Pyrez'

#https://docs.python.org/3/library/exceptions.html#DeprecationWarning
__all__ = (
  'PyrezException',
  'deprecated',
  'invalid_argument',
  'invalid_session_id',
  'invalid_time',
  'match_exception',
  'no_result',
  'not_found',
  'not_supported',
  'paladins_only',
  'player_not_found',
  'private_account',
  'rate_limit_exceeded',
  'realm_royale_only',
  'request_error',
  'session_limit_exceeded',
  'smite_only',
  'unauthorized_error',
  'unexpected_exception',
  'unknown_player',
)
