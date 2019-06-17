import sys
ASYNC = sys.version_info[:2] >= (3, 4)
if ASYNC:
    try:
        from ..utils import get_asyncio
        asyncio = get_asyncio()
        import aiohttp
        #import aiofiles
    except ImportError:
        ASYNC = False#import trollius as asyncio; from trollius import From
    else: # Removes the aiohttp ClientSession instance warning.
        class HTTPSession(aiohttp.ClientSession):#session = HTTPSession()
            """Abstract class for aiohttp."""
            def __init__(self, loop=None):
                super().__init__(loop=loop or self.get_loop())
            def __del__(self):
                """Closes the session instance cleanly when the instance is deleted. Useful for things like when the interpreter closes."""
                if not self.closed:
                    self.close()
        #https://www.tutorialsteacher.com/python/property-decorator
        #@property
        #def loop(self): return self.__loop
        #@loop.setter
        #def loop(self, value=None): self.update_loop(value)
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
            if sys.implementation.name == 'cpython':# Let's not force this dependency, uvloop is much faster on cpython
                try:
                    import uvloop
                except ImportError:
                    pass
                else:
                    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
            if sys.platform == 'win32':
                if not force_fresh and isinstance(asyncio.get_event_loop(), asyncio.ProactorEventLoop) and not asyncio.get_event_loop().is_closed():
                    return asyncio.get_event_loop()
                return asyncio.ProactorEventLoop()
            if force_fresh or asyncio.get_event_loop().is_closed():
                return asyncio.new_event_loop()
            return asyncio.get_event_loop()
        #def update_loop(self, loop=None):
        #    self.__loop = loop or self.get_loop()
        #    asyncio.set_event_loop(self.__loop)
import requests

def json_or_text(resp, is_async=False, encoding='utf-8'):
    from json.decoder import JSONDecodeError
    if is_async:
        async def a_json_or_text(resp, encoding='utf-8'):
            import aiohttp
            try:
                return await resp.json()
            except (JSONDecodeError, ValueError, aiohttp.ContentTypeError):
                return await resp.text(encoding=encoding)
        return a_json_or_text(resp, encoding)
    try:
        return resp.json()
    except (JSONDecodeError, ValueError):
        return resp.text
class APIBase:
    #Do not instantiate this object directly; instead, use::
    """Provide an base class for easier requests. DON'T INITALISE THIS YOURSELF!

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
        self.debug_mode = debug_mode
        if self.debug_mode:
            #from .. import logger#from ..__init__ import logger
            #self.logger = logger
            from ..logging import create_logger
            self.logger = create_logger(self.__class__.__name__)
        self.headers = headers or get_user_agent(requests if not self._is_async else aiohttp)
        self.cookies = cookies
        self.__session__ = requests.Session() if not self._is_async else aiohttp.ClientSession(cookies=self.cookies, headers=self.headers, raise_for_status=raise_for_status)#loop=self.loop, connector=aiohttp.TCPConnector(limit=100),
    def __enter__(self):
        """Enable context management usage: `with APIBase() as api_base`"""
        return self
    def __exit__(self, *args):
        """Clean up."""
        return self.close()
    def __dir__(self):
        """https://github.com/vintasoftware/tapioca-wrapper/blob/master/tapioca/tapioca.py"""
        return [m for m in self.__dict__.keys() if not m.startswith('__')]
        #methods_list = [func for func in dir(APIBase) if callable(getattr(self, func))]
        #methods_list += [m for m in dir(APIBase) if m.startswith('to_')]#RecursionError

        #from types import FunctionType
        #return [x for x, y in self.__dict__.items() if type(y) == FunctionType and not x.startswith('__')]

        #return [(n, t) for n, t in self.__dict__.items() if type(t).__name__ != 'function' and not n.startswith('__')]
    def _httpRequest(self, url, method="GET", raise_for_status=True, params=None, data=None, headers=None, cookies=None, json=None, files=None, auth=None, timeout=None, allowRedirects=False, proxies=None, hooks=None, stream=False, verify=None, cert=None, max_tries=3):
        """Make an HTTP request.

        Parameters
        ----------
        url : str
            URL of the resource
        method : |STR|
            HTTP method to be used by the request
        headers : |DICT|
            Custom headers
        session : aiohttp.ClientSession, optional
            Client session used to make the request
        """
        from json.decoder import JSONDecodeError
        if ASYNC and self._is_async:
            async def __http_request__(url, method='GET', params=None, data=None, headers=None, cookies=None, json=None, files=None, auth=None, timeout=None, allowRedirects=False, proxies=None, hooks=None, stream=False, verify=None, cert=None, max_tries=3, encoding='utf-8'):
                for x in range(max_tries):
                    try:
                        async with self.__session__.request(method=method, url=url, params=params, data=data, json=json, timeout=timeout) as resp:
                            if resp.headers.get('Content-Type', '').rfind('application/json') != -1:
                                return await json_or_text(resp, True)
                            return await resp.read()
                    except (aiohttp.ServerDisconnectedError, asyncio.TimeoutError):# as exc:#!0?
                        await self.sleep(1)
            return __http_request__(url=url, method=method, params=params, data=data, headers=headers or self.headers, cookies=cookies or self.cookies, json=json, files=files, auth=auth, timeout=timeout, allowRedirects=allowRedirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert, max_tries=max_tries)
        with self.__session__.request(method=method, url=url.replace(' ', '%20'), params=params, json=json, data=data, headers=headers or self.headers, cookies=cookies or self.cookies, files=files, auth=auth, timeout=timeout, allow_redirects=allowRedirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert) as resp:
            self.cookies = resp.cookies
            if raise_for_status:
                resp.raise_for_status()#https://2.python-requests.org/en/master/api/#requests.Response.raise_for_status
            if resp.headers.get('Content-Type', '').rfind('application/json') != -1:
                return json_or_text(resp)
            return resp.context
    def close(self):
        """Properly close the underlying HTTP session"""
        if ASYNC and self._is_async:
            async def __close__():
                # await self.__loop.close()
                await self.__session__.close()
            return __close__()
        self.__session__.close()
    if ASYNC:
        @classmethod
        def Async(cls, headers=None, cookies=None, raise_for_status=True, logger_name=None, debug_mode=True, loop=None):
            """Asynchronous version of :class:.APIBase` with synchronous context management capabilities."""
            return cls(headers=headers, cookies=cookies, raise_for_status=raise_for_status, logger_name=loggerName, debug_mode=debug_mode, is_async=True, loop=loop)
        async def sleep(self, seconds):
            """Sleep for the specified number of seconds."""
            await asyncio.sleep(seconds)
        @asyncio.coroutine
        async def __aenter__(self):
            """Enable asynchronous context management usage: `async with APIBase() as api_base`"""
            return self.__enter__()
        async def __aexit__(self, *args):#, exc_type, exc, traceback
            """Clean up."""
            await self.close()#return
