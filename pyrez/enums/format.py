
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class Format(Enum):
  JSON = 'json'
  XML = 'xml'
  ATOM = 'atom'
  RSS = 'rss'

__all__ = (
  'Format',
)
