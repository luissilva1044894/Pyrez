
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

import pyrez

fake_dev_id=1004
fake_auth_key='23DF3C7E9BD14D84BF892AD206B6755C'

async def standard():
  paladins = pyrez.api.Paladins(fake_dev_id , fake_auth_key, is_async=True)
  print(await paladins.data_used())
  await paladins.close()

async def context_manager():
  """Async context manager"""
  async with pyrez.api.Smite.Async(fake_dev_id, fake_auth_key) as smite:
    print(await smite.data_used())

async def a_main():
  await standard()
  await context_manager()

def main():
  import sys
  import asyncio

  if sys.implementation.name == 'cpython':
    try:
      import uvloop
    except ImportError:
      pass
    else:
      asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
  loop = asyncio.get_event_loop()
  #hasattr(asyncio, 'run')
  try:
    # Python 3.7+
    asyncio.run(a_main())
  except (AttributeError):
    loop.run_until_complete(a_main())
  except KeyboardInterrupt:
    pass
  finally:
    loop.close()

if __name__ == '__main__':
  main()
