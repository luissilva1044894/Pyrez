def get_user_agent(dependencies, origin=None):
    from ..__version__ import __version__, __url__, __package_name__
    __user_agent__ = '{pyrez} ({url} {ver}) [Python/{py.major}.{py.minor}.{py.micro} {dependencies.__name__}/{dependencies.__version__}]'.format(pyrez=__package_name__, url=__url__, ver=__version__, py=sys.version_info, dependencies=dependencies)
    return {'User-Agent': __user_agent__, 'Origin': origin} if origin else {'User-Agent': __user_agent__}
