from datetime import datetime

from ..enumerations.Format import Format
from ..enumerations.Language import Language
from ..enumerations.Endpoint import Endpoint
from pyrez.exceptions import UnauthorizedError, InvalidArgument, MatchException, NoResult, NotFound, NotSupported, PlayerNotFound, RequestError, InvalidSessionId#, UnexpectedException
from pyrez.events import Event
from pyrez.models import APIResponse, DataUsed, Friend, LiveMatch, Match, MatchHistory, MatchId as MatchIdByQueue, PatchInfo, Ping, Player, PlayerId, PlayerAcheviements, PlayerStatus, QueueStats, ServerStatus, Session
from .StatusPageAPI import StatusPageAPI
from .APIBase import APIBase, ASYNC
class API(APIBase):
    def __init__(self, devId, authKey, endpoint, *, response_format=Format.JSON, sessionId=None, storeSession=False, headers=None, cookies=None, raise_for_status=True, logger_name=None, debug_mode=True, is_async=False, loop=None):
        super().__init__(headers=headers, cookies=cookies, raise_for_status=raise_for_status, logger_name=logger_name or self.__class__.__name__, debug_mode=debug_mode, is_async=is_async, loop=loop)
        from ..utils import is_num
        from ..utils.string import get_str, upper
        _str = get_str()
        if not devId or not authKey:
            if self.debug_mode:
                self.logger.error('DevId or AuthKey not specified!')
            raise UnauthorizedError('DevId or AuthKey not specified!')
        if not is_num(devId): #len(str(devId)) != 4 or not str(devId).isnumeric():
            if self.debug_mode:
                self.logger.error('You need to pass a valid DevId!')
            raise UnauthorizedError('You need to pass a valid DevId!')
        if len(_str(authKey)) != 32 or not _str(authKey).isalnum():
            if self.debug_mode:
                self.logger.error('You need to pass a valid AuthKey!')
            raise UnauthorizedError('You need to pass a valid AuthKey!')
        if not endpoint:
            if self.debug_mode:
                self.logger.error("Endpoint can't be empty!")
            raise InvalidArgument("Endpoint can't be empty!")
        self.devId = int(devId)
        self.authKey = upper(authKey)
        self.__api_base_url__ = _str(endpoint) 
        self._response_format = Format.JSON #if not response_format or not isinstance(response_format, Format) else response_format
        self.storeSession = storeSession or False
        self.onSessionCreated = Event()
        self.sessionId = sessionId or self._getSession(devId=self.devId) #if sessionId and self.testSession(sessionId)
        self.statusPage = StatusPageAPI() #make all endpoints return just the atual game incidents
    if ASYNC:
        @classmethod
        def Async(cls, devId, authKey, endpoint=Endpoint.PALADINS, response_format=Format.JSON, sessionId=None, storeSession=False, headers=None, cookies=None, raise_for_status=True, logger_name=None, debug_mode=True, loop=None):
            return cls(devId=devId, authKey=authKey, endpoint=endpoint, response_format=response_format, sessionId=sessionId, storeSession=storeSession, headers=headers, cookies=cookies, raise_for_status=raise_for_status, logger_name=logger_name, debug_mode=debug_mode, is_async=True, loop=loop)
    def __request_method__(self, method, x, y=0, params=(), raises=None):
        if ASYNC and self._is_async:
            async def __async_request_method__(method, x, y, params=(), raises=None):
                from ..utils import ___
                return ___(await self.makeRequest(method, params), x, y, raises)
            return __async_request_method__(method, x, y, params, raises)
        from ..utils import ___
        return ___(self.makeRequest(method, params), x, y)
    def __check_url__(self, api_method, params):
        return api_method if str(api_method).lower().startswith('http') else self._buildUrlRequest(api_method, params)
    def _getSession(self, idOnly=True, devId=None):
        try:
            from ..utils.json import read
            from ..utils import get_path, join
            path = join((get_path(__file__), '/', devId or self.devId, '.json'))
            session = Session(**read(path, ASYNC and self._is_async))
        except (FileNotFoundError, ValueError, TypeError):
            return None
        else:
            return session.sessionId if idOnly else session
    def _setSession(self, session, devId=None):
        self.sessionId = session.sessionId
        if self.storeSession and session:
            from ..utils import get_path, join
            from ..utils.json import write
            path = join((get_path(__file__), '/', devId or self.devId, '.json'))
            write(session.json, path, ASYNC and self._is_async)
    @staticmethod
    def _getCurrentTime():
        """
        Returns
        -------
        datetime
            Returns the current UTC time (GMT+0).
        """
        return datetime.utcnow()
    @staticmethod
    def _createTimeStamp(timeFormat='%Y%m%d%H%M', addZero=True):
        """
        Parameters
        ----------
        timeFormat : |STR|
            Format of timeStamp (%Y%m%d%H%M%S)
        addZero : |BOOL|
            Add ``00`` instead ``ss``

        Returns
        -------
        str
            Returns the current UTC time (GMT+0) formatted to ``YYYYMMDDHHmmss``
        """
        return API._getCurrentTime().strftime(timeFormat) + ('00' if addZero else '')
    def _createSignature(self, method_name, timestamp=None):
        from ..utils.auth import generate_md5_hash
        return generate_md5_hash([str(self.devId), method_name.lower(), self.authKey, timestamp or self._createTimeStamp()])
        #return generate_md5_hash('{}{}{}{}'.format(self.devId, method_name.lower(), self.authKey, timestamp or self._createTimeStamp()))
    def _sessionExpired(self):
        return not self.sessionId or not str(self.sessionId).isalnum()
    def _buildUrlRequest(self, api_method=None, params=()):
        from enum import Enum
        if not api_method:
            raise InvalidArgument('No API method specified!')
        urlRequest = '{}/{}{}'.format(self.__api_base_url__, api_method.lower(), Format.JSON if api_method.lower() in ['createsession', 'ping', 'testsession', 'getdataused', 'gethirezserverstatus', 'getpatchinfo'] else self._response_format)
        if api_method.lower() != 'ping':
            urlRequest += '/{}/{}'.format(self.devId, self._createSignature(api_method.lower()))
            if self.sessionId and api_method.lower() != 'createsession':
                if api_method.lower() == 'testsession':
                    return urlRequest + '/{}/{}'.format(str(params[0]), self._createTimeStamp())
                urlRequest += '/{}'.format(self.sessionId)
            urlRequest += '/{}{}'.format(self._createTimeStamp(), '/{}'.format('/'.join(param.strftime('yyyyMMdd') if isinstance(param, datetime) else str(param.value) if isinstance(param, Enum) else str(param) for param in params if param)) if params else '')
        return urlRequest.replace(' ', '%20')
    def _check_session_(self, api_method=None):
        if not api_method:
            raise InvalidArgument('No API method specified!')
        return not api_method.lower() in ['createsession', 'ping', 'testsession'] and self._sessionExpired()
    def _check_response_(self, result, api_method, params):
        if result:
            if self._response_format.equal(Format.XML) or str(result).lower().find("ret_msg") == -1:
                return None if len(str(result)) == 2 and str(result) == "[]" else result
            hasError = APIResponse(**result if str(result).startswith('{') else result[0])
            if hasError and hasError.hasError:
                if hasError.errorMsg.find('Invalid session id') != -1:
                    if self.debug_mode:
                        self.logger.debug('{} - {}'.format(hasError.errorMsg, self.sessionId))
                    raise InvalidSessionId(hasError.errorMsg)
                if hasError.errorMsg == 'Approved':
                    session = Session(**result)
                    if self.debug_mode:
                        self.logger.debug('{}: (Old: {} - New: {})'.format(hasError.errorMsg, self.sessionId, session.sessionId))
                    self._setSession(session)
                    if self.onSessionCreated.hasHandlers():
                        self.onSessionCreated(session)
                else:
                    self._checkErrorMsg(hasError.errorMsg)
        return result
    @classmethod
    def _checkErrorMsg(cls, error_msg):
        if error_msg.find('Error while comparing Server and Client timestamp') != -1 or error_msg.find('Exception - Timestamp') != -1:
            from pyrez.exceptions import InvalidTime
            raise InvalidTime(error_msg)
        if error_msg.find('dailylimit') != -1:
            from pyrez.exceptions import RateLimitExceeded
            raise RateLimitExceeded(error_msg)
        if error_msg.find("No match_queue returned.  It is likely that the match wasn't live when GetMatchPlayerDetails() was called") != -1:
            from pyrez.exceptions import MatchException
            raise MatchException(error_msg)
        if error_msg.find('No Match History') != -1:
            from pyrez.exceptions import MatchException
            raise MatchException(error_msg)
        if error_msg.find('Only training queues') != -1 and error_msg.find('are supported for GetMatchPlayerDetails()') != -1:
            from pyrez.exceptions import MatchException
            raise MatchException(error_msg)
        if error_msg.find('404') != -1:
            from pyrez.exceptions import NotFound
            raise NotFound(error_msg)
        if error_msg.find('The server encountered an error processing the request') != -1:
            from pyrez.exceptions import RequestError
            raise RequestError(error_msg)
        if error_msg.find('Maximum number of active sessions reached') != -1:
            from pyrez.exceptions import SessionLimit
            raise SessionLimit(error_msg)
        if error_msg.find('Exception while validating developer access') != -1:
            from pyrez.exceptions import WrongCredentials
            raise WrongCredentials(error_msg)
    def makeRequest(self, api_method=None, params=()):
        """Construct and make a HTTP request to Hi-Rez Studios API.

        Parameters
        ----------
        api_method : |STR|
        params : Optional: |LIST| or |TUPLE|

        Raises
        ------
        pyrez.exceptions.DailyLimit
            |DailyExceptionDescrip|
        TypeError
            |TypeErrorB|
        pyrez.exceptions.WrongCredentials
            |WrongCredentials|
        pyrez.exceptions.RequestError
            Raised when the server encountered an error processing the request.
        pyrez.exceptions.NotFound
            Raised when the requested endpoint is not found.
        pyrez.exceptions.SessionLimit
            Raised when the maximum number of active sessions is reached.
        """
        if ASYNC and self._is_async:
            async def __make_request__(api_method=None, params=()):
                if self._check_session_(api_method):
                    await self._createSession()
                try:
                    _ = self._check_response_(await self._httpRequest(self.__check_url__(api_method, params)), api_method, params)
                except InvalidSessionId:
                    await self._createSession()
                    return await __make_request__(api_method=api_method, params=params)
                else:
                    return _
            return __make_request__(api_method, params)
        if self._check_session_(api_method):
            self._createSession()
        try:
            _ = self._check_response_(self._httpRequest(self.__check_url__(api_method, params)), api_method, params)
        except InvalidSessionId:
            self._createSession()
            return self.makeRequest(api_method, params)# TODO: Raises an exception instead passing api_method/params
        else:
            return _

    # GET /createsession[ResponseFormat]/{devId}/{signature}/{timestamp}
    def _createSession(self):
        """A required step to Authenticate the devId/signature for further API use.

        Raises
        ------
        TypeError
            |TypeError|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('createsession', Session)

    # GET /ping[ResponseFormat]
    def ping(self):#Checks if API is working < TODO: Make all `makeRequest` call ping()
        """A quick way of validating access (establish connectivity) to the Hi-Rez API.

        You do not need to authenticate your ID or key to do this.

        Raises
        ------
        TypeError
            |TypeError|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
        :class:`pyrez.models.Ping`
            Returns a :class:`pyrez.models.Ping` objects containing infos about the API.
        """
        return self.__request_method__('ping', Ping)

    # GET /testsession[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}
    def testSession(self, sessionId=None):
        """A means of validating that a session is established.

        Parameters
        ----------
        sessionId : Optional |STR|
            A sessionId to validate. Passing in ``None`` will use :attr:`.sessionId` instead of the passed in value.

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
        |BOOL|
            Returns True if the given sessionId is valid, False otherwise.
        """
        session = self.sessionId if not sessionId or not str(sessionId).isalnum() else sessionId
        uri = '{}/testsession{}/{}/{}/{}/{}'.format(self.__api_base_url__, self._response_format, self.devId, self._createSignature('testsession'), session, self._createTimeStamp())
        _ = self._httpRequest(uri)
        return _.find('successful test') != -1

    # GET /getdataused[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}
    def getDataUsed(self):
        """Returns API Developer daily usage limits and the current status against those limits.

        NOTE
        ----
        Getting your data usage does contribute to your daily API limits.

        Raises
        ------
        TypeError
            |TypeError|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
        :class:`pyrez.models.DataUsed` or |NONE|
            Returns a :class:`pyrez.models.DataUsed` object containing resources used or |NONE|.
        """
        return self.__request_method__('getdataused', DataUsed)

    # GET /gethirezserverstatus[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}
    def getServerStatus(self):
        """Function returns ``UP``/``DOWN`` status for the primary game/platform environments.

        NOTE
        ----
            Data is cached once a minute.

        Raises
        ------
        TypeError
            |TypeError|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
        pyrez.models.HiRezServerStatus
            Object of pyrez.models.HiRezServerStatus
        """
        return self.__request_method__('gethirezserverstatus', ServerStatus, 1)

    # GET /getpatchinfo[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}
    def getPatchInfo(self):
        """Function returns information about current deployed patch.

        NOTE
        ----
            Currently, this information only includes patch version.

        Raises
        ------
        TypeError
            |TypeError|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
        Object of pyrez.models.PatchInfo
        """
        return self.__request_method__('getpatchinfo', PatchInfo)

    # GET /getfriends[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerId}
    def getFriends(self, playerId):
        """Returns the User names of each of the player’s friends of one player.

        Parameters
        ----------
        playerId : |INT|

        NOTE
        ----
            This method is PC only.

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
            List of pyrez.models.Friend objects
        """
        return self.__request_method__('getfriends', Friend, 1, params=[playerId])#__ = [ (**___) for ___ in (_ or []) if ___.get('player_id', '0') != '0' ]

    # GET /getmatchdetails[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{matchId}
    # GET /getmatchdetailsbatch[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{matchId,matchId,matchId,...matchId}
    # GET /getmatchplayerdetails[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{matchId}
    def getMatch(self, matchId, isLiveMatch=False):
        """Returns the player information / statistics for a particular match.

        There is three ways to call this method::

            getMatch(matchId)
            #or
            getMatch([matchId, matchId, matchId, matchId, matchId])
            #or
            getMatch(matchId, True)

        Parameters
        ----------
        matchId : |INT| or |LIST| of |INT|
            |MatchIdDescrip|
        isLiveMatch : Optional |BOOL|

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Warning
        -------
        There is a byte limit to the amount of data returned.

        Please limit the matchId parameter to 5-10 matches for DB Performance reasons.
        """
        if isinstance(matchId, (type(()), type([]))):
            mthd_name = 'getmatchdetailsbatch'
            params = [','.join(matchId)]
        else:
            mthd_name = 'getmatchplayerdetails' if isLiveMatch else 'getmatchdetails'
            params = [matchId]
        return self.__request_method__(mthd_name, LiveMatch if isLiveMatch else Match, 1, params=params)

    # GET /getmatchhistory[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerId}
    def getMatchHistory(self, playerId):
        """Gets recent matches and high level match statistics for a particular player.

        Parameters
        ----------
        playerId : |INT|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('getmatchhistory', MatchHistory, 1, params=[playerId])

    # GET /getmatchidsbyqueue[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{queueId}/{date}/{hour}
    def getMatchIds(self, queueId, date=None, hour=-1):
        """Lists all Match IDs for a particular Match Queue.

        Useful for API developers interested in constructing data by Queue.

        Parameters
        ----------
        queueId : |INT|
            The id of the game mode
        date : |INT|
        hour : |INT|
            Used to limit the data returned (valid values: 0 - 23).

            An ``hour`` parameter of ``-1`` represents the entire day, but be warned that this may be more data than we can return for certain queues.

        Raises
        ------
        TypeError
            |TypeErrorC|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Warning
        -------
            To avoid HTTP timeouts in the getMatchIds() method, you can now specify a 10-minute window within the specified {hour} field to lessen the size of data returned by appending a “,mm” value to the end of {hour}.

            For example, to get the match Ids for the first 10 minutes of hour 3, you would specify {hour} as “3,00”.

            This would only return the Ids between the time 3:00 to 3:09. Rules below:
                - Only valid values for mm are “00”, “10”, “20”, “30”, “40”, “50”.

                - To get the entire third hour worth of Match Ids, call getMatchIds() 6 times, specifying the following values for {hour}: “3,00”, “3,10”, “3,20”, “3,30”, “3,40”, “3,50”.
        """
        return self.__request_method__('getmatchidsbyqueue', MatchIdByQueue, 1, params=[queueId, self._createTimeStamp('%Y%m%d', False) if not date else date.strftime('%Y%m%d/%H,%M') if isinstance(date, datetime) else date, None if isinstance(date, datetime) else (format(hour, ',.2f').replace('.', ',') if isinstance(hour, float) and hour != -1 else hour)])

    # GET /getplayerachievements[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerId}
    def getPlayerAchievements(self, playerId):
        """Returns select achievement totals for the specified playerId.

        Parameters
        ----------
        playerId : |INT|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('getplayerachievements', PlayerAcheviements, params=[playerId])

    # GET /getplayeridbyname[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerName}
    # GET /getplayeridbyportaluserid[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{portalId}/{portalUserId}
    # GET /getplayeridsbygamertag[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{portalId}/{gamerTag}
    def getPlayerId(self, playerName, portalId=None):
        """Function returns a list of Hi-Rez playerId values.

        Parameters
        ----------
        playerName : |INT| or |STR|
            Function returns a list of Hi-Rez playerId values (expected list size = 1) for playerName provided.
        portalId : Optional |INT| or :class:`pyrez.enumerations.PortalId`
            Only returns a list of Hi-Rez playerId values for portalId provided. (Defaults to |NONE|)

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        if not portalId:
            mthd_name = 'getplayeridbyname'
            params = [playerName]
        else:
            mthd_name = 'getplayeridbyportaluserid' if str(playerName).isnumeric() else 'getplayeridsbygamertag'
            params = [portalId, playerName]
        return self.__request_method__(mthd_name, PlayerId, 1, params=params)

    # GET /getplayerstatus[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerId}
    def getPlayerStatus(self, playerId):
        """
        Returns player status as follows:
            - 0: Offline,
            - 1: In Lobby,
            - 2: God Selection,
            - 3: In Game,
            - 4: Online,
            - 5: Player not found

        Parameters
        ----------
        playerId : |INT|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
        pyrez.models.PlayerStatus
            Object of pyrez.models.PlayerStatus containing player status
        """
        return self.__request_method__('getplayerstatus', PlayerStatus, params=[playerId])

    # GET /getqueuestats[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerId}/{queueId}
    def getQueueStats(self, playerId, queueId):
        """Returns match summary statistics for a (player, queue) combination grouped by gods played.

        Parameters
        ----------
        playerId : |INT|
        queueId : |INT|

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('getqueuestats', QueueStats, 1, params=[playerId, queueId])

    # GET /searchplayers[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{searchPlayer}
    def searchPlayers(self, playerName):
        """
        Parameters
        ----------
        playerName : |STR|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('searchplayers', Player, 1, params=[playerName])
