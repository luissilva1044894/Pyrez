#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
__author__ = "Luis (Lugg) Gustavo"
__author_email__ = "the.nonsocial@gmail.com"
__copyright__ = "2018-{}, {}".format(datetime.utcnow().year, __author__)
__build__ = 0x02000000
__description__ = "An open-source wrapper for Hi-Rez Studios API (Paladins, Realm Royale, and Smite), written in Python."
__license__ = "MIT"
__package_name__ = "pyrez"
__url__ = "https://github.com/luissilva1044894/{package_name}".format(package_name=__package_name__)#"https://{package_name}.readthedocs.io/en/stable".format(package_name=__package_name__)
VERSION = (1, 2, 0, 0)
__version__ = '.'.join(str(v) for v in VERSION) + 'dev0'
__title__ = "{}/{}".format(__package_name__.capitalize(), __version__)
version = __version__

__release_level = [ 'alpha', 'beta', 'release candidate', 'final' ]

from collections import namedtuple
version_info = namedtuple("VersionInfo", "major minor micro releaselevel serial")(major=VERSION[0], minor=VERSION[1], micro=VERSION[2], releaselevel=__release_level[2], serial=0)

__all__ = (
    "__title__",
    "__description__",
    "__url__",
    "__version__",
    "__author__",
    #"__author_email__",
    "__license__",
    "__copyright__",
    "__package_name__",
    "version_info",
)

#author_info = ( ('Luis (Lugg) Gustavo', 'the.nonsocial@gmail.com'), )
#__author__ = ", ".join("{} <{}>".format(*info) for info in author_info)
