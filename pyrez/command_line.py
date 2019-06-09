#!/usr/bin/env python
# -*- coding: utf-8 -*-

#try:
#	input = raw_input  # Python 2
#except NameError:
#	pass

def check_python(min_version=(3, 5), min_year=2020, auto_exit=True):
	import sys
	from .__version__ import __package_name__

	ver = sys.version_info[:2] < min_version and datetime.utcnow().year >= min_year
	if ver:#auto_exit and ver:
		print('ERROR: {} requires at least Python {} to run.'.format(__package_name__.capitalize(), '.'.join(map(str, (min_version)))))
		sys.exit(1)
	return ver

def show_version():
	from .__version__ import __package_name__, version_info

	import sys
	import platform
	import requests
	entries = []
	entries.append('- Python v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}'.format(sys.version_info))
	entries.append('- {0} v{1.major}.{1.minor}.{1.micro}-{1.releaselevel}'.format(__package_name__.capitalize(), version_info))

	#import aiohttp
	#entries.append('- aiohttp v{0.__version__}'.format(aiohttp))
	entries.append('- requests v{0.__version__}'.format(requests))
	entries.append('- System info: {0.system} {0.release} {0.version}'.format(platform.uname()))
	print("\n".join(entries))

def test_logger():# https://github.com/nficano/pytube/issues/163
	from .logging import create_logger
	logger = create_logger()#https://docs.python.org/3/library/logging.html
	logger.critical('This is critical level')
	logger.debug('This is debug level')
	logger.error('This is error level')
	logger.info('This is info level')
	logger.success('This is success level')
	logger.warning('This is warning level')

def parse_cli_flags(args):
	"""Command line application for Pyrez package"""
	from .__version__ import __package_name__, __version__
	from argparse import ArgumentParser

	parser = ArgumentParser(prog=__package_name__.capitalize(), usage='%(prog)s [arguments]', description=parse_cli_flags.__doc__)
	parser.add_argument('--info', '-i', '-I', dest='info', action='store_true', help="Show %(prog)s and dependencies versions")
	parser.add_argument('--logs', '-l', '-L', dest='logs', action='store_true')
	parser.add_argument('--version', '-V', '-v', action='version', version="Using %(prog)s {}".format(__version__), help="Show %(prog)s's current version")

	#https://docs.python.org/2/howto/argparse.html
	#https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser
	#parser.add_argument('--devid', action='store', dest='devid', default=0000, required=False, type=int)#, help=''
	#https://pythonhelp.wordpress.com/2011/11/20/tratando-argumentos-com-argparse/
	#https://docs.python.org/3/library/argparse.html#module-argparse
	#https://docs.python.org/3/howto/argparse.html
	parser.set_defaults(func=show_version)

	cli_flags = parser.parse_args(args)#return parser.parse_args(args)
	if cli_flags.info:
		show_version()
	elif cli_flags.logs:
		test_logger()

def main():
	import sys

	parse_cli_flags(sys.argv[1:])
	sys.exit(0)

if __name__ == '__main__':
	import sys

	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
