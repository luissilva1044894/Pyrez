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

class StandardErrorHandler(logging.StreamHandler):
	def __init__(self, level=logging.NOTSET):
		logging.Handler.__init__(self, level)
	@property
	def stream(self):
		return sys.stderr#.stdout

class ColorizingStreamHandler(StandardErrorHandler):
	# color names to indices
	color_map = { 'black': 0, 'red': 1, 'green': 2, 'yellow': 3, 'blue': 4, 'magenta': 5, 'cyan': 6, 'white': 7, }

	#levels to (background, foreground, bold/intense)
	level_map = {
		logging.DEBUG: (None, 'blue', WINDOWS),
		logging.INFO: (None, 'white', False),
		logging.WARNING: (None, 'yellow', WINDOWS),
		logging.ERROR: (None, 'red', WINDOWS),
		logging.CRITICAL: ('red', 'white', True),
	}
	csi, reset = '\x1b[', '\x1b[0m'
	@property
	def is_tty(self):
		isatty = getattr(self.stream, 'isatty', None)
		return isatty and isatty()
	def emit(self, record):
		try:
			message = self.format(record)
			stream = self.stream
			if not self.is_tty:
				stream.write(message)
			else:
				self.output_colorized(message)
			stream.write(getattr(self, 'terminator', '\n'))
			self.flush()
		except (KeyboardInterrupt, SystemExit):
			pass#raise
		except Exception:
			self.handleError(record)
	if not WINDOWS:
		def output_colorized(self, message):
			self.stream.write(message)
	else:
		from colorama import init
		init(convert=True)

		def output_colorized(self, message):
			import ctypes #Windows 10 ANSI support
			ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11), 7)
			ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-12), 7)
			self.stream.write(message)
		"""#http://plumberjack.blogspot.com/2010/12/colorizing-logging-output-in-terminals.html
		import re
		ansi_esc = re.compile(r'\x1b\[((?:\d+)(?:;(?:\d+))*)m')

		nt_color_map = {
			0: 0x00,    # black
			1: 0x04,    # red
			2: 0x02,    # green
			3: 0x06,    # yellow
			4: 0x01,    # blue
			5: 0x05,    # magenta
			6: 0x03,    # cyan
			7: 0x07,    # white
		}
		def output_colorized(self, message):
			import ctypes
			parts = self.ansi_esc.split(message)
			write = self.stream.write
			h = None
			fd = getattr(self.stream, 'fileno', None)
			if fd is not None:
				fd = fd()
				if fd in (1, 2): # stdout or stderr
					h = ctypes.windll.kernel32.GetStdHandle(-10 - fd)
			while parts:
				text = parts.pop(0)
				if text:
					write(text)
				if parts:
					params = parts.pop(0)
					if h is not None:
						params = [int(p) for p in params.split(';')]
						color = 0
						for p in params:
							if 40 <= p <= 47:
								color |= self.nt_color_map[p - 40] << 4
							elif 30 <= p <= 37:
								color |= self.nt_color_map[p - 30]
							elif p == 1:
								color |= 0x08 # foreground intensity on
							elif p == 0: # reset to default color
								color = 0x07
							#else: pass # error condition ignored
						ctypes.windll.kernel32.SetConsoleTextAttribute(h, color)
		"""
	def colorize(self, message, record):
		if record.levelno in self.level_map:
			bg, fg, bold = self.level_map[record.levelno]
			params = []
			if bg in self.color_map:
				params.append(str(self.color_map[bg] + 40))
			if fg in self.color_map:
				params.append(str(self.color_map[fg] + 30))
			if bold:
				params.append('1')
			if params:
				message = ''.join((self.csi, ';'.join(params), 'm', message, self.reset))
		return message
	def format(self, record):
		message = logging.StreamHandler.format(self, record)
		if self.is_tty:# Don't colorize any traceback
			parts = message.split('\n', 1)
			#parts[0] = self.colorize(parts[0], record)#output_colorized()
			message = '\n'.join(parts)
		return message
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
	stream_handler = ColorizingStreamHandler() #logging.StreamHandler(sys.stdout)
	stream_handler.setFormatter(logging.Formatter(formatter_console, datefmt=datefmt))
	if rewrite:
		stream_handler.terminator = ''

	try:
		LOG_FILE_PATH = os.path.join(log_folder_path or os.getcwd(), filename or "LOG_FILE.log")# create file handler
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
