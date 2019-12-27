
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .request_error import RequestError
class NoResult(RequestError):
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)

__all__ = (
  'NoResult',
)
