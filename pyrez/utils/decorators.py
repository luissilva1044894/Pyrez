
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-
import functools

def check_credentials(f):
	@functools.wraps(f)
	def wrapper(self, *args, **kw):
		__dev_id__, __auth_key__ = kw.get('dev_id') or args[0], kw.get('auth_key') or args[1]
		from ..exceptions.invalid_argument import InvalidArgument
		if not __dev_id__ or not __auth_key__:
			raise InvalidArgument('DevId or AuthKey not specified!')#IdOrAuthEmpty('DevId or AuthKey not specified!')
		if len(str(__dev_id__)) != 4 or not str(__dev_id__).isnumeric():
			raise InvalidArgument('You need to pass a valid DevId!')
		if len(str(__auth_key__)) != 32 or not str(__auth_key__).isalnum():
			raise InvalidArgument('You need to pass a valid AuthKey!')
		return f(self, *args, **kw)
	return wrapper
def is_public(f):
	@functools.wraps(f)
	def wrapper(self, *args, **kw):
		if not self.public:
			from ..exceptions.private_account import PrivateAccount
			raise PrivateAccount(self.error_msg or None)
		return f(self, *args, **kw)
	return wrapper

def has_match_id(f):
	@functools.wraps(f)
	def wrapper(self, *args, **kw):
		if not getattr(self, 'match_id') or self.match_id <= 0:
			from ..exceptions import PyrezException
			raise PyrezException
		return f(self, *args, **kw)
	return wrapper
