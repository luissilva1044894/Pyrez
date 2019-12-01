
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from datetime import datetime
__author__ = 'Luis (Lugg) Gustavo'
__author_email__ = 'the.nonsocial@gmail.com'
__copyright__ = f'2018-{datetime.utcnow().year}, {__author__}'
__description__ = 'An open-source wrapper for Hi-Rez Studios API (Paladins, Realm Royale, and Smite), written in Python.'
__license__ = 'MIT'
__package_name__ = 'pyrez'
__url__ = f'https://github.com/luissilva1044894/{__package_name__}'#f'https://{__package_name__}.readthedocs.io/en/stable'
VERSION = (1, 2, 0, 0, 'dev0')
#__version__ = '.'.join(str(v) for v in VERSION) + 'dev0'
__version__ = '.'.join(map(str, VERSION[:4])) + (VERSION[4] if VERSION[4] else '')
__title__ = f'{__package_name__.capitalize()}/{__version__}'
version = __version__

__release_level = [ 'alpha', 'beta', 'candidate', 'final' ]

from collections import namedtuple
version_info = namedtuple('VersionInfo', 'major minor micro releaselevel serial')(major=VERSION[0], minor=VERSION[1], micro=VERSION[2], releaselevel=__release_level[2], serial=0)

__all__ = (
  '__title__',
  '__description__',
  '__url__',
  '__version__',
  '__author__',
  #'__author_email__',
  '__license__',
  '__copyright__',
  '__package_name__',
  'version_info',
)

authors = (
  (__author__, __author_email__),
)
__authors__ = ', '.join('{} <{}>'.format(*_) for _ in authors)
