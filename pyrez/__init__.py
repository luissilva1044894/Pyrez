
import sys
from datetime import datetime
if sys.version_info[:2] < (3, 4) and datetime.utcnow().year >= 2020:
    raise RuntimeError("Unsupported Python version")

__author__ = "Luis (Lugg) Gustavo"
__author_email__ = "luis.silva.1044894@gmail.com"
__copyright__ = "Copyright (c) 2018 Luís (Lugg) Gustavo"
__build__ = 0x000909
__description__ = "An open-source wrapper for Hi-Rez Studios' API (Paladins, Realm Royale, and Smite), written in Python"
__license__ = "MIT"
__package_name__ = "Pyrez"
__url__ = "https://discord.gg/XkydRPS"
__version__ = "0.9.9"
__title__ = "{}-{}".format(__package_name__, __version__)
version = __version__

from collections import namedtuple
version_info = namedtuple("VersionInfo", "major minor micro releaselevel serial")(major=0, minor=9, micro=9, releaselevel="beta", serial=0)
