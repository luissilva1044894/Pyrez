# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reference:
	https://github.com/ischouten/logquicky/blob/master/logquicky/logquicky.py
	https://gist.github.com/vsajip/758430
	https://github.com/laysakura/rainbow_logging_handler/
	https://gist.github.com/brainsik/1238935
	https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
	plumberjack.blogspot.com/2010/12/colorizing-logging-output-in-terminals.html
"""
import logging
import sys
import os

# Windows requires special handling and the first step is detecting it :-).
# Optional external dependency (only needed on Windows).
WINDOWS = sys.platform.startswith('win') or os.name == 'nt'


def get_logger(name=None):
	return logging.getLogger(name or __name__)

def add_handler(logger, handler=None):
	try:
		from logging import NullHandler
	except ImportError:
		class NullHandler(logging.Handler):
			def emit(self, record):
				pass
	logger.addHandler(handler or NullHandler())
	return logger

def create_logger(name=None, rewrite=False, level=None, formatter_console='%(asctime)s %(name)s [%(levelname)s] %(message)s',
				formatter_file='%(asctime)s %(name)s [%(levelname)s in %(module)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
				log_folder_path=None, filename=None):
	"""Create a configured instance of logger.

	Parameters
	----------
	level
		Describe the severity level of the logs to handle.
	"""
	from logging.handlers import RotatingFileHandler

	#level="INFO"
	logger = get_logger(name)

	# Some colors to make the next part more readable
	colors = {
		'blue': '\033[0;34m',
		'green': '\033[0;32m',
		'purple': '\033[0;35m',
		'red': '\033[0;31m',
		'bold_red': '\033[1;31m',
		'reset': '\033[0m',
		'clear': '\033[2J',
	}
	# adding a new logging level
	logging.SUCCESS = 15 # as ALL (NOTSET) = 0, DEBUG = 10, INFO = 20, WARN (WARNING) = 30, ERROR = 40, FATAL = CRITICAL, CRITICAL = 50

	# Configure new configuration for "levelname" (add colors)
	logging.addLevelName(logging.DEBUG, '{blue}DEBUG{reset}'.format(blue=colors['blue'], reset=colors['reset']))
	logging.addLevelName(logging.INFO, '{green}INFO{reset}'.format(green=colors['green'], reset=colors['reset']))
	logging.addLevelName(logging.WARN, '{purple}WARN{reset}'.format(purple=colors['purple'], reset=colors['reset']))
	logging.addLevelName(logging.ERROR, '{red}ERROR{reset}'.format(red=colors['red'], reset=colors['reset']))
	logging.addLevelName(logging.CRITICAL, '{bold_red}CRITICAL{reset}'.format(bold_red=colors['bold_red'], reset=colors['reset']))
	logging.addLevelName(logging.SUCCESS, '{green}SUCCESS{reset}'.format(green=colors['green'], reset=colors['reset']))

	logger.success = lambda msg, *args: logger._log(logging.SUCCESS, msg, args)

	# Configure the console handler/ STDOUT
	from .colorizing_stream_handler import ColorizingStreamHandler
	stream_handler = ColorizingStreamHandler() #logging.StreamHandler(sys.stdout)
	stream_handler.setFormatter(logging.Formatter(formatter_console, datefmt=datefmt))
	if rewrite:
		stream_handler.terminator = ''

	try:
		from ..__version__ import __package_name__
		LOG_FILE_PATH = os.path.join(log_folder_path or os.getcwd(), filename or "{}_LOG_FILE.log".format(__package_name__.upper()))# create file handler
		file_handler = logging.FileHandler(LOG_FILE_PATH)#RotatingFileHandler(filename, mode='a', maxBytes=1000000, backupCount=2, encoding='utf-8')
		file_handler.setFormatter(logging.Formatter(formatter_file, datefmt=datefmt))
		logger = add_handler(logger, file_handler)
	except PermissionError:
		pass #logS.error(f"Cannot write log to file in '{file}' due to permission issues.")
	# Set the final level
	logger.setLevel(level or logging.DEBUG)

	return add_handler(logger, stream_handler)
#logger.debug('DEBUG')
#logger.info('INFO')
#logger.warning('WARNING')
#logger.error('ERROR')
#logger.critical('CRITICAL')
## https://github.com/nficano/pytube/issues/163
#logS = create_logger('logS', level="ERROR")
