def get_str():
	from sys import version_info
	return str if version_info[0] >= 3 else unicode
def lower(s):
	try:
		return get_str()(s).lower()
	except TypeError:
		return None
def upper(s):
	try:
		return get_str()(s).upper()
	except TypeError:
		return None
def to_camel_case(name):
	if isinstance(name, int):
		return name
	components = name.split('_')
	return components[0] + "".join(x.title() for x in components[1:])
def title(s):
	try:
		import re
		return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)
	except (ImportError, TypeError):
		return None

def random(length=32, source=None):
	import string
	import random
	return ''.join(random.choice(source or (string.ascii_letters + string.digits)) for x in range(length))

def encode(value, encoding='utf-8'):
	"""
	Parameters
	----------
	value : |STR|
	encoding : |STR|

	Returns
	-------
	str
		String encoded to format type
	"""
	try:
		import six
	except ImportError:
		pass
	else:
		if not isinstance(value, six.text_type):
			return get_str()(value)
	return value.encode(encoding)

def decode(value, encoding='utf-8'):
	return value.decode(u'utf-8')
