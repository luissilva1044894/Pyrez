
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .. import API
class RealmRoyale(API):
  # GET /getleaderboard[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{queue_id}/{ranking_criteria}
  def leaderboard(self, queue_id, ranking_criteria, **kw):
    return self.request('getleaderboard', params=[queue_id, ranking_criteria], **kw)

  # GET /getplayer[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}|{player_name}/{"hirez"}] | {steam_id}/{"steam"}
  def player(self, player, platform=None, **kw):
    from ..enums.portal import Portal
    return self.request('getplayer', params=player if not platform else [player, Portal(platform) or 'hirez'], **kw)#PlayerNotFound("Player doesn't exist or it's hidden"))

  # GET /getplayermatchhistory[response_format]/{dev_id}/{signature}/{session_id}/{player_id}
  # GET /getplayermatchhistoryafterdatetime[response_format]/{dev_id}/{signature}/{session_id}/{start_datetime}/{player_id}
  def match_history(self, player_id, start_datetime=None, **kw):
    params = player_id if not start_datetime else [start_datetime.strftime('yyyyMMddHHmmss') if hasattr(start_datetime, 'strftime') else start_datetime, player_id]
    return self.request('getplayermatchhistory' if not start_datetime else 'getplayermatchhistoryafterdatetime', params=params, **kw)

  # GET /getplayerstats[response_format]/{dev_id}/{signature}/{session_id}/{player_id}
  def player_stats(self, player_id, **kw):
    return self.request('getplayerstats', params=player_id, **kw)

  # GET /getTalents[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{language_code}
  def items(self, language=None, **kw):
    from ..enums.language import Language
    return self.request('gettalents', params=Language(language), **kw)

__all__ = (
  'RealmRoyale',
)
