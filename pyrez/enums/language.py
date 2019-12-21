
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
    return {
      1: 'English', 2: 'Deutsch', 3: 'Français',
      5: 'Chinese', 7: 'Spanish (Outdated)', 9: 'Español',
      10: 'Português', 11: 'Русский', 12: 'Polski', 13: 'Türkçe'
    }.get(self.id, super().__str__())

  @property
  def emoji(self):
    return { 2: '🇩🇪', 3: '🇫🇷', 5: '🇨🇳', 7: '🇪🇸', 9: '🇦🇷', 10: '🇧🇷', 11: '🇷🇺', 12: '🇵🇱', 13: '🇹🇷' }.get(self.id, '🇺🇸')

__all__ = (
  'Language',
)
