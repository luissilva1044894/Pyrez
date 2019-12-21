
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class Language(Enum):
  ENGLISH = 1
  GERMAN = 2
  GERMAN = 'de'
  GERMAN = 'de_de'
  GERMAN = 'ger'
  FRENCH = 3
  FRENCH = 'fr'
  FRENCH = 'fr_fr'
  FRENCH = 'fre'
  CHINESE = 5
  CHINESE = 'chi'
  CHINESE = 'zh'
  CHINESE = 'zh_cn'
  SPANISH = 7
  SPANISH_LATIN_AMERICA = 9
  SPANISH_LATIN_AMERICA = 'es'
  SPANISH_LATIN_AMERICA = 'es_la'
  SPANISH_LATIN_AMERICA = 'es_es'
  SPANISH_LATIN_AMERICA = 'espanol'
  SPANISH_LATIN_AMERICA = 'spa'
  SPANISH_LATIN_AMERICA = 'spanish'
  PORTUGUESE = 10
  PORTUGUESE = 'por'
  PORTUGUESE = 'portugues'
  PORTUGUESE = 'pt'
  PORTUGUESE = 'pt_br'
  PORTUGUESE = 'pt_pt'
  RUSSIAN = 11
  RUSSIAN = 'ru'
  RUSSIAN = 'ru_ru'
  RUSSIAN = 'rus'
  RUSSIAN = 'русский'
  POLISH = 12
  POLISH = 'pl'
  POLISH = 'pl_pl'
  POLISH = 'pol'
  POLISH = 'polski'
  TURKISH = 13
  TURKISH = 'tr'
  TURKISH = 'tr_tr'
  TURKISH = 'tur'
  TURKISH = 'turkce'

  def __str__(self):
    return {Language.GERMAN:'Deutsch', Language.FRENCH:'Français', Language.CHINESE:'Chinese', Language.SPANISH:'Spanish (Outdated)', Language.SPANISH_LATIN_AMERICA:'Español', Language.PORTUGUESE:'Português', Language.RUSSIAN:'Русский', Language.POLISH:'Polski', Language.TURKISH:'Türkçe'}.get(self, 'English')#super().__str__()

  @property
  def emoji(self):
    return {Language.GERMAN:'🇩🇪', Language.FRENCH:'🇫🇷', Language.CHINESE:'🇨🇳', Language.SPANISH:'🇪🇸', Language.SPANISH_LATIN_AMERICA:'🇦🇷', Language.PORTUGUESE:'🇧🇷', Language.RUSSIAN:'🇷🇺', Language.POLISH:'🇵🇱', Language.TURKISH:'🇹🇷'}.get(self, '🇺🇸')

__all__ = (
  'Language',
)
