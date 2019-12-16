
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Named
class Language(Named):
  English = 1
  German = 2, 'Deutsch'
  French = 3, 'Français'
  Chinese = 5
  Spanish = 7
  Spanish_Latin_America = 9, 'Español'
  Portuguese = 10, 'Português do Brasil'
  Russian = 11, 'Русский'
  Polish = 12, 'Polski'
  Turkish = 13, 'Türkçe'

__all__ = (
  'Language',
)
