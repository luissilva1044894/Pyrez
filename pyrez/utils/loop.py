
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

import asyncio
import sys

def get_running_loop(loop=None, force_fresh=False):
  #if not force_fresh and loop and not loop.is_closed() or loop.is_running():
  #  return loop
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

def create_task(func, loop):
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

def run(*args):
  def get_future(args):
    coros = list(filter(inspect.iscoroutine, args))
    if coros and isinstance(coros, (tuple, list)):
      if len(coros) > 1:
        return asyncio.gather(*coros)
      return coros[0]
    return coros
  loop = get_running_loop()
  loop.run_until_complete(get_future(args))

def executor_function(sync_function):
  @functools.wraps(sync_function)
  async def sync_wrapper(*args, **kw):
    loop = get_running_loop()
    return await loop.run_in_executor(None, functools.partial(sync_function, *args, **kw))
  return sync_wrapper

def executor(function):
  @wraps(function)
  def decorator(loop, *args, **kw):
    return loop.run_in_executor(None, function, *args, **kw)
  return decorator
