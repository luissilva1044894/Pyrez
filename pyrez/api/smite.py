
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from .base_paladins_smite import BasePaladinsSmite
class Smite(BasePaladinsSmite):
  # GET /getgodrecommendeditems[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{god_id}/{language_code}
  def god_recommended_items(self, god_id, language=None):
    from ..enums.language import Language
    return self.request('getgodrecommendeditems', params=[god_id, language or Language.English])

  # GET /getmotd[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}
  def motd(self):
    return self.request('getmotd')

  # GET /getteamdetails[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{clan_id}
  def team_details(self, clan_id):
    return self.request('getteamdetails', params=clan_id)

  # GET /getteamplayers[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{clan_id}
  def team_players(self, clan_id):
    return self.request('getteamplayers', params=clan_id)

  # GET /gettopmatches[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}
  def top_matches(self):
    return self.request('gettopmatches')

  # GET /searchteams[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{search_team}
  def search_teams(self, search_team):
    return self.request('searchteams', params=search_team)

__all__ = (
  'Smite',
)
