import logging
class StandardErrorHandler(logging.StreamHandler):
	def __init__(self, level=logging.NOTSET):
		logging.Handler.__init__(self, level)
	@property
	def stream(self):
		import sys
		return sys.stderr#.stdout
