
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Named
class Language(Named):
  English = 1 #en_US
  German = 2, 'Deutsch' #de_DE
  French = 3, 'Français' #fr_FR
  Chinese = 5 #zh_CN
  Spanish = 7 #es_ES
  Spanish_Latin_America = 9, 'Español' #es_LA
  Portuguese = 10, 'Português do Brasil' #pt_BR
  Russian = 11, 'Русский' #ru_RU
  Polish = 12, 'Polski' #pl_PL
  Turkish = 13, 'Türkçe' #tr_TR

__all__ = (
  'Language',
)
