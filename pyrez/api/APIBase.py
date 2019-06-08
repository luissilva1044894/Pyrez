class APIBase:
    #Do not instantiate this object directly; instead, use::
    """The constructor for APIBase class. DON'T INITALISE THIS YOURSELF!

    Attributes
    ----------
    headers : class:`dict`
    cookies : class:`dict`

    Keyword arguments
    -----------------
    headers : class:`dict`
    cookies : class:`dict`
    
    Methods
    -------
    __init__(devId, header=None)
    _encode(string, encodeType="utf-8")
    _httpRequest(url, headers=None)
    """
    def __init__(self, headers=None, cookies=None, raise_for_status=True, loggerName=None, debugMode=True):
        from ..__version__ import __title__
        import requests
        from sys import version_info
        self.debugMode = debugMode
        if self.debugMode:
            from ..logging import create_logger
            self.logger = create_logger(name=loggerName)
        self.headers = headers or { 'user-agent': '{pyrez} [Python/{python.major}.{python.minor}.{python.micro} {dependencies.__name__}/{dependencies.__version__}]'.format(pyrez=__title__, python=version_info, dependencies=requests) }
        self.cookies = cookies
        self.__session__ = requests.Session()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.__session__.close()
    def _httpRequest(self, url, method="GET", raise_for_status=True, params=None, data=None, headers=None, cookies=None, json=None, files=None, auth=None, timeout=None, allowRedirects=False, proxies=None, hooks=None, stream=False, verify=None, cert=None, max_tries=3):
        from json.decoder import JSONDecodeError
        with self.__session__.request(method=method, url=url.replace(' ', '%20'), params=params, json=json, data=data, headers=headers or self.headers, cookies=cookies or self.cookies, files=files, auth=auth, timeout=timeout, allow_redirects=allowRedirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert) as resp:
            self.cookies = resp.cookies
            if raise_for_status:
                resp.raise_for_status()#https://2.python-requests.org/en/master/api/#requests.Response.raise_for_status
            try:
                return resp.json()
            except (JSONDecodeError, ValueError):
                return resp.text
    def close(self):
        return self.__session__.close()
    @classmethod
    def _encode(cls, string, encodeType="utf-8"):
        """

        Parameters
        ----------
        string [str]:
        encodeType [str]:

        Returns
        -------
        str
            String encoded to format type
        """
        return str(string).encode(encodeType)
