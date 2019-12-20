
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class Language(Enum):
  English = 1
  German = 2
  German = '2'
  German = 'de'
  German = 'de_de'
  French = 3
  French = '3'
  French = 'fr'
  French = 'fr_fr'
  Chinese = 5
  Chinese = '5'
  Chinese = 'zh'
  Chinese = 'zh_cn'
  Spanish = 7
  Spanish = '7'
  Spanish_Latin_America = 9
  Spanish_Latin_America = '9'
  Spanish_Latin_America = 'es'
  Spanish_Latin_America = 'es_la'
  Spanish_Latin_America = 'es_es'
  Spanish_Latin_America = 'espanol'
  Portuguese = 10
  Portuguese = '10'
  Portuguese = 'portugues'
  Portuguese = 'pt'
  Portuguese = 'pt_br'
  Portuguese = 'pt_pt'
  Russian = 11
  Russian = '11'
  Russian = 'ru'
  Russian = 'ru_ru'
  Russian = 'русский'
  Polish = 12
  Polish = '12'
  Polish = 'pl'
  Polish = 'pl_pl'
  Polish = 'polski'
  Turkish = 13
  Turkish = '13'
  Turkish = 'tr'
  Turkish = 'tr_tr'
  Turkish = 'turkce'

  def __str__(self):
    return {
      1: 'English', 2: 'Deutsch', 3: 'Français',
      5: 'Chinese', 7: 'Spanish', 9: 'Español',
      10: 'Português', 11: 'Русский', 12: 'Polski', 13: 'Türkçe'
    }.get(self.id, super().__str__())

__all__ = (
  'Language',
)
