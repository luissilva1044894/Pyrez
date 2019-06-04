from json.decoder import JSONDecodeError
from sys import version_info

import requests

from pyrez import __version__ as pyrez
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
    def __init__(self, headers=None, cookies=None, loggerName=None, debugMode=True):
        self.debugMode = debugMode
        if self.debugMode:
            from ..logging import create_logger
            self.logger = create_logger(loggerName or self.__class__.__name__)
        self.headers = headers or { "user-agent": "{pyrez} [Python/{python.major}.{python.minor}.{python.micro} requests/{requests}]".format(pyrez=pyrez.__title__, python=version_info, requests=requests.__version__) }
        self.cookies = cookies
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
        httpResponse = requests.request(method=method, url=url.replace(' ', '%20'), params=params, json=json, data=data, headers=headers or self.headers, cookies=cookies or self.cookies, files=files, auth=auth, timeout=timeout, allow_redirects=allowRedirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert)
        self.cookies = httpResponse.cookies
        if raise_for_status:
            httpResponse.raise_for_status()#https://2.python-requests.org/en/master/api/#requests.Response.raise_for_status
        try:
            return httpResponse.json()
        except (JSONDecodeError, ValueError):
            return httpResponse.text
