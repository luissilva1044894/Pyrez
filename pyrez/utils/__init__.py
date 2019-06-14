#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------- IMPORT DEPENDENCIES -------
#import json

# ------- IMPORT LOCAL DEPENDENCIES  -------

def get_str():
    from sys import version_info
    return str if version_info[0] == 3 else unicode

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
            fmt = ''.join(['{0.__name__} is deprecated', ', use {1} instead' if instead else '', '.'])

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
        names = [k for k in vars_ if isinstance(x, vars_[k])]#type(x) == type(vars_[k]) and x is vars_[k]
    return names[0] if names else None
