#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------- IMPORT DEPENDENCIES -------
#import json

# ------- IMPORT LOCAL DEPENDENCIES  -------

def to_camel_case(name):
    if isinstance(name, int):
        return name
    components = name.split('_')
    return components[0] + "".join(x.title() for x in components[1:])

#def find_defining_class(obj, meth_name):
#    return [ty for ty in type(obj).mro() if meth_name in ty.__dict__]
#print find_defining_class(car, 'speedometer') 

def get_user_agent(dependencies, origin=None):
    import sys
    from ..__version__ import __version__, __url__, __package_name__
    __user_agent__ = '{pyrez} ({url} {ver}) [Python/{py.major}.{py.minor}.{py.micro} {dependencies.__name__}/{dependencies.__version__}]'.format(pyrez=__package_name__, url=__url__, ver=__version__, py=sys.version_info, dependencies=dependencies)
    if origin:
        return { 'User-Agent': __user_agent__, 'Origin': origin }
    return { 'User-Agent': __user_agent__ }

def format_decimal(data, form=',d'):
    return format(int(data), form) if data else 0
def get_asyncio():
    try:
        import asyncio
    except ImportError:
        import trollius as asyncio
    return asyncio

def ___(_, __, ___=1):#![]: 0
    if ___:
        return [__(**____) for ____ in (_ or [])]#([][0] if [] and len([]) < 2 else []) or None#str(_).startswith('[')
    try:
        return __(**_[0])
    except (IndexError, KeyError):
        return __(**_)
    except TypeError:
        pass
    return None

def get_str():
    from sys import version_info
    return str if version_info[0] >= 3 else unicode
def _encode(string, encode_type='utf-8'):
        """
        Parameters
        ----------
        string : |STR|
        encode_type : |STR|

        Returns
        -------
        str
            String encoded to format type
        """
        return get_str()(string).encode(encode_type)
def create_signature(params=()):
    """Actually the authKey isn't passed directly, but instead embedded and hashed as MD5 Signature.

    Signatures use 4 items to be created: devId, authKey, methodName (without the Response Format), and timestamp.

    Parameters
    ----------
    methodName : |STR|
        Method name
    timestamp : |STR|
        Current timestamp

    Returns
    -------
    str
        Returns a MD5 hash code of the method (devId + methodName + authKey + timestamp)
    """
    _str = "".join(params) if isinstance(params, (type(()), type([]))) else params
    from hashlib import md5
    return md5(_str.encode('utf-8')).hexdigest()
def is_num(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True

def is_instance_or_subclass(x, cls):
    """Return True if ``x`` is either a subclass or instance of ``cls``."""
    try:
        return issubclass(x, cls)
    except TypeError:
        return isinstance(x, cls)

def deprecated(instead=None):
    def actual_decorator(func):
        def decorated(*args, **kwargs):
            import warnings

            warnings.simplefilter('always', DeprecationWarning) # turn off filter
            fmt = '{0.__name__} is deprecated{}.'.format(', use {1} instead.' if instead else '')

            warnings.warn(fmt.format(func, instead), stacklevel=3, category=DeprecationWarning)
            warnings.simplefilter('default', DeprecationWarning) # reset filter
            return func(*args, **kwargs)
        return decorated
    return actual_decorator

def to_json(obj, separators=(',', ':'), ensure_ascii=True):
    import json
    return json.dumps(obj, separators=(',', ':'), ensure_ascii=True)

def retrieve_name(x, vars_=vars()):
    """Gets the name of x. Does it from the out most frame inner-wards.

    :param x: variable to get name from.
    :return: string
    """
    try:
        import inspect

        for fi in reversed(inspect.stack()):
            names = [k for k, v in fi.frame.f_locals.items() if v is x]
        #print(str([k for k, v in inspect.currentframe().f_back.f_locals.items() if v is x][0])+': '+str(x))
    except ImportError:#[k for k, v in locals().items() if v == x][0]
        names = [k for k in vars_ if isinstance(x, vars_[k])] #type(x) == type(vars_[k]) and x is vars_[k]
    return names[0] if names else None
