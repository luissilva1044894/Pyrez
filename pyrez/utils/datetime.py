# ------- IMPORT DEPENDENCIES -------
from datetime import (
  datetime,
  timedelta,
)
#from dateutil import *
# ------- DATETIME UTILS -------

def get_seen(timestamp):
	delta = datetime.utcnow() - timestamp
	hours, remainder = divmod(int(delta.total_seconds()), 3600)
	minutes, seconds = divmod(remainder, 60)
	days, hours = divmod(hours, 24)
	years, days = divmod(days, 365)
	fmt = '{y}y, {d}d' if years else "{d}d" if days else "{h}h, {m}m" if hours else "{m}m, {s}s"
	return fmt.format(d=days, h=hours, m=minutes, s=seconds)

def string_datetime_utc_to_datetime(datetime_string, strftime='%m/%d/%Y %I:%M:%S %p'):
	return from_iso_datetime(datetime_string, strftime=strftime)
#def datetime_string_to_datetime_obj, *, strftime='%Y-%m-%dT%H:%M:%S', use_dateutil=True):#Convert datetime string to datetime obj with his format described in strftime argument function
def from_iso_datetime(datetime_string, *, strftime='%Y-%m-%dT%H:%M:%S', use_dateutil=True):
	"""Parse an ISO8601-formatted datetime string and return a datetime object.
	Use dateutil's parser if possible and return a timezone-aware datetime.
	"""
	#if not _iso8601_datetime_re.match(datetime_string):
	#    raise ValueError('Not a valid ISO8601-formatted datetime string')
	#if dateutil_available and use_dateutil: ## Use dateutil's parser if possible
	#    return parser.isoparse(datetime_string)
	#else:
	#    # Strip off timezone info.
	try:
		return datetime.strptime(datetime_string[:20], strftime)
	except ValueError:
		return datetime.strptime(datetime_string, strftime)

def datetime_obj_to_datetime_string(datetime_obj, strftime='%Y-%m-%d %H:%M:%S %H:%M:%S'):
	"""Generate UTC datetime string"""
	return datetime_obj.strftime(strftime)

def datetime_local_to_datetime_utc(datetime_local):
	"""Hardcode utc zone"""
	from dateutil import tz
	utc_zone = tz.gettz('UTC') #tz.tzutc()# or Auto-detect utc zone

	# Convert local time to UTC
	return datetime_local.astimezone(utc_zone)

def datetime_utc_to_datetime_local(datetime_utc, local_zone = None):
	if local_zone is None :
		from dateutil import tz
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
	from time import time
	# timetuple() convert datetime obj to timestamp obj
	# time.mktime convert timestamp obj to timestamp string
	return time.mktime(datetime_utc.timetuple())

# Create Jinja new filter
#def datetimeformat(date, format='%Y-%m-%d %H:%M:%S'):
#    return string_timestamp_utc_to_string_datetime_utc(date, format)
#app.jinja_env.filters['datetimeformat'] = datetimeformat
class Timedelta(timedelta):
    """Difference between two datetime values.

    Attributes
    ----------
    days : |FLOAT|
    	The total amount of days within the duration.
    hours : |FLOAT|
        The total amount of hours within the duration.
    minutes : |FLOAT|
        The total amount of minutes within the duration.
    seconds : |FLOAT|
        The total amount of seconds within the duration.
    """
    #staticmethod
    #def get_seen(timestamp): return Timedelta(seconds=(datetime.utcnow() - timestamp).total_seconds())
    @property
    def days(self): return self.seconds / 86400#24*60*60
    @property
    def hours(self): return self.seconds / 3600 #60*60
    @property
    def minutes(self): return self.seconds / 60
    @property
    def seconds(self): return self.total_seconds()
    def __str__(self):
    	fmt = "{d}d" if self.days > 1 else "{h}h, {m}m" if self.hours  > 1 else "{m}m, {s}s"
    	return fmt.format(d=int(self.days), h=int(self.hours), m=int(self.minutes), s=int(self.seconds))
