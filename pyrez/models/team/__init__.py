
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ..api_response import APIResponse
class Team(APIResponse):
	def __init__(self, *, api=None, **kw):
    APIResponse.__init__(self, **kw)
    self.founder = kw.get('Founder') or None
    self.founder_id = kw.get('FounderId') or 0
    self.name = kw.get('Name') or None
    self.players = kw.get('Players') or 0
    self.tag = kw.get('Tag') or None
    self.id = kw.get('TeamId') or 0

__all__ = (
	'Team',
	'info',
	'player',
	'search',
)
