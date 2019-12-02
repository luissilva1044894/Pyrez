
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

__methods__ = ['createsession', 'getdataused', 'gethirezserverstatus', 'getpatchinfo', 'ping', 'testsession']

from .base import Base
from ..utils import decorators
class API(Base):
	@decorators.check_credentials
	def __init__(self, *args, **kw):
		Base.__init__(self, *args, **kw)
		from ..enums.format import Format
		from ..enums.endpoint import Endpoint
		self.auth_key = str(kw.pop('auth_key', args[1])).upper()
		self.dev_id = int(kw.pop('dev_id', args[0]))
		self.__session__ = kw.pop('session_id', None) or None
		self._response_format = Format(kw.pop('response_format', None))
		self.__endpoint__ = Endpoint(kw.pop('endpoint', self.__class__.__name__.lower()))
		# self.status_page = StatusPage(self.__endpoint__)
	def __int__(self):
		return self.dev_id or -1
	@classmethod
	def Async(cls, *args, **kw):
		#return cls(dev_id, auth_key, is_async=True, **kw)
		return cls(is_async=True, *args, **kw)
	def __repr__(self):
		return f'<{self.__class__.__name__} dev_id: {self.dev_id} - {self.__endpoint__}>'
	@property
	def session_id(self):
		if not self.__session__:
			try:
				from ..utils.file import read_file, join_path, get_path
				from ..models.session import Session
				path = join_path((get_path(__file__), f'{self.dev_id}.json'))
				'''
				if self._is_async:
					f = self.loop.create_task(read_file(path, is_async=self._is_async, is_json=True))
				else:
					f = read_file(path, is_async=self._is_async, is_json=True)
				session = Session(api=self, **f)
				'''
				session = Session(api=self, **read_file(path, is_json=True))
			except (ValueError, TypeError):
				pass
			else:
				self.__session__ = session
		if hasattr(self.__session__, 'session_id'):
			return self.__session__.session_id
		return self.__session__ or None
	@session_id.setter
	def session_id(self, session):
		if session and session.is_approved:
			self.__session__ = session
			from ..utils.file import write_file, join_path, get_path
			path = join_path((get_path(__file__), f'{self.dev_id}.json'))
			'''
			if self._is_async:
				self.loop.create_task(write_file(path, session.json, is_async=self._is_async, is_json=True))
			else:
				write_file(path, session.json, is_async=self._is_async, is_json=True)
			#write_file(path, session, is_async=self._is_async)
			'''
			write_file(path, session.json, is_json=True)
	@property
	def _invalid_session_id(self):
		return not self.session_id or not str(self.session_id).isalnum()
	def _check_response_(self, result):
		from ..enums.format import Format
		from ..models.api_response import APIResponse
		
		if result:
			if str(self._response_format).upper() == 'XML' or str(result).lower().find('ret_msg') == -1:
				if 'Endpoint not found.' in str(result):
					from ..exceptions.RequestError import RequestError
					raise RequestError(result)
				#return None if len(str(result)) == 2 and str(result) == '[]' else result
				return None if str(result)[:2] == '[]' else result
			#has_error = APIResponse(**result if str(result).startswith('{') else result[0])
			has_error = APIResponse(**result if str(result)[0] == '{' else result[0])
			if has_error and has_error.has_error:
				#'Invalid session id' in has_error.has_error
				if has_error.error_msg.find('Invalid session id') != -1:
					from ..exceptions.invalid_session_id import InvalidSessionId
					raise InvalidSessionId(has_error.error_msg)
				if has_error.error_msg == 'Approved':
					from ..models.session import Session
					self.session_id = Session(api=self, **result)
				else:
					from ..utils.validators import check_error_msg
					check_error_msg(has_error.error_msg)
					#self._checkErrorMsg(has_error.error_msg)
		return result
	'''
	@classmethod
	def _checkErrorMsg(cls, error_msg):
		if error_msg.find('Error while comparing Server and Client timestamp') != -1 or error_msg.find('Exception - Timestamp') != -1:
			from ..exceptions.invalid_time import InvalidTime
			raise InvalidTime(error_msg)
		if error_msg.find('dailylimit') != -1:
			from ..exceptions.RateLimitExceeded import RateLimitExceeded
			raise RateLimitExceeded(error_msg)
		if error_msg.find("No match_queue returned.  It is likely that the match wasn't live when GetMatchPlayerDetails() was called") != -1:
			from ..exceptions.MatchException import MatchException
			raise MatchException(error_msg)
		if error_msg.find('No Match History') != -1:
			from ..exceptions.MatchException import MatchException
			raise MatchException(error_msg)
		if error_msg.find('Only training queues') != -1 and error_msg.find('are supported for GetMatchPlayerDetails()') != -1:
			from ..exceptions.MatchException import MatchException
			raise MatchException(error_msg)
		if error_msg.find('404') != -1:
			from ..exceptions.NotFound import NotFound
			raise NotFound(error_msg)
		if error_msg.find('The server encountered an error processing the request') != -1:
			from ..exceptions.RequestError import RequestError
			raise RequestError(error_msg)
		if error_msg.find('Maximum number of active sessions reached') != -1:
			from ..exceptions.SessionLimitExceeded import SessionLimitExceeded
			raise SessionLimitExceeded(error_msg)
		if error_msg.find('Exception while validating developer access') != -1:
			from ..exceptions.UnauthorizedError import UnauthorizedError
			raise UnauthorizedError(error_msg)
	'''
	def request(self, api_method=None, params=(), *, json=True):
		from ..exceptions.invalid_session_id import InvalidSessionId
		if api_method:
			if self._is_async:
				async def __make_request__(api_method=None, params=()):
					try:
						if not api_method.lower() in [__methods__[0], __methods__[-2], __methods__[-1]] and self._invalid_session_id:
							raise InvalidSessionId
						return await self.http.get(api_method if str(api_method).lower().startswith('http') else self._build_url_(api_method, params), json=json)
						#return asyncio.ensure_future(self.http.get(self._build_url_(api_method, params), json=json))
					except InvalidSessionId:
						await self._create_session()
						return await __make_request__(api_method=api_method, params=params, json=json)
				return __make_request__(api_method, params)
			try:
				if not api_method.lower() in [__methods__[0], __methods__[-2], __methods__[-1]] and self._invalid_session_id:
					raise InvalidSessionId
				r = self._check_response_(self.http.get(api_method if str(api_method).lower().startswith('http') else self._build_url_(api_method, params), json=json))
				'''
				if isinstance(r, dict):
					try:
						return APIResponse(**r)
					except (ValueError, TypeError):
						pass
				'''
				return r or None
			except InvalidSessionId:
				self._create_session()
				return self.request(api_method=api_method, params=params, json=json)
		raise InvalidArgument('No API method specified!')
		'''
		try:
		_ = self.http.get(self._httpRequest(self.__check_url__(api_method, params)), api_method, params)
		except InvalidSessionId:
			self._createSession()
			return self.makeRequest(api_method, params)# TODO: Raises an exception instead passing api_method/params
		else:
			return _
		'''
	def create_signature(self, api_method, timestamp=None):
		from ..utils.time import get_timestamp
		from ..utils.auth import generate_md5_hash
		return generate_md5_hash([self.dev_id, api_method.lower(), self.auth_key, timestamp or get_timestamp()])
		#return generate_md5_hash('{}{}{}{}'.format(self.dev_id, api_method.lower(), self.auth_key, timestamp or get_timestamp()))

	def _build_url_(self, api_method=None, params=()):
		from ..enums.format import Format
		from ..utils.time import get_timestamp
		if api_method:
			#url = '{}/{}{}'.format(self.__endpoint__, api_method.lower(), Format.JSON if api_method.lower() in __methods__ else self._response_format)
			__r_format__ = Format.JSON if api_method.lower() in __methods__ and str(self._response_format) in ['json', 'xml'] else self._response_format
			url = f'{self.__endpoint__}/{api_method.lower()}{__r_format__}'
			if api_method.lower() != __methods__[-2]:
				url += f'/{self.dev_id}/{self.create_signature(api_method)}'
				if api_method.lower() != __methods__[0] and self.session_id or api_method.lower() == __methods__[-1]:
					if api_method.lower() == __methods__[-1]:
						if isinstance(params, (list, tuple)):
							_arg = params[0]
						else:
							_arg = params or self.session_id
							#if not _arg: raise InvalidArgument('')
						return url + f'/{_arg}/{get_timestamp()}'
					url += f'/{self.session_id}'
				url += f'/{get_timestamp()}'
				if params:
					if isinstance(params, (list, tuple)):
						from datetime import datetime
						from enum import Enum
						url += '/'.join(p.strftime('yyyyMMdd') if isinstance(p, datetime) else str(p.value) if isinstance(p, Enum) else str(p) for p in params if p)
					else:
						url += str(params)
			return url
		raise InvalidArgument('No API method specified!')

	# GET /createsession[response_format]/{dev_id}/{signature}/{timestamp}
	def _create_session(self):
	  from ..models.session import Session
	  _ = self.request(__methods__[0])
	  if not _:
	  	return None
	  return Session(api=self, **_)

	# Criar um decorator pra ver se é async, e retornar como async
	# Decorator pra verificar os inputs, e dar "raise" se for inválido
	# GET /ping[response_format]
	def ping(self):
		if self._is_async:
			r = self.loop.create_task(self.request(__methods__[-2]))
			#<Task pending coro=<API.request.<locals>.__make_request__() running at C:\Program Files\Python37\lib\site-packages\pyrez\api\__init__.py:126>>
		else:
			r = self.request(__methods__[-2])
		return r

	# GET /testsession[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}
	def test_session(self, session_id=None):
	  return self.request(__methods__[-1], params=session_id or self.session_id)

	# GET /getdataused[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}
	def data_used(self):
	  return self.request(__methods__[1])

	# GET /gethirezserverstatus[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}
	def server_status(self):
	  return self.request(__methods__[2])

	# GET /getpatchinfo[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}
	def patch_info(self):
		return self.request(__methods__[-3])

	# GET /getfriends[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}
	def get_friends(self, player_id):
		return self.request('getfriends', params=player_id)

	# GET /getmatchdetails[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{match_id}
	# GET /getmatchdetailsbatch[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{match_id,match_id,match_id,..,match_id}
	# GET /getmatchplayerdetails[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{match_id}
	def get_match(self, match_id, is_live=False):
		if isinstance(match_id, (list, tuple)):
			mthd_name, params = 'getmatchdetailsbatch', ','.join((str(_) for _ in match_id))
		else:
			mthd_name, params = 'getmatchplayerdetails' if is_live else 'getmatchdetails', match_id
		return self.request(mthd_name, params=params)

	# GET /getmatchidsbyqueue[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{queue_id}/{date}/{hour}
	def get_match_ids(self, queue_id, data=None, hour=-1):
		return self.request('getmatchidsbyqueue', params=[queue_id, data, hour])

	# GET /getplayerachievements[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}
	def get_player_achievements(self, player_id):
		return self.request('getplayerachievements', params=player_id)

	# GET /getplayeridbyname[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_name}
	# GET /getplayeridbyportaluserid[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{portal_id}/{portal_user_id}
	# GET /getplayeridsbygamertag[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{portal_id}/{gamer_tag}
	# GET /getplayeridinfoforxboxandswitch[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_name}
	def get_player_id(self, player_name, portal_id=None, *, xbox_or_switch=None):
		if xbox_or_switch:
			return self.request('getplayeridinfoforxboxandswitch', params=player_name)
		if not portal_id:
			r = self.request('getplayeridbyname', params=player_name)
			from ..models.mixins.player import Player
			return [Player(api=self, **_) for _ in r if _] if isinstance(r, list) and len(r) > 1 else Player(api=self, **r[0])
		else:
			mthd_name = 'getplayeridbyportaluserid' if str(player_name).isnumeric() else 'getplayeridsbygamertag'
			params = [portal_id, player_name]
		return self.request(mthd_name, params=params)

	# GET /getplayerstatus[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}
	def get_player_status(self, player_id):
		return self.request('getplayerstatus', params=player_id)

	# GET /getqueuestats[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}/{queue_id}
	def get_queue_stats(self, player_id, queue_id):
		return self.request('getqueuestats', params=[player_id, queue_id])

	# GET /searchplayers[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{search_player}
	def search_players(self, player_name):
		return self.request('searchplayers', params=player_name)

__all__ = (
	'API',
)

"""
API:
  ping
  createsession
  testsession
  getdataused
  gethirezserversatus
  getpatchinfo

  getgods/getitems
    getgodleaderboard
    getgodskins
    getgodrecommendeditems
  getchampions
    getchampioncards
    getchampionleaderboard
    getchampionskins
  getplayer
    getfriends
    getgodranks
    getchampionranks
    getplayerloadouts
    getplayerachievements
    getplayerstatus
      getmatchplayerdetails
    getmatchhistory
      getmatchdetails
    getqueuestats
  getplayerId
  searchplayers
  getdemodetails
  getmatchidsbyqueue
  getleagueseasons
    getleagueleaderboard
  searchteams
    getteamdetails
    getteamplayers
  getesportsproleaguedetails
  getmotd
"""
