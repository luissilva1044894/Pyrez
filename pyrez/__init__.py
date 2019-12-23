
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

#
# _____
#|  __ \
#| |__) |   _ _ __ ___ ____
#|  ___/ | | | '__/ _ \_  /
#| |   | |_| | | |  __// /
#|_|    \__, |_|  \___/___|
#        __/ |
#       |___/


__methods__ = ['createsession', 'getdataused', 'gethirezserverstatus', 'getpatchinfo', 'ping', 'testsession']

from .base import Base
from .utils import decorators
from .utils.cache import cache
class API(Base):
  """This is the main class which contains some core functions like making requests to the corresponding Hi-Rez API endpoints."""
  @decorators.check_credentials
  def __init__(self, dev_id, auth_key, *args, **kw):
    Base.__init__(self, *args, **kw)
    from .enums.format import Format
    from .enums.endpoint import Endpoint
    self.auth_key = str(kw.pop('auth_key', auth_key)).upper()
    self.dev_id = int(kw.pop('dev_id', dev_id))
    self.__session__ = kw.pop('session_id', None) or None
    self._response_format = Format(kw.pop('response_format', None))
    self.__endpoint__ = Endpoint(kw.pop('endpoint', self.__class__.__name__.lower()))
    # self.status_page = StatusPage(self.__endpoint__)
  def __int__(self):
    return self.dev_id or -1
  @classmethod
  def Async(cls, dev_id, auth_key, *args, **kw):
    return cls(dev_id, auth_key, is_async=True, *args, **kw)
  def __repr__(self):
    return f'<{self.__class__.__name__} dev_id: {self.dev_id} - {self.__endpoint__}>'
  @property
  def session_id(self):
    if not self.__session__:
      try:
        from .utils.file import read_file, get_path
        from .models.session import Session
        path = f'{get_path(root=True)}\\data\\{self.dev_id}.json'
        '''
        if self.is_async:
          f = self.loop.create_task(read_file(path, is_async=self.is_async, is_json=True))
        else:
          f = read_file(path, is_async=self.is_async, is_json=True)
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
    self.__session__ = session
    if session and hasattr(session, 'is_approved') and session.is_approved:
      from .utils.file import write_file, get_path
      path = f'{get_path(root=True)}\\data\\{self.dev_id}.json'
      '''
      if self.is_async:
        self.loop.create_task(write_file(path, session.json, is_async=self.is_async, is_json=True))
      else:
        write_file(path, session.json, is_async=self.is_async, is_json=True)
      #write_file(path, session, is_async=self.is_async)
      '''
      write_file(path, session.json, is_json=True)
  @property
  def _invalid_session_id(self):
    return not self.session_id or not str(self.session_id).isalnum()
  def _check_response_(self, result):
    from .enums.format import Format
    from .models.api_response import APIResponse

    if result:
      if self._response_format == 'XML' or str(result).lower().find('ret_msg') == -1:
        if 'Endpoint not found.' in str(result):
          from .exceptions.request_error import RequestError
          raise RequestError(result)
        #return None if len(str(result)) == 2 and str(result) == '[]' else result
        return None if str(result)[:2] == '[]' else result
      #has_error = APIResponse(**result if str(result).startswith('{') else result[0])
      has_error = APIResponse(**result if str(result)[0] == '{' else result[0])
      if has_error and has_error.has_error:
        #'Invalid session id' in has_error.has_error
        if has_error.error_msg.find('Invalid session id') != -1:
          from .exceptions.invalid_session_id import InvalidSessionId
          raise InvalidSessionId(has_error.error_msg)
        if has_error.error_msg == 'Approved':
          from .models.session import Session
          self.session_id = Session(api=self, **result)
        else:
          from .utils.validators import check_error_msg
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

  def request(self, api_method=None, params=(), **kw):
    from .exceptions.invalid_session_id import InvalidSessionId
    from .exceptions.invalid_argument import InvalidArgument
    from .utils import ___
    from .utils.cache.data import Data
    #_cls, raises, __cls__ = kw.pop('cls', None), kw.pop('raises', None), self.__class__.__name__.lower()
    _cls, raises, __cls__, _params_ = kw.pop('cls', None), kw.pop('raises', None), (self.__endpoint__.name if hasattr(self, '__endpoint__') else self.__class__.__name__).upper(), None if not params else '_'.join([str(_).upper() for _ in params if _]) if isinstance(params, (list, tuple)) else str(params)
    __filter__, __api__, __sorted_by__, __reverse__ = kw.pop('filter', None), kw.pop('api', None) or self, kw.pop('sorted_by', None), kw.pop('reverse', None)
    _wants_update_ = cache.needs_refresh(api_method, __cls__, _params_, force=kw.pop('force', not kw.pop('cached', True)))
    #_wants_update_ = kw.pop('force', not kw.pop('cached', True) and api_method not in cache._defaults.get(__cls__).keys() or cache._defaults.get(__cls__, {}).get(api_method, {}).get('optional')) or (not cache.has_key(__cls__) or cache.has_key(__cls__) and (not cache.get(__cls__).get(api_method) or cache.get(__cls__).get(api_method).needs_refresh or _params_ and not cache.get(__cls__).get(f'{api_method},{_params_}') or cache.get(__cls__).get(f'{api_method},{_params_}').needs_refresh))
    #_json = kw.pop('json', str(self._response_format) == 'json')
    if api_method:
      if self.is_async:
        async def __request__(api_method=None, params=(), **kw):
          try:
            if _wants_update_:
              if not api_method.lower() in [__methods__[0], __methods__[-2], __methods__[-1]] and self._invalid_session_id:
                raise InvalidSessionId
              #return asyncio.ensure_future(self.http.get(self._build_url_(api_method, params), json=_json))
              r = self._check_response_(await self.http.get(api_method if str(api_method).lower().startswith('http') else self._build_url_(api_method, params), **kw))
              cache.set(__cls__, r, sub_key=api_method if not _params_ else f'{api_method},{_params_}', auto_save=True)
            else:
              r = cache.get(__cls__, sub_key=api_method if not _params_ else f'{api_method},{_params_}')
              if hasattr(r, 'value') and isinstance(r, Data):
                r = r.value
            if not _cls:
              return r or None
            return ___(r, _cls, raises, filter=__filter__, sorted_by=__sorted_by__, reverse=__reverse__, api=__api__)
          except InvalidSessionId:
            await self._create_session()
            return await self.request(api_method=api_method, params=params, cls=_cls, force=_wants_update_, raises=raises, filter=__filter__, sorted_by=__sorted_by__, reverse=__reverse__, api=__api__, **kw)
        return __request__(api_method=api_method, params=params, **kw)
      try:
        if _wants_update_:
          if not api_method.lower() in [__methods__[0], __methods__[-2], __methods__[-1]] and self._invalid_session_id:
            raise InvalidSessionId
          import re
          r = self._check_response_(self.http.get(api_method if re.match('(?i)^(https|http)?://.*$', str(api_method).lower()) else self._build_url_(api_method, params), **kw))
          '''
          try:
            print('try try')
            __timeout__ = kw.pop('timeout', cache._defaults.get(__cls__).get(api_method).get('timeout')) or cache._defaults.get(__cls__).get('timeout')
          except AttributeError:
            print('try except')
            __timeout__ = cache._defaults.get(__cls__).get('timeout')
          '''
          cache.set(__cls__, r, sub_key=api_method if not _params_ else f'{api_method},{_params_}', auto_save=True)
        else:
          r = cache.get(__cls__, sub_key=api_method if not _params_ else f'{api_method},{_params_}')
          if hasattr(r, 'value') and isinstance(r, Data):
            r = r.value
          '''
          if isinstance(r, dict):
            try:
              return APIResponse(**r)
            except (ValueError, TypeError):
              pass
          '''
        #if not _cls:
        #  return r or None
        return ___(r, _cls, raises, filter=__filter__, sorted_by=__sorted_by__, reverse=__reverse__, api=__api__)
      except InvalidSessionId:
        self._create_session()
        return self.request(api_method=api_method, params=params, cls=_cls, force=_wants_update_, raises=raises, api=__api__, filter=__filter__, sorted_by=__sorted_by__, reverse=__reverse__, **kw)# json=_json,
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

  def _create_signature_(self, api_method, timestamp=None):
    from .utils.time import get_timestamp
    from .utils.auth import generate_md5_hash
    return generate_md5_hash([self.dev_id, api_method.lower(), self.auth_key, timestamp or get_timestamp()])
    #return generate_md5_hash('{}{}{}{}'.format(self.dev_id, api_method.lower(), self.auth_key, timestamp or get_timestamp()))

  def _build_url_(self, api_method=None, params=()):
    from .enums.format import Format
    from .utils.time import get_timestamp
    if not api_method:
      raise InvalidArgument('No API method specified!')
    __r_format__ = Format.JSON if api_method.lower() in __methods__ and not self._response_format in ['json', 'xml'] else self._response_format
    url = f'{self.__endpoint__}/{api_method.lower()}{__r_format__}'
    if api_method.lower() != __methods__[-2]:
      url += f'/{self.dev_id}/{self._create_signature_(api_method)}'
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
          url += f"/{'/'.join(p.strftime('yyyyMMdd') if isinstance(p, datetime) else str(p.value) if hasattr(p, 'value') or isinstance(p, Enum) else str(p) for p in params if p)}"
        else:
          url += f'/{params}'
    return url

  def info(self, **kw):
    from .utils.file import read_file, get_path
    from .utils import slugify
    path = f'{get_path(__file__, root=True)}\\data\\links.json'
    return read_file(path)[slugify(self.__endpoint__.name).replace('_', '-')]#['website']['api']

  # GET /createsession[response_format]/{dev_id}/{signature}/{timestamp}
  @cache.defaults(__methods__[0], timeout=15)
  def _create_session(self, **kw):
    from .models.session import Session
    return self.request(__methods__[0], cls=kw.pop('cls', Session), **kw)

  # Decorator pra verificar os inputs, e dar "raise" se for inválido
  @cache.defaults(__methods__[-2], True, timeout=1)
  def ping(self, **kw):
    """/ping[response_format] GET
    A quick way of validating access (establish connectivity) to the API."""
    from .models.ping import Ping
    return self.request(__methods__[-2], cls=kw.pop('cls', Ping), **kw)

  # GET /testsession[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}
  def test_session(self, session_id=None, **kw):
    return self.request(__methods__[-1], params=session_id or self.session_id, **kw)

  # GET /getdataused[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}
  def data_used(self, **kw):
    return self.request(__methods__[1], **kw)

  # GET /gethirezserverstatus[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}
  @cache.defaults(__methods__[1], timeout=15)
  def server_status(self, **kw):
    return self.request(__methods__[2], **kw)

  # GET /getpatchinfo[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}
  def patch_info(self, **kw):
    return self.request(__methods__[-3], **kw)

  # GET /getfriends[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}
  def friends(self, player_id, **kw):
    from .models.player import _Base
    return self.request('getfriends', params=player_id, cls=kw.pop('cls', _Base), filter=kw.pop('filter', 'player_id'), sorted_by=kw.pop('sorted_by', 'name'), **kw)

  # GET /getmatchdetails[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{match_id}
  # GET /getmatchdetailsbatch[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{match_id,match_id,match_id,..,match_id}
  # GET /getmatchplayerdetails[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{match_id}
  @cache.defaults(['getmatchdetails', 'getmatchdetailsbatch'], timeout=15)
  @cache.defaults('getmatchplayerdetails', timeout=5)
  def match(self, match_id, is_live=False, **kw):
    if isinstance(match_id, (list, tuple)):
      mthd_name, params, __sorted_by__ = 'getmatchdetailsbatch', ','.join((str(_) for _ in match_id)), 'Match'
    else:
      mthd_name, params, __sorted_by__ = 'getmatchplayerdetails' if is_live else 'getmatchdetails', match_id, 'taskForce' if is_live else 'TaskForce'
    return self.request(mthd_name, params=params, sorted_by=kw.pop('sorted_by', __sorted_by__), **kw)

  # GET /getmatchidsbyqueue[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{queue_id}/{date}/{hour}
  def match_ids(self, queue_id, data=None, hour=-1, **kw):
    return self.request('getmatchidsbyqueue', params=[queue_id, data, hour], sorted_by=kw.pop('sorted_by', 'Active_Flag'), reverse=kw.pop('reverse', True), **kw)

  # GET /getplayerachievements[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}
  def player_achievements(self, player_id, **kw):
    return self.request('getplayerachievements', params=player_id, **kw)

  # GET /getplayeridbyname[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_name}
  # GET /getplayeridbyportaluserid[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{portal_id}/{portal_user_id}
  # GET /getplayeridsbygamertag[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{portal_id}/{gamer_tag}
  # GET /getplayeridinfoforxboxandswitch[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_name}
  @cache.defaults(['getplayeridinfoforxboxandswitch', 'getplayeridbyname', 'getplayeridbyportaluserid', 'getplayeridsbygamertag'], True, timeout=5)
  def player_id(self, player_name, portal_id=None, *, xbox_or_switch=None, **kw):
    from .models.player import _Base
    if xbox_or_switch:
      return self.request('getplayeridinfoforxboxandswitch', params=player_name, cls=kw.pop('cls', _Base), **kw)
    if not portal_id:
      #return self.__request__('getplayeridbyname', _Base, params=player_name)
      return self.request('getplayeridbyname', params=player_name, cls=kw.pop('cls', _Base), **kw)
    return self.request('getplayeridbyportaluserid' if str(player_name).isnumeric() else 'getplayeridsbygamertag', params=[portal_id, player_name], cls=kw.pop('cls', _Base), **kw)

  # GET /getplayerstatus[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}
  def player_status(self, player_id, **kw):
    from .models.player.status import Status
    return self.request('getplayerstatus', params=player_id, cls=kw.pop('cls', Status), **kw)

  # GET /getqueuestats[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}/{queue_id}
  def queue_stats(self, player_id, queue_id, **kw):
    return self.request('getqueuestats', params=[player_id, queue_id], **kw)

  # GET /searchplayers[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{search_player}
  @cache.defaults(__methods__[-2], True)
  def search_players(self, player_name, **kw):
    return self.request('searchplayers', params=player_name, **kw)

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

from .paladins import (
  Paladins,
)
from .realm_royale import (
  RealmRoyale,
)
from .smite import (
  Smite,
)

#from .enums import *
from .exceptions import (
  PyrezException,
)

from .__version__ import (
  __author__,
  __author_email__,
  __copyright__,
  __description__,#__about__,
  __license__,
  __package_name__,
  __url__,
  version_info,#__version_info__,
  __version__,
)

#from .models import *
#from .utils import *

__all__ = (
  'API',
  'enums',
  'exceptions',
  'models',
  'utils',
  '__version__',
)
