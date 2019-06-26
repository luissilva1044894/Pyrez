import pyrez

fake_dev_id=1004
fake_auth_key='23DF3C7E9BD14D84BF892AD206B6755C'

async def standard_async():
    paladins = pyrez.PaladinsAPI(fake_dev_id , fake_auth_key, is_async=True)
    print(await paladins.getDataUsed())
    paladins.close()

async def context_manager():
    """Async context manager"""
    async with pyrez.SmiteAPI.Async(fake_dev_id, fake_auth_key) as smite:
        print(await smite.getDataUsed())

async def amain():
    await standard_async()
    await context_manager()

def main():
    try:
        import asyncio
    except ImportError:
        import trollius as asyncio #TODO: Expand Python < 3.3 usage
    loop = asyncio.get_event_loop()
    try:
        # Python 3.7+
        asyncio.run(amain())
    except (AttributeError):
        loop.run_until_complete(amain())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()

if __name__ == '__main__':
    main()
