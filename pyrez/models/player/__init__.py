
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ..api_response import APIResponse
from ...utils import decorators
class _Base(APIResponse):
	def __init__(self, *, api=None, **kw):
		#APIResponse.__init__(self, **kw)
		super().__init__(**kw)
		self.id = kw.get('player_id') or kw.get('Id') or kw.get('id') or kw.get('playerId') or 0
		if self.id != 0:
			from ...utils.num import try_int
			self.id = try_int(self.id)
		self.name = kw.get('player_name') or kw.get('Name') or kw.get('name') or kw.get('playerName') or None
		if self.name:
			self.name = str(self.name)
		self.portal_id = kw.get('portal_id') or 0
		#self.platform = kw.get('portal_id') or -1 # Steam | Hirez | Hi-Rez | Discord | unknown | PSN | XboxLive | Switch | switch | Nintendo Switch | xbox | 
		# account_id = kw.get('account_id') or 0
		self.__api__ = api
	def __repr__(self):
		return f'<Player {self.name} ({self.id})>'
	def __eq__(self, other):
		if not self.private and isinstance(other, self.__class__):
			return self.id == other.id
		return False
	def __hash__(self):
		return hash(self.id)
	def __int__(self):
		return self.id or -1
	@property
	def public(self): #hidden_profile
		return self.id > 0
	@decorators.is_public
	def expand(self): #info | profile
		if isinstance(self, Player) and self.__class__.__name__ == Player.__name__:
			r = self.__api__.player(self.id)
			if r:
				return Player(api=self.__api__, **r[0])
		return self
	@decorators.is_public
	def status(self):
		r = self.__api__.player_status(self.id)
		if r and r[0]['status'] != 5:
			from ..player.status import Status
			return Status(api=self, **r[0])
	@decorators.is_public
	def friends(self):
		return [Player(api=self.__api__, **p) for p in self.__api__.friends(self.id) if p.get('player_id', 0) not in [0, '0']]
	@decorators.is_public
	def match_history(self, language=None):
		from ...enums.language import Language
		pass #return [PartialMatch(self, language or Language.English, m) for m in self.__api__.match_history(self.id)]

class Base(_Base):
	def __init__(self, *, api=None, **kw):
		super().__init__(api=api, **kw)
		self.created = kw.get('Created_Datetime') or kw.get('created_datetime') or  None
		self.last_login = kw.get('Last_Login_Datetime') or kw.get('last_login_datetime') or None
		self.level = kw.get('Level') or kw.get('level') or 0 #account_level
		self.region = kw.get('Region') or kw.get('region') or None

class Player(Base):
	def __init__(self, *, api=None, **kw):
		super().__init__(api=api, **kw)
		self.steam_id = kw.get('steam_id') or 0

__all__ = (
	'Player',
	'Base',
)
