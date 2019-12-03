
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import API
class RealmRoyale(API):
  # GET /getleaderboard[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{queue_id}/{ranking_criteria}
  def leaderboard(self, queue_id, ranking_criteria):
    return self.request('getleaderboard', params=[queue_id, ranking_criteria])

  # GET /getplayer[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}|{player_name}/{"hirez"}] | {steam_id}/{"steam"}
  def player(self, player, platform=None):
    plat = platform if platform else 'hirez' if not str(player).isdigit() or str(player).isdigit() and len(str(player)) <= 8 else 'steam'
    return self.request('getplayer', params=[player, plat])#PlayerNotFound("Player doesn't exist or it's hidden"))

  # GET /getplayermatchhistory[response_format]/{dev_id}/{signature}/{session_id}/{player_id}
  # GET /getplayermatchhistoryafterdatetime[response_format]/{dev_id}/{signature}/{session_id}/{start_datetime}/{player_id}
  def match_history(self, player_id, start_datetime=None):
    from datetime import datetime
    methodName = 'getplayermatchhistory' if not start_datetime else 'getplayermatchhistoryafterdatetime'
    params = player_id if not start_datetime else [start_datetime.strftime('yyyyMMddHHmmss') if isinstance(start_datetime, datetime) else start_datetime, playerId]
    return self.request(methodName, params=params)

  # GET /getplayerstats[response_format]/{dev_id}/{signature}/{session_id}/{player_id}
  def player_stats(self, player_id):
    return self.request('getplayerstats', params=player_id)

  # GET /getTalents[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{language_code}
  def items(self, language=None):
    from ..enums.language import Language
    return self.request('gettalents', params=language or Language.English)

__all__ = (
	'RealmRoyale',
)
