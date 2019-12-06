
__all__ = (
  #'dump',
  'dumps',
  #'load',
  'loads',
  'JSONDecoder',
  'JSONEncoder',
  'jsonify',
)

# ujson is blazing fast, but fall back to standard json if not installed
try:
  import simplejson as _json
except ImportError:
  try:
    from django.utils import simplejson as _json
  except ImportError:
    try:
      import ujson as _json
    except ImportError:
      import json as _json#raise ImportError('A json library is required to use this python library')

def _wrap_reader_for_text(fp, encoding):
  if isinstance(fp.read(0), bytes):
    fp = io.TextIOWrapper(io.BufferedReader(fp), encoding)
  return fp
def _wrap_writer_for_text(fp, encoding):
  try:
    fp.write('')
  except TypeError:
    fp = io.TextIOWrapper(fp, encoding)
  return fp

def custom_encoder(obj):
  import datetime
  if isinstance(obj, datetime.datetime):
    return obj.isoformat()

def dump(obj, fp, *args, **kw):
  encoding = kw.pop('encoding', None)
  if encoding:
    fp = _wrap_writer_for_text(fp, encoding)
  return _json.dump(obj, fp, **kw)

def dumps(obj, *args, **kw):
  #kw['default'] = custom_encoder
  kw.setdefault('ensure_ascii', False)
  kw.setdefault('sort_keys', False)
  kw.setdefault('cls', JSONEncoder)

  encoding = kw.pop('encoding', None)
  rv = _json.dumps(obj, *args, **kw)
  if encoding and isinstance(rv, str):#text_type
    return rv.encode(encoding)
  return rv

def loads(obj, *args, **kw):
  kw.setdefault('cls', JSONDecoder)
  #kw['cls'] = JSONDecoder
  return _json.loads(obj, *args, **kw)

def unpack_json(data):
  return loads(data)

def jsonify(*args, **kw):
  # if args and kw: raise TypeError('jsonify() behavior undefined when passed both args and kwargs')
  data = args[0] if len(args) == 1 else args or kw
  indent = kw.pop('indent', None)#2
  separators = kw.pop('indent', (',', ':'))#(', ', ': ')
  return dumps(data, indent=indent, separators=separators)

class JSONEncoder(_json.JSONEncoder):
  """
  JSON serializer for objects not serializable by default json code.
  Decoder that transforms ISO time format representations into datetime.datetime
  """
  def default(self, obj):
    from datetime import date
    from uuid import UUID
    if isinstance(obj, date): #isinstance(obj, (date, time)): return obj.isoformat()
      from email.utils import formatdate
      from time import mktime
      return formatdate(timeval=mktime((obj.timetuple())), localtime=False, usegmt=True)
    if hasattr(obj, 'isoformat'):
      return obj.isoformat()
      # return { '_type': 'datetime', 'value': obj.strftime('%Y-%m-%d %H:%M:%S') }
    if isinstance(obj, UUID):
      return str(obj)
    if hasattr(obj, 'to_json'):
      return obj.to_json()
      # return self.default(obj.to_json())
    if hasattr(obj, '__slots__'):
      return {_: getattr(obj, _) for _ in obj.__slots__ if hasattr(obj, _)}
    if hasattr(obj, '__dict__'):
      return obj.__dict__ or {}
    try:
      return super().default(obj)
    except TypeError:
      return str(obj)
    # return super(_json.JSONEncoder, self).default(obj)
    # return _json.JSONEncoder.default(self, obj)
# json.dumps(obj, default=JSONEncoder.default)
# json.dumps(obj, default=lambda x: x.__dict__)
# default=lambda x: getattr(x, '__dict__', str(x))

def new_scanstring(s, end, encoding=None, strict=True):
  import re
  iso_datetime_regex = re.compile(r'^(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d\.\d+([+-][0-2]\d:[0-5]\d|Z)?)|(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d([+-][0-2]\d:[0-5]\d|Z)?)|(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d([+-][0-2]\d:[0-5]\d|Z)?)$')
  (s, end) = json.decoder.scanstring(s, end, strict) #(s, end) = _json.decoder.scanstring(s, end, encoding, strict)
  if iso_datetime_regex.match(s):
    import dateutil.parser
    return (dateutil.parser.parse(s), end)
    # return datetime.fromisoformat(s)
  if re.compile(r'^\d{4}-[01]\d-[0-3]\d').match(s):
    from datetime import date
    return (date.fromisoformat(s), end)
  if re.compile(r'[0-2]\d:[0-5]\d:[0-5]\d').match(s):
    from datetime import time
    return (time.fromisoformat(s), end)
  return (s, end)

class JSONDecoder(_json.JSONDecoder):
  def __init__(self, *args, **kw):
    _json.JSONDecoder.__init__(self, *args, **kw)
    #_json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kw)
    self.parse_string = new_scanstring
    self.scan_once = _json.scanner.py_make_scanner(self) # Use the python version as the C version do not use the new parse_string

  def object_hook(self, obj):
    if '_type' not in obj:
      return obj
    _type = obj['_type']
    if _type == 'datetime':
      return parser.parse(obj['value'])
    return obj
