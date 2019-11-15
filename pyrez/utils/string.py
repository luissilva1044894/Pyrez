def get_str():
	try:
		return unicode
	except NameError:
		pass#return str
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
	return components[0] + ''.join(x.title() for x in components[1:])
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
#MAX_LENGTH = 4096
def split_text(text, length=4096):
	return [text[i:i + length] for i in range(0, len(text), length)]
def safe_split_text(text, length=4096):
	temp_text = text
	parts = []
	while temp_text:
		if len(temp_text) > length:
			try:
				split_pos = temp_text[:length].rindex(' ')
			except ValueError:
				split_pos = length
			if split_pos < length // 4 * 3:
				split_pos = length
			parts.append(temp_text[:split_pos])
			temp_text = temp_text[split_pos:].lstrip()
		else:
			parts.append(temp_text)
			break
	return parts
def utf8(raw):
	"""Return the value as a UTF-8 string."""
	if type(raw) == type(u''):
		return raw.encode('utf-8')
	try:
		return unicode(raw, 'utf-8').encode('utf-8')
	except UnicodeError:
		try:
			return unicode(raw, 'iso-8859-1').encode('utf-8')
		except UnicodeError:
			return unicode(raw, 'ascii', 'replace').encode('utf-8')
