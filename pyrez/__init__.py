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

from .logging import create_logger
logger = create_logger(__package_name__)

#
# _____
#|  __ \
#| |__) |   _ _ __ ___ ____
#|  ___/ | | | '__/ _ \_  /
#| |   | |_| | | |  __// /
#|_|    \__, |_|  \___/___|
#        __/ |
#       |___/
