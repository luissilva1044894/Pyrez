#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
__author__ = "Luis (Lugg) Gustavo"
__author_email__ = "the.nonsocial@gmail.com"
__copyright__ = "2018-{}, {}".format(datetime.utcnow().year, __author__)
__build__ = 0x0100065
__description__ = "An open-source wrapper for Hi-Rez Studios API (Paladins, Realm Royale, and Smite), written in Python."
__license__ = "MIT"
__package_name__ = "pyrez"
__url__ = "https://{package_name}.readthedocs.io/en/stable".format(package_name=__package_name__)
VERSION = (1, 0, 6)
__version__ = "1.0.6"#'.'.join(map(str, VERSION))
__title__ = "{}-{}".format(__package_name__.capitalize(), __version__)
version = __version__

from collections import namedtuple
version_info = namedtuple("VersionInfo", "major minor micro releaselevel serial")(major=VERSION[0], minor=VERSION[1], micro=VERSION[2], releaselevel="final", serial=0)

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
