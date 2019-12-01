
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

def get(force_fresh=False):
	import asyncio
	import sys
	try:
		import uvloop
	except ImportError:
		asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
	else:
		asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
	if sys.platform == 'win32':
		if not force_fresh and isinstance(asyncio.get_event_loop(), asyncio.ProactorEventLoop) and not asyncio.get_event_loop().is_closed():
			return asyncio.get_event_loop()
		return asyncio.ProactorEventLoop()
	if force_fresh or asyncio.get_event_loop().is_closed():
		return asyncio.new_event_loop()
	return asyncio.get_event_loop()
