
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class Language(Enum):
  English = 1
  German = 2
  French = 3
  Chinese = 5
  Spanish = 7
  Spanish_Latin_America = 9
  Portuguese = 10
  Russian = 11
  Polish = 12
  Turkish = 13

__all__ = (
  'Language',
)
