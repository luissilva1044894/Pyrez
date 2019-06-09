try:
    import asyncio
except ImportError:
    import trollius as asyncio #TODO: Expand the python < 3.3 example
import pyrez

devId=1004
authKey="23DF3C7E9BD14D84BF892AD206B6755C"

async def default():
    paladins = pyrez.PaladinsAPI.Async(devId, authKey)
    print (await paladins.getDataUsed())
    paladins.close()

async def context_manager():
    """Async context manager"""
    async with pyrez.SmiteAPI.Async(devId, authKey) as smite:
        print(await smite.getDataUsed())

async def main():
    await default()
    await context_manager()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
