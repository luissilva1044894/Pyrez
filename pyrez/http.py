from sys import version_info as pythonVersion
import requests
#import json

# http://docs.python-requests.org/en/master/
# http://docs.python-requests.org/en/latest/api.html
# http://docs.python-requests.org/en/latest/user/advanced.html
# http://docs.python-requests.org/en/master/user/quickstart/
class HttpRequest ():
    defaultHeaders = { "user-agent": "HttpRequestWrapper [Python/{0.major}.{0.minor}]".format (pythonVersion) }
    timeout = 500

    #def __init__ (self, *args, **kwargs):
        #return super ().__init__ (*args, **kwargs)
    def __init__ (self, headers = defaultHeaders):
        self.headers = defaultHeaders if headers is None else headers

    def get (self, url, params = None, data = None, headers = defaultHeaders, cookies = None, files = None, auth = None, timeout = None, allowRedirects = False, proxies = None, hooks = None, stream = False, verify = None, cert = None):
        #return requests.get (url = url, params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allow_redirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)#.text
        return self.request ('GET', url = url.replace (' ', '%20'), params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allowRedirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)
    #requests.post (url, data=json.dumps ({ 'some': 'data' }))
    def request (self, method, url, params = None, data = None, headers = defaultHeaders, cookies = None, files = None, auth = None, timeout = None, allowRedirects = False, proxies = None, hooks = None, stream = False, verify = None, cert = None):
        """Constructs and sends a :class:`Request <Request>`.

         Usage::

          >>> import requests
          >>> req = requests.request('GET', 'http://httpbin.org/get')
          <Response [200]>

        :param method: method for the new :class:`Request` object.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
        :param data: (optional) Dictionary or list of tuples ``[(key, value)]`` (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
        :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
            ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
            or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
            defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
            to add for the file.
        :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How many seconds to wait for the server to send data
            before giving up, as a float, or a :ref:`(connect timeout, read
            timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
                the server's TLS certificate, or a string, in which case it must be a path
                to a CA bundle to use. Defaults to ``True``.
        :param stream: (optional) if ``False``, the response content will be immediately downloaded.
        :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        
        return requests.request (method=method, url = url, params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allow_redirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)
    def post (self, url, params = None, data = None, headers = defaultHeaders, cookies = None, files = None, auth = None, timeout = None, allowRedirects = False, proxies = None, hooks = None, stream = False, verify = None, cert = None):
        return requests.post (url = url.replace (' ', '%20'), params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allow_redirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)
    def put (self, url, params = None, data = None, headers = defaultHeaders, cookies = None, files = None, auth = None, timeout = None, allowRedirects = False, proxies = None, hooks = None, stream = False, verify = None, cert = None):
        return requests.put (url = url.replace (' ', '%20'), params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allow_redirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)
    def delete (self, url, params = None, data = None, headers = defaultHeaders, cookies = None, files = None, auth = None, timeout = None, allowRedirects = False, proxies = None, hooks = None, stream = False, verify = None, cert = None):
        return requests.delete (url = url.replace (' ', '%20'), params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allow_redirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)
    def head (self, url, params = None, data = None, headers = defaultHeaders, cookies = None, files = None, auth = None, timeout = None, allowRedirects = False, proxies = None, hooks = None, stream = False, verify = None, cert = None):
        return requests.head (url = url.replace (' ', '%20'), params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allow_redirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)
    def options (self, url, params = None, data = None, headers = defaultHeaders, cookies = None, files = None, auth = None, timeout = None, allowRedirects = False, proxies = None, hooks = None, stream = False, verify = None, cert = None):
        return requests.options (url = url.replace (' ', '%20'), params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allow_redirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)

        #except urllib.error.HTTPError as e:
            #if e.code == 404:
                #raise NoResultError("Couldn't test session. API auth details may be incorrect.") from None
            #else:
                #traceback.print_exc()