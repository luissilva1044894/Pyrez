class APIBase:
    #Do not instantiate this object directly; instead, use::
    """Provide an base class for easier requests. DON'T INITALISE THIS YOURSELF!

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
    def __init__(self, headers=None, cookies=None, loggerName=None, debug_mode=True):
        from ..utils.http import get_user_agent
        import requests
        self.debug_mode = debug_mode
        if self.debug_mode:
            from ..logging import create_logger
            self.logger = create_logger(loggerName or self.__class__.__name__)
        self.headers = headers or get_user_agent()
        self.cookies = cookies
        self.__session__ = requests.Session()
    def __enter__(self):
        """Enable context management usage: `with APIBase() as api_base`"""
        return self
    def __exit__(self, *args):
        """Clean up."""
        self.__session__.close()
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
    def _httpRequest(self, url, method="GET", raise_for_status=True, params=None, data=None, headers=None, cookies=None, json=None, files=None, auth=None, timeout=None, allowRedirects=False, proxies=None, hooks=None, stream=False, verify=None, cert=None):
        """Make a synchronous HTTP request with the `requests` library.

        Parameters
        ----------
        url : str
            URL of the resource
        method : |STR|
            HTTP method to be used by the request
        headers : |DICT|
            Custom headers
        """
        from json.decoder import JSONDecodeError
        with self.__session__.request(method=method, url=url.replace(' ', '%20'), params=params, json=json, data=data, headers=headers or self.headers, cookies=cookies or self.cookies, files=files, auth=auth, timeout=timeout, allow_redirects=allowRedirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert) as resp:
            self.cookies = resp.cookies
            if raise_for_status:
                resp.raise_for_status()#https://2.python-requests.org/en/master/api/#requests.Response.raise_for_status
            if resp.headers.get('Content-Type', '').rfind('application/json') != -1:
                try:
                    return resp.json()
                except (JSONDecodeError, ValueError):
                    return resp.text
            return resp.text
    def close(self):
        """Properly close the underlying HTTP session"""
        return self.__session__.close()
