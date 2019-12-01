
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

def create_task(func, loop):
	import asyncio
	if hasattr(loop, 'create_task'):
		return loop.create_task(func)
	return asyncio.ensure_future(func, loop=loop)

def make_call(func, _is_async, loop=None):
	if _is_async:
		try: # not loop.is_running
			return loop.run_until_complete(create_task(func, loop))
		except RuntimeError:
			return create_task(func, loop)
	return func

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
