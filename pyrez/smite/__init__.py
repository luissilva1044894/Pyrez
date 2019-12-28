
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ..base.paladins_smite import PaladinsSmite
class Smite(PaladinsSmite):
  # GET /getgodrecommendeditems[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{god_id}/{language_code}
  def god_recommended_items(self, god_id, language=None, **kw):
    from ..enums.language import Language
    from ..enums.god import God
    return self.request('getgodrecommendeditems', params=[God(god_id) or god_id, Language(language)], **kw)

  # GET /getmotd[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}
  def motd(self, **kw):
    from .match.motd import MOTD
    return self.request('getmotd', cls=kw.pop('cls', MOTD), **kw)

  # GET /getteamdetails[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{clan_id}
  def team_info(self, clan_id, **kw):
    from .team.info import Info
    return self.request('getteamdetails', params=clan_id, cls=kw.pop('cls', Info), **kw)

  # GET /getteamplayers[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{clan_id}
  def team_players(self, clan_id, **kw):
    from .team.player import Player
    return self.request('getteamplayers', params=clan_id, cls=kw.pop('cls', Player), **kw)

  # GET /gettopmatches[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}
  def top_matches(self, **kw):
    from .match.top import Top
    return self.request('gettopmatches', cls=kw.pop('cls', Top), **kw)

  # GET /searchteams[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{search_team}
  def search_teams(self, search_team, **kw):
    from .team import Team
    return self.request('searchteams', params=search_team, cls=kw.pop('cls', Team), **kw)

__all__ = (
  'Smite',
)
