#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .command_line import check_python
check_python((3, 5))

from .api import *
from .enumerations import *
from .exceptions import *
from .models import *
from .__version__ import *

__all__ = (
	"api",
	"enumerations",
	"exceptions",
	"models",
	"__version__",
)

import logging
try:
	from logging import NullHandler
except ImportError:
	class NullHandler(logging.Handler):
		def emit(self, record):
			pass
logging.getLogger(__name__).addHandler(NullHandler())

#
# _____
#|  __ \
#| |__) |   _ _ __ ___ ____
#|  ___/ | | | '__/ _ \_  /
#| |   | |_| | | |  __// /
#|_|    \__, |_|  \___/___|
#        __/ |
#       |___/
