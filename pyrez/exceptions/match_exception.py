
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .__init__ import PyrezException
class MatchException(PyrezException):
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)

__all__ = (
  'MatchException',
)
