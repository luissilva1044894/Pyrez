
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import API
class BasePaladinsSmite(API):
  def demo_details(self, match_id, **kw):
    return self.request('getdemodetails', params=match_id, **kw)
  def esports_league(self, **kw):
    return self.request('getesportsproleaguedetails', **kw)
  def gods(self, language=None, **kw):
    from ..enums.language import Language
    return self.request('getgods', params=Language(language), **kw)
  def god_leaderboard(self, god_id, language=None, **kw):
    from ..enums.language import Language
    return self.request('getgodleaderboard', params=[god_id, Language(language)], **kw)
  def god_ranks(self, player_id, god_id, **kw):
    return self.request('getgodranks', params=[player_id, god_id], **kw)
  # GET /getgodskins[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{godId}/{languageCode}
  def god_skins(self, god_id, language=None, **kw):
    from ..enums.language import Language
    return self.request('getgodskins', params=[god_id, Language(language)], **kw)
  # GET /getitems[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{languagecode}
  def items(self, language=None, **kw):
    from ..enums.language import Language
    return self.request('getitems', params=Language(language), **kw)

  # GET /getmatchhistory[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}
  def match_history(self, player_id, **kw):
    return self.request('getmatchhistory', params=player_id, **kw)

  def league_leaderboard(self, queue_id, tier, split, **kw):
    return self.request('getleagueleaderboard', params=[queue_id, tier, split], **kw)

  def league_seasons(self, queue_id, **kw):
    return self.request('getleagueseasons', params=queue_id, **kw)

  # GET /getplayer[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id_or_name}
  # GET /getplayer[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id_or_name}/{portal_id}
  # GET /getplayerbatch[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id,player_id,...,player_id}
  def player(self, player, portal_id=None, **kw):
    from ..models.player import Player
    from ..exceptions.player_not_found import PlayerNotFound
    if isinstance(player, (list, tuple)):
      mthd_name, params = 'getplayerbatch', ','.join((str(_) for _ in player))
    else:
      mthd_name, params = 'getplayer', [player, portal_id] if portal_id else player
    return self.request(mthd_name, params=params, cls=kw.pop('cls', Player), raises=PlayerNotFound("Player doesn't exist or it's hidden"), **kw)

__all__ = (
  'BasePaladinsSmite',
)
