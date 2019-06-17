def get_user_agent(dependencies, origin=None):
    from ..__version__ import __DEFAULT_USER_AGENT__
    import sys
    __user_agent__ = __DEFAULT_USER_AGENT__.format(py=sys.version_info, dependencies=dependencies)
    return {'User-Agent': __user_agent__, 'Origin': origin} if origin else {'User-Agent': __user_agent__}
