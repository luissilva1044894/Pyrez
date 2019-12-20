
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import API
class BasePaladinsSmite(API):
  def demo_details(self, match_id):
    return self.request('getdemodetails', params=match_id)
  def esports_league(self):
    return self.request('getesportsproleaguedetails')
  def gods(self, language=None):
    from ..enums.language import Language
    return self.request('getgods', params=language or Language.English)
  def god_leaderboard(self, god_id, language=None):
    from ..enums.language import Language
    return self.request('getgodleaderboard', params=[god_id, language or Language.English])
  def god_ranks(self, player_id, god_id):
    return self.request('getgodranks', params=[player_id, god_id])
  # GET /getgodskins[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{godId}/{languageCode}
  def god_skins(self, god_id, language=None):
    from ..enums.language import Language
    return self.request('getgodskins', params=[god_id, language or Language.English])
  # GET /getitems[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{languagecode}
  def items(self, language=None):
    from ..enums.language import Language
    return self.request('getitems', params=language or Language.English)

  # GET /getmatchhistory[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}
  def match_history(self, player_id):
    return self.request('getmatchhistory', params=player_id)

  def league_leaderboard(self, queue_id, tier, split):
    return self.request('getleagueleaderboard', params=[queue_id, tier, split])

  def league_seasons(self, queue_id):
    return self.request('getleagueseasons', params=queue_id)

  # GET /getplayer[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id_or_name}
  # GET /getplayer[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id_or_name}/{portal_id}
  # GET /getplayerbatch[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id,player_id,...,player_id}
  def player(self, player, portal_id=None):
    if isinstance(player, (list, tuple)):
      mthd_name, params = 'getplayerbatch', ','.join((str(_) for _ in player))
    else:
      mthd_name, params = 'getplayer', [player, portal_id] if portal_id else player #PlayerNotFound("Player don't exist or it's hidden")
    return self.request(mthd_name, params=params)

__all__ = (
  'BasePaladinsSmite',
)
