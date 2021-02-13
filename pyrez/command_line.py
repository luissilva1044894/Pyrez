#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check_python(min_version=(3, 5)):
	import sys
	from .__version__ import __package_name__
	from datetime import datetime

	if sys.version_info[:2] < min_version and datetime.utcnow().year >= 2020:
		print("ERROR: {} requires at least Python {} to run.".format(__package_name__.capitalize(), '.'.join(map(str, (min_version)))))
		sys.exit(1)

def show_version():
	from .__version__ import __package_name__, version_info

	import sys
	import platform
	import requests
	entries = []
	entries.append('- Python v{py.major}.{py.minor}.{py.micro}-{py.releaselevel}'.format(py=sys.version_info))
	entries.append('- {pyrez} v{ver.major}.{ver.minor}.{ver.micro}-{ver.releaselevel}'.format(pyrez=__package_name__.capitalize(), ver=version_info))
	entries.append('- {requests.__name__} v{requests.__version__}'.format(requests=requests))
	try:
		import httpx
	except ImportError:
		pass
	else:
		entries.append('- {httpx.__name__} v{httpx.__version__}'.format(httpx=httpx))
	entries.append('- System info: {platform.system} {platform.release} {platform.version}'.format(platform=platform.uname()))
	print("\n".join(entries))

def test_logger():# https://github.com/nficano/pytube/issues/163
	from . import logger
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

	parser = ArgumentParser(prog=__package_name__.capitalize(), usage="%(prog)s [arguments]", description=parse_cli_flags.__doc__)
	parser.add_argument("--info", "-i", "-I", dest="info", action="store_true", help="Show %(prog)s and dependencies versions")
	parser.add_argument('--logs', '-l', '-L', dest='logs', action='store_true')
	parser.add_argument('--version', action='version', version="Using %(prog)s {}".format(__version__), help="Show %(prog)s's current version")
	parser.set_defaults(func=show_version)

	#return parser.parse_args(args)
	cli_flags = parser.parse_args(args)
	if cli_flags.info:
		show_version()
	elif cli_flags.logs:
		test_logger()

def main():
	import sys

	parse_cli_flags(sys.argv[1:])
	sys.exit(0)

if __name__ == "__main__":
	import sys

	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
