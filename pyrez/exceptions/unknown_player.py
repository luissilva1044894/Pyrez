
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .__init__ import PyrezException 
class UnknownPlayer(PyrezException):
	"""Raises an error when a player does not exist via the API"""
	def __init__(self, *args, **kw):
		super().__init__(*args or ('The specified player was not found',), **kw)

__all__ = (
  'UnknownPlayer',
)