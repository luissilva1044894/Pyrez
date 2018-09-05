from sys import version_info as pythonVersion
import requests

class HttpRequest():
    defaultHeaders = { "user-agent": "HttpRequestWrapper [Python/{0.major}.{0.minor}]".format(pythonVersion) }
    timeout = 500

    def __init__(self, headers = defaultHeaders):
        self.headers = defaultHeaders if headers is None else headers

    def get(self, url, params = None, data = None, headers = defaultHeaders, cookies = None, files = None, auth = None, timeout = None, allowRedirects = False, proxies = None, hooks = None, stream = False, verify = None, cert = None):
        return self.request('GET', url = url.replace(' ', '%20'), params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allowRedirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)
    def request(self, method, url, params = None, data = None, headers = defaultHeaders, cookies = None, files = None, auth = None, timeout = None, allowRedirects = False, proxies = None, hooks = None, stream = False, verify = None, cert = None):
        return requests.request(method=method, url = url, params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allow_redirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)
    def post(self, url, params = None, data = None, headers = defaultHeaders, cookies = None, files = None, auth = None, timeout = None, allowRedirects = False, proxies = None, hooks = None, stream = False, verify = None, cert = None):
        return requests.post(url = url.replace(' ', '%20'), params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allow_redirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)
    def put(self, url, params = None, data = None, headers = defaultHeaders, cookies = None, files = None, auth = None, timeout = None, allowRedirects = False, proxies = None, hooks = None, stream = False, verify = None, cert = None):
        return requests.put(url = url.replace(' ', '%20'), params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allow_redirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)
    def delete(self, url, params = None, data = None, headers = defaultHeaders, cookies = None, files = None, auth = None, timeout = None, allowRedirects = False, proxies = None, hooks = None, stream = False, verify = None, cert = None):
        return requests.delete(url = url.replace(' ', '%20'), params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allow_redirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)
    def head(self, url, params = None, data = None, headers = defaultHeaders, cookies = None, files = None, auth = None, timeout = None, allowRedirects = False, proxies = None, hooks = None, stream = False, verify = None, cert = None):
        return requests.head(url = url.replace(' ', '%20'), params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allow_redirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)
    def options(self, url, params = None, data = None, headers = defaultHeaders, cookies = None, files = None, auth = None, timeout = None, allowRedirects = False, proxies = None, hooks = None, stream = False, verify = None, cert = None):
        return requests.options(url = url.replace(' ', '%20'), params = params, data = data, headers = headers, cookies = cookies, files = files, auth = auth, timeout = timeout, allow_redirects = allowRedirects, proxies = proxies, hooks = hooks, stream = stream, verify = verify, cert = cert)
