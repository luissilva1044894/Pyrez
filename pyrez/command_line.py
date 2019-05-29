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
	entries.append("- Python v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}".format(sys.version_info))
	entries.append("- {0} v{1.major}.{1.minor}.{1.micro}-{1.releaselevel}".format(__package_name__.capitalize(), version_info))

	entries.append("- requests v{0.__version__}".format(requests))
	entries.append("- System info: {0.system} {0.release} {0.version}".format(platform.uname()))
	print("\n".join(entries))

def parse_cli_flags(args):
	"""Command line application for Pyrez package"""
	from .__version__ import __package_name__, __version__
	from argparse import ArgumentParser

	parser = ArgumentParser(prog=__package_name__.capitalize(), usage="%(prog)s [arguments]", description=parse_cli_flags.__doc__)
	parser.add_argument("--info", "-i", "-I", dest="info", action="store_true", help="Show %(prog)s and dependencies versions")
	parser.add_argument('--version', action='version', version="%(prog)s {}".format(__version__), help="Show %(prog)s's current version")
	parser.set_defaults(func=show_version)

	#return parser.parse_args(args)
	cli_flags = parser.parse_args(args)
	if cli_flags.info:
		show_version()

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
