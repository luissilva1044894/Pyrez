# -*- coding: utf-8 -*-

"""
 _____
|  __ \
| |__) |   _ _ __ ___ ____
|  ___/ | | | '__/ _ \_  /
| |   | |_| | | |  __// /
|_|    \__, |_|  \___/___|
        __/ |
       |___/
"""

import sys
from datetime import datetime
if sys.version_info[:2] < (3, 4) and datetime.utcnow().year >= 2020:
    raise RuntimeError("Unsupported Python version - Pyrez requires Python 3.4+")

from .api import *
from .enumerations import *
from .exceptions import *
from .models import *

__all__ = (
	"api",
	"enumerations",
	"exceptions",
	"models",
)

import logging
try:
	from logging import NullHandler
except ImportError:
	class NullHandler(logging.Handler):
		def emit(self, record):
			pass
logging.getLogger(__name__).addHandler(NullHandler())
