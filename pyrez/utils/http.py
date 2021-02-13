
def get_user_agent(origin=None):
	from ..__version__ import (
		__package_name__,
		__url__,
		__version__,
	)
	import sys
	try:
		import httpx as requests
	except ImportError:
		import requests
	__DEFAULT_USER_AGENT__ = '{pyrez} ({url} {ver}) [Python/{py.major}.{py.minor}.{py.micro} {dependencies.__name__}/{dependencies.__version__}]'.format(pyrez=__package_name__, url=__url__, ver=__version__, py=sys.version_info, dependencies=requests)
	return {'User-Agent': __DEFAULT_USER_AGENT__, 'Origin': origin} if origin else {'User-Agent': __DEFAULT_USER_AGENT__}

def json_or_text(r):
	try:
		return r.json()
	except:
		pass
	return r.text or r.content

try:
	import httpx as requests
except ImportError:
	import requests

def http_request(url, method='GET', raise_for_status=True, params=None, headers=None, json=None, *args, **kwargs):
	r = requests.request(method=method, url=url, params=params, json=json, headers=headers or get_user_agent(), *args, **kwargs)
	if raise_for_status:
		if hasattr(r, 'status_code') and r.status_code == 503 or 'The API is unavailable' in r.text:
			raise ServiceUnavailable(r.text)
		r.raise_for_status()
	return r, json_or_text(r)
