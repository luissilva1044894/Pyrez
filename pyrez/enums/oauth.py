
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

from . import Enum
class OAuth(Enum):
  DISCORD = 'discord'
  FACEBOOK = 'facebook'
  GOOGLE = 'google'
  HIREZ = 'hirez'
  NINTENDO_SWITCH = 'switch'
  PLAY_STATION = 'playstation'
  STEAM = 'steam'
  XBOX = 'xbox'

  def _get(self, api=None, param=None):
    from .endpoint import Endpoint
    return f'{api or Endpoint.HIREZ}/oauth/{"" if self == OAuth.HIREZ else "out/"}{self.value}?{"redirect_uri" if self == OAuth.HIREZ else "url"}={param or ""}'
  def __str__(self):
    return self._get()

__all__ = (
  'OAuth',
)
