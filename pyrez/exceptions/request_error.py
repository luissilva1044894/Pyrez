
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .__init__ import PyrezException
class RequestError(PyrezException):
  """Web request returns unsucessful status."""
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)

__all__ = (
  'RequestError',
)
