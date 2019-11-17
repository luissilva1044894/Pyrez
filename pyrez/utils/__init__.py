#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------- IMPORT DEPENDENCIES -------
#import json

# ------- IMPORT LOCAL DEPENDENCIES  -------

#def find_defining_class(obj, meth_name):
#    return [ty for ty in type(obj).mro() if meth_name in ty.__dict__]
#print find_defining_class(car, 'speedometer')

#from .datetime import *
#from .http import *
#from .json import *
#from .string import *

def join(params, separator=None):
    return (separator or '').join((str(_) for _ in params if _))

def get_path(file=None):
    import os
    import inspect
    if file:
        return os.path.dirname(os.path.abspath(file))
    return os.path.abspath(inspect.stack()[-1][1])

def format_decimal(data, form=',d'):
    return format(int(data), form) if data else 0
def get_asyncio():
    try:
        import asyncio
    except ImportError:
        import trollius as asyncio
    return asyncio

def ___(_, __, ___=1, _____=None):#![]: 0
    if isinstance(_, str):
        try:
            return __(_)
        except Exception as exc:
            print(exc, _)
    if ___:
        return [__(**____) for ____ in (_ or [])]#([][0] if [] and len([]) < 2 else []) or None#str(_).startswith('[')
    try:
        return __(**_[0])
    except (IndexError, KeyError):
        return __(**_)
    except TypeError:
        pass
    if _____:
        raise _____
    return None

def is_num(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True

def int_or_string(val):
    """Loads a value from MO into either an int or string value.
    String is returned if we can't turn it into an int.
    """
    try:
        return int(val.replace(',', ''))
    except ValueError:
        return val

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
