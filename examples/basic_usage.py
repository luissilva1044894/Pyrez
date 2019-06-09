import pyrez

devId=1004
authKey='23DF3C7E9BD14D84BF892AD206B6755C'

async def standard_async():
    paladins = pyrez.PaladinsAPI.Async(devId, authKey)
    print(await paladins.getDataUsed())
    paladins.close()

async def context_manager():
    """Async context manager"""
    async with pyrez.SmiteAPI.Async(devId, authKey) as smite:
        print(await smite.getDataUsed())

async def amain():
    await standard_async()
    await context_manager()

def main():
    with pyrez.PaladinsAPI(devId, authKey) as paladins:
        print(paladins.getDataUsed())
    try:
        import asyncio
    except ImportError:
        import trollius as asyncio #TODO: Expand Python < 3.3 usage
    try:
        asyncio.run(amain())
    except (AttributeError):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(amain())

if __name__ == '__main__':
    main()
