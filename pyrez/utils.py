#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------- IMPORT DEPENDENCIES ------- 
from time import time
from datetime import datetime
import json
#from dateutil import *
#from dateutil import tz
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
            fmt = '{0.__name__} is deprecated{}.'.format(', use {1} instead.' if instead else '')

            warnings.warn(fmt.format(func, instead), stacklevel=3, category=DeprecationWarning)
            warnings.simplefilter('default', DeprecationWarning) # reset filter
            return func(*args, **kwargs)
        return decorated
    return actual_decorator

def to_json(obj):
    return json.dumps(obj, separators=(',', ':'), ensure_ascii=True)

def retrieve_name(x):#, vars_=vars()):
    import inspect
    """
    Gets the name of x. Does it from the out most frame inner-wards.
    :param x: variable to get name from.
    :return: string
    """
    for fi in reversed(inspect.stack()): #[k for k, v in locals().items() if v == x][0]
        names = [k for k, v in fi.frame.f_locals.items() if v is x] #[k for k in vars_ if type(x) == type(vars_[k]) and x is vars_[k]]
        return names[0] if len(names) > 0 else None
        #print(str([k for k, v in inspect.currentframe().f_back.f_locals.items() if v is x][0])+': '+str(x))

# ------- DATETIME UTILS -------

#def datetime_string_to_datetime_obj, *, strftime='%Y-%m-%dT%H:%M:%S', use_dateutil=True):#Convert datetime string to datetime obj with his format described in strftime argument function
def from_iso_datetime(datetime_string, *, strftime='%m/%d/%Y %I:%M:%S %p'): #'%Y-%m-%dT%H:%M:%S', use_dateutil=True):
    """Parse an ISO8601-formatted datetime string and return a datetime object.
    Use dateutil's parser if possible and return a timezone-aware datetime.
    """
    #if not _iso8601_datetime_re.match(datetime_string):
    #    raise ValueError('Not a valid ISO8601-formatted datetime string')
    #if dateutil_available and use_dateutil: ## Use dateutil's parser if possible
    #    return parser.isoparse(datetime_string)
    #else:
    #    # Strip off timezone info.
    return datetime.strptime(datetime_string[:19], strftime)

def datetime_obj_to_datetime_string(datetime_obj, strftime='%Y-%m-%d %H:%M:%S %H:%M:%S'):
    """Generate UTC datetime string"""
    return datetime_obj.strftime(strftime)

def datetime_local_to_datetime_utc(datetime_local):
    """Hardcode utc zone"""
    utc_zone = tz.gettz('UTC')
    # utc_zone = tz.tzutc()# or Auto-detect utc zone

    # Convert local time to UTC
    return datetime_local.astimezone(utc_zone)

def datetime_utc_to_datetime_local(datetime_utc, local_zone = None):
    if local_zone is None :
        # Hardcode local zone
        # local_zone = tz.gettz('America/Chicago')
        # or Auto-detect local zone
        local_zone = tz.tzlocal()
    # Tell the datetime object that it's in local time zone since
    # datetime objects are 'naive' by default
    return datetime_utc.replace(tzinfo=local_zone)

def string_timestamp_utc_to_string_datetime_utc(timestamp_utc, strftime = '%Y-%m-%d %H:%M:%S'):
    return datetime.fromtimestamp(timestamp_utc).strftime(strftime)

def string_datetime_utc_to_string_timestamp_utc(datetime_utc):
    # timetuple() convert datetime obj to timestamp obj
    # time.mktime convert timestamp obj to timestamp string
    return time.mktime(datetime_utc.timetuple())

# Create Jinja new filter
#def datetimeformat(date, format='%Y-%m-%d %H:%M:%S'):
#    return string_timestamp_utc_to_string_datetime_utc(date, format)
#app.jinja_env.filters['datetimeformat'] = datetimeformat
