import sys
ASYNC = sys.version_info[:2] >= (3, 4)
if ASYNC:
    try:
        from ..utils import get_asyncio
        asyncio = get_asyncio()
        import aiohttp
        import aiofiles
    except ImportError:
        ASYNC = False#import trollius as asyncio; from trollius import From
import requests
class APIBase:
    #Do not instantiate this object directly; instead, use::
    """The constructor for APIBase class. DON'T INITALISE THIS YOURSELF!

    Attributes
    ----------
    headers : |DICT|
    cookies : |DICT|

    Keyword Arguments
    -----------------
    headers : |DICT|
    cookies : |DICT|

    Methods
    -------
    __init__(devId, header=None)
    _encode(string, encodeType="utf-8")
    _httpRequest(url, headers=None)
    """
    def __init__(self, headers=None, cookies=None, raise_for_status=True, logger_name=None, debug_mode=True, is_async=False, loop=None):
        from ..utils import get_user_agent#super().__init__(headers, cookies)
        self._is_async = ASYNC
        if ASYNC:
            self._is_async = is_async
            if self._is_async:
                self.update_loop(loop)
        self.debug_mode = debug_mode
        if self.debug_mode:
            from .. import logger#from ..__init__ import logger
            self.logger = logger
        self.headers = headers or get_user_agent(requests if not self._is_async else aiohttp)
        self.cookies = cookies
        self.__session__ = requests.Session() if not self._is_async else aiohttp.ClientSession(cookies=self.cookies, headers=self.headers, raise_for_status=raise_for_status)#loop=self.loop, connector=aiohttp.TCPConnector(limit=100),
    #def __del__(self):
    #    """Closes the session instance cleanly when the instance is deleted. Useful for things like when the interpreter closes."""
    #    if ASYNC and self._is_async:
    #        return self._close()
    #    self.close()
    def __enter__(self):
        """We are our own iterator."""
        return self
    def __exit__(self, *args):
        return self.close()
    def _httpRequest(self, url, method="GET", raise_for_status=True, params=None, data=None, headers=None, cookies=None, json=None, files=None, auth=None, timeout=None, allowRedirects=False, proxies=None, hooks=None, stream=False, verify=None, cert=None, max_tries=3):
        if ASYNC and self._is_async:
            return self._async_httpRequest(url=url, method=method, params=params, data=data, headers=data, cookies=cookies, json=json, files=files, auth=auth, timeout=timeout, allowRedirects=allowRedirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert, max_tries=max_tries)
        from json.decoder import JSONDecodeError
        with self.__session__.request(method=method, url=url.replace(' ', '%20'), params=params, json=json, data=data, headers=headers or self.headers, cookies=cookies or self.cookies, files=files, auth=auth, timeout=timeout, allow_redirects=allowRedirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert) as resp:
            self.cookies = resp.cookies
            if raise_for_status:
                resp.raise_for_status()#https://2.python-requests.org/en/master/api/#requests.Response.raise_for_status
            try:
                return resp.json()
            except (JSONDecodeError, ValueError):
                return resp.text
    if ASYNC:
        @classmethod
        def Async(cls, headers=None, cookies=None, raise_for_status=True, logger_name=None, debug_mode=True, loop=None):
            return cls(headers=headers, cookies=cookies, raise_for_status=raise_for_status, logger_name=loggerName, debug_mode=debug_mode, is_async=True, loop=loop)
        @asyncio.coroutine
        async def __aenter__(self):
            """We are our own iterator."""
            return self.__enter__()
        async def __aexit__(self, *args):#, exc_type, exc, traceback
            await self.close()#return
        @staticmethod
        def wrap(func):#https://github.com/Tinche/aiofiles/blob/master/aiofiles/os.py
            from functools import partial, wraps
            @asyncio.coroutine
            @wraps(func)
            def run(*args, loop=None, executor=None, **kwargs):
                if not loop:
                    loop = APIBaseMixin.get_loop()
                    pfunc = partial(func, *args, **kwargs)
                return loop.run_in_executor(executor, pfunc)
            return run
        async def _close(self):
            #await self.__loop.close()
            await self.__session__.close()
        #def close(self):
        #    if self._is_async:
        #        self.__loop.close()
        #    return self.__session__.close()
        #https://www.tutorialsteacher.com/python/property-decorator
        @property
        def loop(self): return self.__loop
        @loop.setter
        def loop(self, value=None): self.update_loop(value)
        @staticmethod
        def get_loop(force_fresh=False):
            """
            Parameters
            ----------
            force_fresh : |BOOL|
                Get a new loop

            Returns
            -------
            asyncio.AbstractEventLoop
                Return a loop event
            """
            import os
            # Let's not force this dependency, uvloop is much faster on cpython
            if sys.implementation.name == 'cpython':
                try:
                    import uvloop
                except ImportError:
                    pass
                else:
                    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
            if sys.platform == 'win32':# or os.name == 'nt':
                if not force_fresh and isinstance(asyncio.get_event_loop(), asyncio.ProactorEventLoop) and not asyncio.get_event_loop().is_closed():
                    return asyncio.get_event_loop()
                return asyncio.ProactorEventLoop()
            if force_fresh or asyncio.get_event_loop().is_closed():
                return asyncio.new_event_loop()
            return asyncio.get_event_loop()
        def update_loop(self, loop=None):
            self.__loop = loop or self.get_loop(True)
            asyncio.set_event_loop(self.__loop)
        async def _async_httpRequest(self, url, method='GET', params=None, data=None, headers=None, cookies=None, json=None, files=None, auth=None, timeout=None, allowRedirects=False, proxies=None, hooks=None, stream=False, verify=None, cert=None, max_tries=3):
            from json.decoder import JSONDecodeError
            for x in range(max_tries):
                try:
                    async with self.__session__.request(method=method, url=url, params=params, data=data, json=json, timeout=timeout) as resp:
                        try:
                            return await resp.json()
                        except (JSONDecodeError, ValueError):
                            return await resp.text()
                except (aiohttp.ServerDisconnectedError, asyncio.TimeoutError):# as exc:#!0?
                    await asyncio.sleep(1)
    #else:
    def close(self):
        if ASYNC and self._is_async:
            return self._close()
        self.__session__.close()
