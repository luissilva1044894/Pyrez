
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
	for i in range(kwargs.pop('retries', 5)):
		try:
			r = requests.request(method=method, url=url, params=params, json=json, headers=headers or get_user_agent(), *args, **kwargs)
		except:
			pass
		else:
			return r, json_or_text(r)
	return None, None
