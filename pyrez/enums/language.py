
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class Language(Enum):
  ENGLISH = 1
  GERMAN = 2
  GERMAN = '2'
  GERMAN = 'de'
  GERMAN = 'de_de'
  FRENCH = 3
  FRENCH = '3'
  FRENCH = 'fr'
  FRENCH = 'fr_fr'
  CHINESE = 5
  CHINESE = '5'
  CHINESE = 'zh'
  CHINESE = 'zh_cn'
  SPANISH = 7
  SPANISH = '7'
  SPANISH_LATIN_AMERICA = 9
  SPANISH_LATIN_AMERICA = '9'
  SPANISH_LATIN_AMERICA = 'es'
  SPANISH_LATIN_AMERICA = 'es_la'
  SPANISH_LATIN_AMERICA = 'es_es'
  SPANISH_LATIN_AMERICA = 'espanol'
  PORTUGUESE = 10
  PORTUGUESE = '10'
  PORTUGUESE = 'portugues'
  PORTUGUESE = 'pt'
  PORTUGUESE = 'pt_br'
  PORTUGUESE = 'pt_pt'
  RUSSIAN = 11
  RUSSIAN = '11'
  RUSSIAN = 'ru'
  RUSSIAN = 'ru_ru'
  RUSSIAN = 'русский'
  POLISH = 12
  POLISH = '12'
  POLISH = 'pl'
  POLISH = 'pl_pl'
  POLISH = 'polski'
  TURKISH = 13
  TURKISH = '13'
  TURKISH = 'tr'
  TURKISH = 'tr_tr'
  TURKISH = 'turkce'

  def __str__(self):
    return {
      1: 'English', 2: 'Deutsch', 3: 'Français',
      5: 'Chinese', 7: 'Spanish', 9: 'Español',
      10: 'Português', 11: 'Русский', 12: 'Polski', 13: 'Türkçe'
    }.get(self.id, super().__str__())

__all__ = (
  'Language',
)
