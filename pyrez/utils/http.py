def get_user_agent(origin=None):
	import sys
	from ..__version__ import __version__, __url__, __package_name__
	import requests
	__user_agent__ = '{prz} ({u} {v}) [Python/{py.major}.{py.minor}.{py.micro} requests/{re.__version__}]'.format(prz=__package_name__, u=__url__, v=__version__, py=sys.version_info, re=requests)
	return {'User-Agent': __user_agent__, 'Origin': origin} if origin else {'User-Agent': __user_agent__}
