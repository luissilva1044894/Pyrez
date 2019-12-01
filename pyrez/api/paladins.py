
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .base_paladins_smite import BasePaladinsSmite
class Paladins(BasePaladinsSmite):
	'''
	# GET /getchampions[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{language_code}
	def get_champions(self, language=Language.English):
		return self.request('getchampions', params=language or Language.English)
	# GET /getchampioncards[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{god_id}/{language_code}
	def get_champion_cards(self, god_id, language=Language.English):
		return self.request('getchampioncards', params=[god_id, language or Language.English])
	# GET /getchampionleaderboard[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{god_id}/{queue_id}
	def get_champion_leaderboard(self, god_id, queue_id=QueuePaladins.Live_Competitive_Keyboard):
		return self.request('getchampionleaderboard', params=[god_id, queue_id or QueuePaladins.Live_Competitive_Keyboard])
	# GET /getchampionranks[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}
	def get_champion_ranks(self, player_id):
		return self.request('getchampionranks', params=player_id)
	# GET /getchampionskins[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{god_id}/{language_code}
	def get_champion_skins(self, god_id, language=Language.English):
		return self.request('getchampionskins', params=[god_id, language or Language.English])
	'''
	# return self.__request_method__('getplayer', params=[player, portalId] if portalId else [player], raises=PlayerNotFound("Player doesn't exist or it's hidden"))

	# GET /getplayerloadouts[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}/{language_code}
	def get_player_loadouts(self, player_id, language=None):
		from ..enums.language import Language
		return self.request('getplayerloadouts', params=[player_id, language or Language.English])

	# GET /getplayerbatchfrommatch[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{match_id}
	def get_players_from_match(self, match_id):
		return self.request('getplayerbatchfrommatch', params=match_id)	

	# GET /getplayerchampions[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}
	def get_player_champions(self, player_id):
		return self.request('getplayerchampions', params=player_id)	

__all__ = (
	'Paladins',
)
