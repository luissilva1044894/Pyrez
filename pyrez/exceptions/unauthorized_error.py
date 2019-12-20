
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .__init__ import PyrezException 
class UnauthorizedError(PyrezException):
  """Raised when the current Credentials is invalid, blocked or missing"""
  def __init__(self, *args, **kw):
    #you try to access a resource and it fails due to some issue with your authentication
    super().__init__(*args, **kw)

__all__ = (
  'UnauthorizedError',
)
