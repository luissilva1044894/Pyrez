
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from ..base.paladins_smite import PaladinsSmite
class Smite(PaladinsSmite):
  # GET /getgodrecommendeditems[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{god_id}/{language_code}
  def god_recommended_items(self, god_id, language=None, **kw):
    from ..enums.language import Language
    return self.request('getgodrecommendeditems', params=[god_id, Language(language)], **kw)

  # GET /getmotd[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}
  def motd(self, **kw):
    return self.request('getmotd', **kw)

  # GET /getteamdetails[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{clan_id}
  def team_details(self, clan_id, **kw):
    return self.request('getteamdetails', params=clan_id, **kw)

  # GET /getteamplayers[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{clan_id}
  def team_players(self, clan_id, **kw):
    return self.request('getteamplayers', params=clan_id, **kw)

  # GET /gettopmatches[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}
  def top_matches(self, **kw):
    return self.request('gettopmatches', **kw)

  # GET /searchteams[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{search_team}
  def search_teams(self, search_team, **kw):
    return self.request('searchteams', params=search_team, **kw)

__all__ = (
  'Smite',
)
