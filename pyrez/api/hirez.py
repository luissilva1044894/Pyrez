
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

class Hirez:
	def __init__(self, web_token=None, *args, **kw):#, username, password
		from ..enums.endpoint import Endpoint
		self.__endpoint__ = Endpoint(kw.pop('endpoint', self.__class__.__name__))
		self.username = kw.pop('username', None)
		self.password = kw.pop('password', None)
		self.__web_token__ = web_token or None

	@property
	def web_token(self):
		if not self.__web_token__:
			self.__web_token__ = self._login().get('webToken')
		return self.__web_token__

	@classmethod
	def _get_endpoint(cls, endpoint=None, act='/acct'):
		from ..enums.endpoint import Endpoint
		#return '{}{}{}'.format(Endpoint.HIREZ, act or '', '/{}'.format(endpoint) if endpoint else '')
		return f'{Endpoint(cls.__name__)}{act or ""}{f"/{endpoint}" if endpoint else ""}'
	
	@classmethod
	def create(cls, username, password, email=None, *args, **kw):
		import requests
		_ = requests.post(url=Hirez._get_endpoint(endpoint='create'), json={'username':username, 'password':password, 'confirmPassword':password, 'email':email, 'over13':'true', 'subscribe':'on'}, *args, **kw)
		return cls(_.json().get('webToken', None), username=username, password=password)

	def login(self, username=None, password=None, recaptcha=None, *args, **kw):
		"""Log in to a Hi-Rez Studios Account"""
		return self.request('login', {'username':username or self.username, 'password':password or self.password}, *args, **kw)
  
	def request(self, endpoint, params={}, *args, **kw):
		#https://api.hirezstudios.com/acct/{resource},{method:{method},headers:{"Content-Type":"application/json"},body:{body}}
		from json.decoder import JSONDecodeError
		import time
		import urllib3
		import requests
		for n in range(kw.pop('max_tries', 5)):
			try:
				with requests.request(method=kw.pop('method', 'POST'), url=self._get_endpoint(endpoint), headers={**kw.pop('headers', {}), **{'Origin': 'https://my.hirezstudios.com'}}, json={**params, **{'webToken':self.web_token}}, *args, **kw) as r:
					if r.headers.get('Content-Type', '').startswith('application'):
						if r.headers.get('Content-Type', '').rfind('json') != -1:
							try:
								return r.json()
							except (JSONDecodeError, ValueError):
								return r.text
					return r.content
			except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError) as exc:
				time.sleep(n)

	def info(self, *args, **kw):
		return self.request('info', *args, **kw)
  
	def decrypt_token(self, token, *args, **kw):
		return self.request('decryptToken', {'token':token}, *args, **kw)
  
	def encrypt_token(self, token=None, *args, **kw):
		return self.request('encryptToken', {'token':token or self.web_token}, *args, **kw)
  
	def link(self, token, platform, *args, **kw):
		if isinstance(platform, bool):
			return self.request('linkSteam', {'token':token, 'platform':'steam'}, *args, **kw)
		return self.request('linkNew', {'token':token, 'platform':platform}, *args, **kw)

	def validate_recaptcha(self, recaptcha, *args, **kw):
		return self.request('validateRecaptcha', {'captcha':recaptcha}, *args, **kw)

	def change_email(self, new_email, *args, **kw):
		return self.request('changeEmail', {'newEmail':new_email, 'password':self.password}, *args, **kw)

	def create_single_use_code(self, *args, **kw):
		return self.request('createSingleUseCode', *args, **kw)

	def create_verification(self, *args, **kw):
		return self.request('createVerification', *args, **kw)

	def rewards(self, *args, **kw):
		return self.request('rewards', *args, **kw)

	def transactions(self, *args, **kw):
		return self.request('transactions', *args, **kw)

	def set_backup_email(self, backup_email, *args, **kw):
		return self.request('setBackupEmail', {'email':backup_email}, *args, **kw)

	def subscribe(self, subscribe=False, *args, **kw):
		return self.request('subscribe', {'subscribe':subscribe}, *args, **kw)

	def two_factor(notify_email=True, notify_sms=False, validation_period=1, *args, **kw):
		return self.request('twoFactorOptIn', {'notifyBySms':notify_sms, 'notifyByEmail':notify_email, 'validationPeriod':validation_period}, *args, **kw)

	def verify(self, key, *args, **kw):
		return self.request('verify', {'key': key}, *args, **kw)

	'''
	def create_affiliate(self, first_name, last_name, email, country, channel_id, platformId, platform_player, community_name, address1, state_province, city, address_zip, privacy, *args, **kw):
		return requests.post('https://acct.hirezstudios.com/api/affiliate/create', headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=f'email=${email}&gameId=${game_id}&recordType=${record_type}&firstName=${first_name}&lastName=${last_name}&country=${country}&urlTwitter=${url_twitter}&urlFacebook=${url_facebook}&urlTwitch=${url_twitch}&urlYouTube=${url_youtube}&urlMixer=${url_mixer}&urlOther=${url_other}&urlWebsite=${url_website}&primaryChannelId=${channel_id}&primaryPlatformId=${platform_id}&primaryPlatformPlayer=${platform_player}&phone=${phone}&communityName=${community_name}&address1=${address1}&address2=${address2}&stateProvince=${state_province}&city=${city}&zip=${address_zip}&comments=${comments}&accountId=${user_id}', *args, **kw)
	'''

__all__ = (
	'Hirez',
)
