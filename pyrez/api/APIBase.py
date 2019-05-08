from json.decoder import JSONDecodeError
from sys import version_info

import requests

import pyrez
class APIBase:
    """
    DON'T INITALISE THIS YOURSELF!
    Attributes:
        headers [dict]:
        cookies [dict]:
    Methods:
        __init__(devId, header=None)
        _encode(string, encodeType="utf-8")
        _httpRequest(url, headers=None)
    """
    def __init__(self, headers=None, cookies=None):
        """
        The constructor for APIBase class.
        Keyword arguments/Parameters:
            headers:
        """
        self.headers = headers or { "user-agent": "{0} [Python/{1.major}.{1.minor} requests/{2}]".format(pyrez.__title__, version_info, requests.__version__) }
        self.cookies = cookies
    @classmethod
    def _encode(cls, string, encodeType="utf-8"):
        """
        Keyword arguments/Parameters:
            string [str]:
            encodeType [str]:
        Returns:
            String encoded to format type
        """
        return str(string).encode(encodeType)
    def _httpRequest(self, url, method="GET", params=None, data=None, headers=None, cookies=None, json=None, files=None, auth=None, timeout=None, allowRedirects=False, proxies=None, hooks=None, stream=False, verify=None, cert=None):
        httpResponse = requests.request(method=method, url=url.replace(' ', '%20'), params=params, json=json, data=data, headers=headers if headers else self.headers, cookies=cookies if cookies else self.cookies, files=files, auth=auth, timeout=timeout, allow_redirects=allowRedirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert)
        self.cookies = httpResponse.cookies
        #if httpResponse.status_code >= 400:
        #    raise NotFoundException("{}".format(httpResponse.text))
        httpResponse.raise_for_status()#https://2.python-requests.org/en/master/api/#requests.Response.raise_for_status
        try:
            return httpResponse.json()
        except (JSONDecodeError, ValueError):
            return httpResponse.text
