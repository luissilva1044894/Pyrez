
from ..exceptions.ServiceUnavailable import ServiceUnavailable
from ..logging import create_logger
from ..utils.http import http_request
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
        self.debug_mode = debug_mode
        if self.debug_mode:
            self.logger = create_logger(loggerName or self.__class__.__name__)
    def __enter__(self):
        """Enable context management usage: `with APIBase() as api_base`"""
        return self
    def __exit__(self, *args):
        """Clean up."""
        pass
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
    def _httpRequest(self, url, method='GET', raise_for_status=True, params=None, headers=None, json=None, *args, **kwargs):
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
        r, t = http_request(url, method=method, params=params, headers=headers, json=json, *args, **kwargs)
        if raise_for_status:
            if hasattr(r, 'status_code') and r.status_code == 503 or 'The API is unavailable' in r.text:
                raise ServiceUnavailable(r.text)
            r.raise_for_status()
        return t
  
    def close(self):
        """Properly close the underlying HTTP session"""
        pass
