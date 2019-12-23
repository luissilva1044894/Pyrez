
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ..base.paladins_smite import PaladinsSmite
class Paladins(PaladinsSmite):
  '''
  # GET /getchampions[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{language_code}
  def champions(self, language=Language.English):
    return self.request('getchampions', params=language or Language.English)
  # GET /getchampionleaderboard[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{god_id}/{queue_id}
  def champion_leaderboard(self, god_id, queue_id=QueuePaladins.Live_Competitive_Keyboard):
    return self.request('getchampionleaderboard', params=[god_id, queue_id or QueuePaladins.Live_Competitive_Keyboard])
  # GET /getchampionranks[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}
  def champion_ranks(self, player_id):
    return self.request('getchampionranks', params=player_id)
  # GET /getchampionskins[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{god_id}/{language_code}
  def champion_skins(self, god_id, language=Language.English):
    return self.request('getchampionskins', params=[god_id, language or Language.English])
  '''

  # GET /getchampioncards[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{god_id}/{language_code}
  def champion_cards(self, god_id, language=None):
    from ..enums.champion import Champion
    return self.request('getchampioncards', params=[Champion(god_id) or god_id, Language(language)])

  def player(self, player, portal_id=None, **kw):
    from .player import Player
    return super().player(player, portal_id=portal_id, cls=kw.pop('cls', Player), **kw)

  # GET /getplayerchampions[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}
  def player_champions(self, player_id, **kw):
    from .player.champion import Champion
    return self.request('getplayerchampions', params=player_id, cls=kw.pop('cls', Champion), **kw)

  # GET /getplayerloadouts[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}/{language_code}
  def player_loadouts(self, player_id, language=None, **kw):
    from ..enums.language import Language
    return self.request('getplayerloadouts', params=[player_id, Language(language)], **kw)

  # GET /getplayerbatchfrommatch[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{match_id}
  def players_from_match(self, match_id, **kw):
    return self.request('getplayerbatchfrommatch', params=match_id, **kw)

__all__ = (
  'Paladins',
)
