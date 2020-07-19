
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
  CHINESE = 'cn'
  CHINESE = 'zh'
  CHINESE = 'zh_cn'
  SPANISH = 7
  SPANISH_LATIN_AMERICA = 9
  SPANISH_LATIN_AMERICA = 'es'
  SPANISH_LATIN_AMERICA = 'es_es'
  SPANISH_LATIN_AMERICA = 'es_la'
  SPANISH_LATIN_AMERICA = 'es_mx'
  SPANISH_LATIN_AMERICA = 'espanol'
  SPANISH_LATIN_AMERICA = 'spa'
  SPANISH_LATIN_AMERICA = 'spanish'
  PORTUGUESE = 10
  PORTUGUESE = 'br'
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

  @property
  def lang_code(self):
    return {2: 'de_DE', 3: 'fr_FR', 5: 'zh_CN', 7: 'es_LA', 9: 'es_LA', 10: 'pt_BR', 11: 'ru_RU', 12: 'pl_PL', 13: 'tr_tr'}.get(int(self), 'en_US')

  def __str__(self):
    return {Language.GERMAN:'Deutsch', Language.FRENCH:'Français', Language.CHINESE:'Chinese', Language.SPANISH:'Spanish (Outdated)', Language.SPANISH_LATIN_AMERICA:'Español', Language.PORTUGUESE:'Português', Language.RUSSIAN:'Русский', Language.POLISH:'Polski', Language.TURKISH:'Türkçe'}.get(self, super().__str__())

  @property
  def emoji(self):
    return {Language.GERMAN:'🇩🇪', Language.FRENCH:'🇫🇷', Language.CHINESE:'🇨🇳', Language.SPANISH:'🇪🇸', Language.SPANISH_LATIN_AMERICA:'🇦🇷', Language.PORTUGUESE:'🇧🇷', Language.RUSSIAN:'🇷🇺', Language.POLISH:'🇵🇱', Language.TURKISH:'🇹🇷'}.get(self, '🇺🇸')

__all__ = (
  'Language',
)
