
from datetime import datetime
import json
from hashlib import md5
import os

from pyrez.enumerations import (
    Format,
    Language,
)
from pyrez.exceptions import (
    DailyLimit,
    IdOrAuthEmpty,
    InvalidArgument,
    MatchException,
    NoResult,
    NotFound,
    NotSupported,
    PlayerNotFound,
    RequestError,
    SessionLimit,
    WrongCredentials,
    PrivatePlayer,
    #UnexpectedException,
)
from pyrez.events import Event
from pyrez.models import (
    APIResponse,
    DataUsed,
    Friend,
    LiveMatch,
    Match,
    MatchHistory,
    MatchId as MatchIdByQueue,
    PatchInfo,
    Ping,
    Player,
    PlayerId,
    PlayerAcheviements,
    PlayerStatus,
    QueueStats,
    ServerStatus,
    Session,
)
from .APIBase import APIBase
from .StatusPageAPI import StatusPageAPI
class API(APIBase):
    def __init__(self, devId, authKey, endpoint, responseFormat=Format.JSON, sessionId=None, storeSession=True, debug_mode=True):
        super().__init__(debug_mode=debug_mode)
        if not devId or not authKey:
            if self.debug_mode:
                self.logger.error('DevId or AuthKey not specified!')
            raise IdOrAuthEmpty("DevId or AuthKey not specified!")
        if len(str(devId)) != 4 or not str(devId).isnumeric():
            if self.debug_mode:
                self.logger.error('You need to pass a valid DevId!')
            raise InvalidArgument("You need to pass a valid DevId!")
        if len(str(authKey)) != 32 or not str(authKey).isalnum():
            if self.debug_mode:
                self.logger.error('You need to pass a valid AuthKey!')
            raise InvalidArgument("You need to pass a valid AuthKey!")
        if not endpoint:
            if self.debug_mode:
                self.logger.error("Endpoint can't be empty!")
            raise InvalidArgument("Endpoint can't be empty!")
        self.devId = int(devId)
        self.authKey = str(authKey).upper()
        self.__endpoint__ = str(endpoint)
        self._responseFormat = Format.JSON if not responseFormat or not isinstance(responseFormat, Format) else responseFormat
        self.storeSession = storeSession or False
        self.onSessionCreated = Event()
        self.sessionId = sessionId or self._getSession(devId=self.devId) #if sessionId and self.testSession(sessionId)
        self.statusPage = StatusPageAPI() #make all endpoints return just the atual game incidents
    @classmethod
    def _getSession(cls, idOnly=True, devId=None):
        try:
            with open("{}/{}.json".format(os.path.dirname(os.path.abspath(__file__)), devId or cls.devId), 'r', encoding="utf-8") as f:
                session = Session(**json.load(f))
                return session.sessionId if idOnly else session
        except (FileNotFoundError, ValueError):
            return None
    def __setSession(self, session, devId=None):
        self.sessionId = session.sessionId
        if self.storeSession and session:
            with open('{}/{}.json'.format(os.path.dirname(os.path.abspath(__file__)), devId or self.devId), 'w', encoding='utf-8') as f:
                f.write(json.dumps(session.json, sort_keys=True, ensure_ascii=True, indent=4))#f.write(str(session.json).replace("'", "\""))
    @classmethod
    def _createTimeStamp(cls, timeFormat="%Y%m%d%H%M", addZero=True):
        """
        Parameters
        ----------
        timeFormat : |STR|
            Format of timeStamp (%Y%m%d%H%M%S)
        addZero : |BOOL|
            Add 00 instead ``ss``

        Returns
        -------
        str
            Returns the current UTC time (GMT+0) formatted to ``YYYYMMDDHHmmss``
        """
        return cls._getCurrentTime().strftime(timeFormat) + ("00" if addZero else "")
    @classmethod
    def _getCurrentTime(cls):
        """
        Returns
        -------
        datetime
            Returns the current UTC time (GMT+0).
        """
        return datetime.utcnow()
    def _createSignature(self, methodName, timestamp=None):
        """Actually the authKey isn't passed directly, but instead embedded and hashed as MD5 Signature.

        Signatures use 4 items to be created: devId, authKey, methodName (without the Response Format), and timestamp.

        Parameters
        ----------
        methodName : |STR|
            Method name
        timestamp : |STR|
            Current timestamp

        Returns
        -------
        str
            Returns a MD5 hash code of the method (devId + methodName + authKey + timestamp)
        """
        return md5(self._encode("{}{}{}{}".format(self.devId, methodName.lower(), self.authKey, timestamp or self._createTimeStamp()))).hexdigest()
    def _sessionExpired(self):
        return not self.sessionId or not str(self.sessionId).isalnum()
    def _buildUrlRequest(self, apiMethod=None, params=()):
        if not apiMethod:
            raise InvalidArgument("No API method specified!")
        urlRequest = "{}/{}{}".format(self.__endpoint__, apiMethod.lower(), self._responseFormat)
        if apiMethod.lower() != "ping":
            urlRequest += "/{}/{}".format(self.devId, self._createSignature(apiMethod.lower()))
            if self.sessionId and apiMethod.lower() != "createsession":
                if apiMethod.lower() == "testsession":
                    return urlRequest + "/{}/{}".format(str(params[0]), self._createTimeStamp())
                urlRequest += "/{}".format(self.sessionId)
            urlRequest += "/{}{}".format(self._createTimeStamp(), "/{}".format('/'.join(param.strftime("yyyyMMdd") if hasattr(param, 'strftime') else str(param.value) if hasattr(param, 'value') else str(param) for param in params if param)) if params else "")
        return urlRequest.replace(' ', "%20")
    @classmethod
    def _checkErrorMsg(cls, errorMsg):
        if errorMsg.find("Player Privacy Flag") != -1:
            raise PrivatePlayer(errorMsg)
        if errorMsg.find("dailylimit") != -1:
            raise DailyLimit(errorMsg)
        if errorMsg.find("No match_queue returned.  It is likely that the match wasn't live when GetMatchPlayerDetails() was called") != -1:
            raise MatchException(errorMsg)
        if errorMsg.find("No Match History") != -1:
            raise MatchException(errorMsg)
        if errorMsg.find("Only training queues") != -1 and errorMsg.find("are supported for GetMatchPlayerDetails()") != -1:
            raise MatchException(errorMsg)
        if errorMsg.find("404") != -1:
            raise NotFound(errorMsg)
        if errorMsg.find("The server encountered an error processing the request") != -1:
            raise RequestError(errorMsg)
        if errorMsg.find("Maximum number of active sessions reached") != -1:
            raise SessionLimit(errorMsg)
        if errorMsg.find("Exception while validating developer access") != -1:
            raise WrongCredentials(errorMsg)
    def makeRequest(self, apiMethod=None, params=()):
        """Construct and make a HTTP request to Hi-Rez Studios API.

        Parameters
        ----------
        apiMethod : |STR|
        params : Optional: |LIST| or |TUPLE|

        Raises
        -------
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
        if not apiMethod:
            raise InvalidArgument("No API method specified!")
        if not apiMethod.lower() in ["createsession", "ping", "testsession"] and self._sessionExpired():
            self._createSession()
        result = self._httpRequest(apiMethod if str(apiMethod).lower().startswith("http") else self._buildUrlRequest(apiMethod, params))
        if result:
            if self._responseFormat.equal(Format.XML) or str(result).lower().find("ret_msg") == -1:
                return None if len(str(result)) == 2 and str(result) == "[]" else result
            hasError = APIResponse(**result if str(result).startswith('{') else result[0])
            if hasError and hasError.hasError:
                if hasError.errorMsg.find("Invalid session id") != -1:
                    if self.debug_mode:
                        self.logger.debug('{} ({})'.format(hasError.errorMsg, self.sessionId))
                    self._createSession()
                    return self.makeRequest(apiMethod, params)
                if hasError.errorMsg == "Approved":
                    session = Session(**result)
                    if self.debug_mode:
                        self.logger.debug('{}: (Old session: {}, new session: {})'.format(hasError.errorMsg, self.sessionId, session.sessionId))
                    self.__setSession(session)
                    if self.onSessionCreated.hasHandlers():
                        self.onSessionCreated(session)
                else:
                    try:
                        self._checkErrorMsg(hasError.errorMsg)
                    except PrivatePlayer:
                        if str(apiMethod).lower() == 'getplayer':
                            raise
        return result
    def switchEndpoint(self, endpoint):
        if not isinstance(endpoint, Endpoint):
            raise InvalidArgument("You need to use the Endpoint enum to switch endpoints")
        self._endpointBaseURL = str(endpoint)

    # GET /createsession[ResponseFormat]/{devId}/{signature}/{timestamp}
    def _createSession(self):
        """A required step to Authenticate the devId/signature for further API use.

        Raises
        -------
        TypeError
            |TypeError|

        NOTE
        -----
            This method raises :meth:`makeRequest` exceptions.
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, Format.JSON
        _ = self.makeRequest("createsession")
        self._responseFormat = tempResponseFormat
        return Session(**_) if _ else None

    # GET /ping[ResponseFormat]
    def ping(self):
        """A quick way of validating access (establish connectivity) to the Hi-Rez API.

        You do not need to authenticate your ID or key to do this.

        Raises
        -------
        TypeError
            |TypeError|

        NOTE
        -----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
        :class:`pyrez.models.Ping`
            Returns a :class:`pyrez.models.Ping` objects containing infos about the API.
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, Format.JSON
        _ = self.makeRequest("ping")
        self._responseFormat = tempResponseFormat
        return Ping(_) if _ else None

    # GET /testsession[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}
    def testSession(self, sessionId=None):
        """A means of validating that a session is established.

        Parameters
        ----------
        sessionId : Optional |STR|
            A sessionId to validate. Passing in ``None`` will use :attr:`.sessionId` instead of the passed in value.

        Raises
        -------
        TypeError
            |TypeErrorA|

        NOTE
        -----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
        |BOOL|
            Returns a |BOOL| that means if the passed sessionId is valid.
        """
        session = self.sessionId if not sessionId or not str(sessionId).isalnum() else sessionId
        uri = "{}/testsession{}/{}/{}/{}/{}".format(self.__endpoint__, self._responseFormat, self.devId, self._createSignature("testsession"), session, self._createTimeStamp())
        _ = self._httpRequest(uri)
        return _.find("successful test") != -1

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
        tempResponseFormat, self._responseFormat = self._responseFormat, Format.JSON
        _ = self.makeRequest("getdataused")
        self._responseFormat = tempResponseFormat
        return DataUsed(**_) if str(_).startswith('{') else DataUsed(**_[0]) if _ else None

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
        tempResponseFormat, self._responseFormat = self._responseFormat, Format.JSON
        _ = self.makeRequest("gethirezserverstatus")
        self._responseFormat = tempResponseFormat
        __ = [ ServerStatus(**___) for ___ in (_ or []) ]
        return (__ if len(__) > 1 else __[0]) if __ else None

    # GET /getitems[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{languageCode}
    def getItems(self, language=Language.English):
        """
        Parameters
        ----------
        language : |LanguageParam|
            |LanguageParamDescrip|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        _ = self.makeRequest("getitems", [language or Language.English])
        return None if self._responseFormat.equal(Format.XML) or not _ else _

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
        tempResponseFormat, self._responseFormat = self._responseFormat, Format.JSON
        _ = self.makeRequest("getpatchinfo")
        self._responseFormat = tempResponseFormat
        return PatchInfo(**_) if _ else None

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
        _ = self.makeRequest("getfriends", [playerId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ Friend(**___) for ___ in (_ or []) if ___.get("player_id", "0") != "0" ]
        return __ or None

    # GET /getmatchdetails[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{matchId}
    # GET /getmatchdetailsbatch[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{matchId,matchId,matchId,...matchId}
    # GET /getmatchplayerdetails[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{matchId}
    def getMatch(self, matchId, isLiveMatch=False):
        """Returns the player information / statistics for a particular match.

        There is three ways to call this method::

            getMatch(matchId)
            #or
            getMatch([matchId, matchId, matchId])
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
        _sorted = 'sorted' if isinstance(matchId, (tuple, list)) and isLiveMatch else ''
        _ = self.makeRequest('{}{}'.format("getmatchdetailsbatch", _sorted), [','.join(matchId)]) if isinstance(matchId, (type(()), type([]))) else self.makeRequest("getmatchplayerdetails" if isLiveMatch else "getmatchdetails", [matchId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ LiveMatch(**___) if isLiveMatch else Match(**___) for ___ in (_ or []) ] if not _sorted else _ or []
        return __ or None

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
        _ = self.makeRequest("getmatchhistory", [playerId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ MatchHistory(**___) for ___ in (_ or []) ]
        return __ or None

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

            This would only return the Ids between the time 3:00 to 3:09.
            Rules below:
                Only valid values for mm are “00”, “10”, “20”, “30”, “40”, “50”.

                To get the entire third hour worth of Match Ids, call getMatchIds() 6 times, specifying the following values for {hour}: “3,00”, “3,10”, “3,20”, “3,30”, “3,40”, “3,50”.
        """
        _ = self.makeRequest("getmatchidsbyqueue", [queueId, self._createTimeStamp("%Y%m%d", False) if not date else date.strftime("%Y%m%d/%H,%M") if isinstance(date, datetime) else date, None if isinstance(date, datetime) else (format(hour, ",.2f").replace('.', ',') if isinstance(hour, float) and hour != -1 else hour)])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ MatchIdByQueue(**___) for ___ in (_ or []) ]
        return __ or None

    # GET /getplayer[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerIdOrName}
    # GET /getplayer[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerIdOrName}/{portalId}
    def getPlayer(self, player, portalId=None):
        """Returns league and other high level data for a particular player.

        Parameters
        ----------
        player : |INT| or |STR|
            playerName or playerId of the player you want to get info on
        portalId : Optional |INT| or :class:`pyrez.enumerations.PortalId`
            The portalId that you want to looking for (Defaults to |NONE|)

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
            pyrez.models.PlayerSmite | pyrez.models.PlayerPaladins object with league and other high level data for a particular player.

        """
        _ = self.makeRequest("getplayer", [player, portalId] if portalId else [player])
        return None if self._responseFormat.equal(Format.XML) or not _ else _

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
        _ = self.makeRequest("getplayerachievements", [playerId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        return PlayerAcheviements(**_) if str(_).startswith('{') else PlayerAcheviements(**_[0])

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
        _ = self.makeRequest("getplayeridbyname", [playerName]) if not portalId else self.makeRequest("getplayeridbyportaluserid" if str(playerName).isnumeric() else "getplayeridsbygamertag", [portalId, playerName])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ PlayerId(**___) for ___ in (_ or []) ]
        return __ or None

    # GET /getplayerstatus[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerId}
    def getPlayerStatus(self, playerId):
        """Returns player status as follows:
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
        _ = self.makeRequest("getplayerstatus", [playerId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        return PlayerStatus(**_) if str(_).startswith('{') else PlayerStatus(**_[0])

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
        _ = self.makeRequest("getqueuestats", [playerId, queueId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ QueueStats(**___) for ___ in (_ or []) ]
        return __ or None

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
        _ = self.makeRequest("searchplayers", [playerName])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ Player(**___) for ___ in (_ or []) ]
        return __ or None
