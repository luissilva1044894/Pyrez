from datetime import datetime
from hashlib import md5

from pyrez.enumerations import Format, Language
from pyrez.exceptions import DailyLimit, IdOrAuthEmpty, InvalidArgument, LiveMatchException, NoResult, NotFound, NotSupported, PlayerNotFound, RequestError, SessionLimit, UnexpectedException, WrongCredentials
from pyrez.events import Event
from pyrez.models import APIResponse, DataUsed, Friend, LiveMatch, Match, MatchHistory, MatchId as MatchIdByQueue, PatchInfo, Ping, Player, PlayerId, PlayerAcheviements, PlayerStatus, QueueStats, ServerStatus, Session
#from pyrez.models.Smite import Player as SmitePlayer, Item as SmiteItem, TopMatch as SmiteTopMatch, God, GodLeaderboard, GodRank, GodRecommendedItem, GodSkin
#from pyrez.models.Smite.Team import Player as TeamPlayer, Search as TeamSearch, Info as TeamDetail
from .API import API
from .StatusPage import StatusPage
class APIBase(API):
    """
    Class for handling connections and requests to Hi-Rez Studios' APIs. IS BETTER DON'T INITALISE THIS YOURSELF!
    """
    def __init__(self, devId, authKey, endpoint, responseFormat=Format.JSON, sessionId=None, storeSession=False):
        """
        The constructor for HiRezAPI class.
        Keyword arguments/Parameters:
            devId [int]: Used for authentication. This is the devId that you receive from Hi-Rez Studios.
            authKey [str]: Used for authentication. This is the authKey that you receive from Hi-Rez Studios.
            endpoint [str]: The endpoint that you want to access to retrieve information from the Hi-Rez Studios' APIs.
            responseFormat [pyrez.enumerations.Format]: The response format that will be used by default when making requests (default pyrez.enumerations.Format.JSON)
            sessionId [str]: An active sessionId (default None)
            storeSession [bool]: (default False)
        """
        super().__init__()
        if not devId or not authKey:
            raise IdOrAuthEmpty("DevId or AuthKey not specified!")
        if len(str(devId)) != 4 or not str(devId).isnumeric():
            raise InvalidArgument("You need to pass a valid DevId!")
        if len(str(authKey)) != 32 or not str(authKey).isalnum():
            raise InvalidArgument("You need to pass a valid AuthKey!")
        if not endpoint:
            raise InvalidArgument("Endpoint can't be empty!")
        self._devId = int(devId)
        self._authKey = str(authKey)
        self._endpointBaseURL = str(endpoint)
        self._responseFormat = Format(responseFormat) if isinstance(responseFormat, Format) else Format.JSON
        self.storeSession = storeSession
        self.onSessionCreated = Event()
        self.currentSessionId = sessionId if sessionId else self._getSession() #if sessionId and self.testSession(sessionId)
        self.statusPage = StatusPage() #make all endpoints return just the atual game incidents
    @classmethod
    def _getSession(cls):
        import json
        import os
        try:
            with open("{}/session.json".format(os.path.dirname(os.path.abspath(__file__))), 'r', encoding="utf-8") as sessionJson:
                return Session(**json.load(sessionJson)).sessionId
        except (FileNotFoundError, ValueError):
            return None
    def __setSession(self, session):
        import os
        self.currentSessionId = session.sessionId
        if self.storeSession and session:
            with open("{}/session.json".format(os.path.dirname(os.path.abspath(__file__))), 'w', encoding="utf-8") as sessionJson:
                sessionJson.write(str(session.json).replace("'", "\""))
    @classmethod
    def _createTimeStamp(cls, timeFormat="%Y%m%d%H%M", addZero=True):
        """
        Keyword arguments/Parameters:
            timeFormat [str]: Format of timeStamp (%Y%m%d%H%M%S)
        Returns:
            Returns the current UTC time (GMT+0) formatted to 'YYYYMMDDHHmmss'
        """
        return cls._getCurrentTime().strftime(timeFormat) + ("00" if addZero else "")
    @classmethod
    def _getCurrentTime(cls):
        """
        Returns:
            Returns the current UTC time (GMT+0).
        """
        return datetime.utcnow()
    def _createSignature(self, methodName, timestamp=None):
        """
        Actually the authKey isn't passed directly, but instead embedded and hashed as MD5 Signature.
        Signatures use 4 items to be created: devId, authKey, methodName (without the Response Format), and timestamp.
        Keyword arguments/Parameters:
            methodName [str]: Method name
            timestamp [str]: Current timestamp
        Returns:
            Returns a MD5 hash string of (devId + methodName + authKey + timestamp)
        """
        return md5(self._encode("{}{}{}{}".format(self._devId, methodName.lower(), self._authKey, timestamp if timestamp else self._createTimeStamp()))).hexdigest()
    def _sessionExpired(self):
        return not self.currentSessionId or not str(self.currentSessionId).isalnum()
    def _buildUrlRequest(self, apiMethod=None, params=()):
        from enum import Enum
        if not apiMethod:
            raise InvalidArgument("No API method specified!")
        urlRequest = "{}/{}{}".format(self._endpointBaseURL, apiMethod.lower(), self._responseFormat)
        if apiMethod.lower() != "ping":
            urlRequest += "/{}/{}".format(self._devId, self._createSignature(apiMethod.lower()))
            if self.currentSessionId and apiMethod.lower() != "createsession":
                if apiMethod.lower() == "testsession":
                    return urlRequest + "/{}/{}".format(str(params[0]), self._createTimeStamp())
                urlRequest += "/{}".format(self.currentSessionId)
            urlRequest += "/{}{}".format(self._createTimeStamp(), "/{}".format('/'.join(param.strftime("yyyyMMdd") if isinstance(param, datetime) else str(param.value) if isinstance(param, Enum) else str(param) for param in params if param)) if params else "")
        return urlRequest.replace(' ', "%20")
    @classmethod
    def _checkErrorMsg(cls, errorMsg):
        if errorMsg.find("dailylimit") != -1:
            raise DailyLimit("Daily limit reached: {}".format(errorMsg))
        if errorMsg.find("Maximum number of active sessions reached") != -1:
            raise SessionLimit("Concurrent sessions limit reached: {}".format(errorMsg))
        if errorMsg.find("Exception while validating developer access") != -1:
            raise WrongCredentials("Wrong credentials: {}".format(errorMsg))
        if errorMsg.find("No match_queue returned.  It is likely that the match wasn't live when GetMatchPlayerDetails() was called") != -1:
            raise LiveMatchException("Match isn't live: {}".format(errorMsg))
        if errorMsg.find("Only training queues") != -1 and errorMsg.find("are supported for GetMatchPlayerDetails()") != -1:
            raise LiveMatchException("Queue not supported by getLiveMatchDetails(): {}".format(errorMsg))
        if errorMsg.find("The server encountered an error processing the request") != -1:
            raise RequestError("The server encountered an error processing the request: {}".format(errorMsg))
        if errorMsg.find("404") != -1:
            raise NotFound("{}".format(errorMsg))
    def makeRequest(self, apiMethod=None, params=()):
        if not apiMethod:
            raise InvalidArgument("No API method specified!")
        if(apiMethod.lower() != "createsession" and self._sessionExpired()):
            self._createSession()
        result = self._httpRequest(apiMethod if str(apiMethod).lower().startswith("http") else self._buildUrlRequest(apiMethod, params))
        if result:
            if self._responseFormat.equal(Format.XML):
                return result
            if str(result).lower().find("ret_msg") == -1:
                return None if len(str(result)) == 2 and str(result) == "[]" else result
            hasError = APIResponse(**result if str(result).startswith('{') else result[0])
            if hasError and hasError.hasError():
                if hasError.errorMsg == "Approved":
                    session = Session(**result)
                    self.__setSession(session)
                    if self.onSessionCreated.hasHandlers():
                        self.onSessionCreated(session)
                elif hasError.errorMsg.find("Invalid session id") != -1:
                    self._createSession()
                    return self.makeRequest(apiMethod, params)
                else:
                    self._checkErrorMsg(hasError.errorMsg)
            return result
    def switchEndpoint(self, endpoint):
        if not isinstance(endpoint, Endpoint):
            raise InvalidArgument("You need to use the Endpoint enum to switch endpoints")
        self._endpointBaseURL = str(endpoint)
    def _createSession(self):
        """
        /createsession[Format]/{devId}/{signature}/{timestamp}
        A required step to Authenticate the devId/signature for further API use.
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, Format.JSON
        _ = self.makeRequest("createsession")
        self._responseFormat = tempResponseFormat
        return Session(**_) if _ else None
    def ping(self):
        """
        /ping[ResponseFormat]
            A quick way of validating access to the Hi-Rez API.
        Returns:
            Object of pyrez.models.Ping: Returns the infos about the API.
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, Format.JSON
        _ = self.makeRequest("ping")
        self._responseFormat = tempResponseFormat
        return Ping(_) if _ else None
    def testSession(self, sessionId=None):
        """
        /testsession[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            A means of validating that a session is established.
        Keyword arguments/Parameters:
            sessionId [str]: A sessionId to validate
        Returns:
            Returns a boolean that means if a sessionId is valid.
        """
        session = self.currentSessionId if not sessionId or not str(sessionId).isalnum() else sessionId
        uri = "{}/testsession{}/{}/{}/{}/{}".format(self._endpointBaseURL, self._responseFormat, self._devId, self._createSignature("testsession"), session, self._createTimeStamp())
        _ = self._httpRequest(uri)
        return _.find("successful test") != -1
    def getDataUsed(self):
        """
        /getdataused[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Returns API Developer daily usage limits and the current status against those limits.
        Returns:
            Returns a pyrez.models.DataUsed object containing resources used.
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, Format.JSON
        _ = self.makeRequest("getdataused")
        self._responseFormat = tempResponseFormat
        return DataUsed(**_) if str(_).startswith('{') else DataUsed(**_[0]) if _ else None
    def getServerStatus(self):
        """
        /gethirezserverstatus[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Function returns UP/DOWN status for the primary game/platform environments. Data is cached once a minute.
        Returns:
            Object of pyrez.models.HiRezServerStatus
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, Format.JSON
        _ = self.makeRequest("gethirezserverstatus")
        self._responseFormat = tempResponseFormat
        __ = [ ServerStatus(**___) for ___ in (_ if _ else []) ]
        return (__ if len(__) > 1 else __[0]) if __ else None
    def getItems(self, language=Language.English):
        _ = self.makeRequest("getitems", [language])
        return None if self._responseFormat.equal(Format.XML) or not _ else _
    def getPatchInfo(self):
        """
        /getpatchinfo[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Function returns information about current deployed patch. Currently, this information only includes patch version.
        Returns:
            Object of pyrez.models.PatchInfo
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, Format.JSON
        _ = self.makeRequest("getpatchinfo")
        self._responseFormat = tempResponseFormat
        return PatchInfo(**_) if _ else None
    def getFriends(self, playerId):
        """
        /getfriends[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
            Returns the User names of each of the player’s friends of one player. [PC only]
        Returns:
            List of pyrez.models.Friend objects
        """
        _ = self.makeRequest("getfriends", [playerId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ Friend(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getMatch(self, matchId, isLive=False):
        """
        /getmatchdetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{matchId}
        /getmatchdetailsbatch[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{matchId,matchId,matchId,...matchId}
        /getmatchplayerdetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{matchId}
            Returns the player information / statistics for a particular match.
        Keyword arguments/Parameters:
            matchId [int]:
            isLive [bool]:
        """
        _ = self.makeRequest("getmatchdetailsbatch", [','.join(matchId)]) if isinstance(matchId, (type(()), type([]))) else self.makeRequest("getmatchplayerdetails" if isLive else "getmatchdetails", [matchId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ LiveMatch(**___) if isLive else Match(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getMatchHistory(self, playerId):
        """
        /getmatchhistory[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
            Gets recent matches and high level match statistics for a particular player.
        Keyword arguments/Parameters:
            playerId [int]:
        """
        _ = self.makeRequest("getmatchhistory", [playerId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ MatchHistory(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getMatchIds(self, queueId, date=None, hour=-1):
        """
        /getmatchidsbyqueue[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queue}/{date}/{hour}
            Lists all Match IDs for a particular Match Queue; useful for API developers interested in constructing data by Queue.
            To limit the data returned, an {hour} parameter was added (valid values: 0 - 23).
            An {hour} parameter of -1 represents the entire day, but be warned that this may be more data than we can return for certain queues.
            Also, a returned “active_flag” means that there is no match information/stats for the corresponding match.
            Usually due to a match being in-progress, though there could be other reasons.
        Keyword arguments/Parameters:
            queueId [int]:
            date [int]:
            hour [int]:
        NOTE:
            To avoid HTTP timeouts in the GetMatchIdsByQueue() method, you can now specify a 10-minute window within the specified {hour} field to lessen the size of data returned by appending a “,mm” value to the end of {hour}.
            For example, to get the match Ids for the first 10 minutes of hour 3, you would specify {hour} as “3,00”.
            This would only return the Ids between the time 3:00 to 3:09.
            Rules below:
                Only valid values for mm are “00”, “10”, “20”, “30”, “40”, “50”
                To get the entire third hour worth of Match Ids, call GetMatchIdsByQueue() 6 times, specifying the following values for {hour}: “3,00”, “3,10”, “3,20”, “3,30”, “3,40”, “3,50”.
                The standard, full hour format of {hour} = “hh” is still supported.
        """
        _ = self.makeRequest("getmatchidsbyqueue", [queueId, self._createTimeStamp("%Y%m%d", False) if not date else date.strftime("%Y%m%d/%H,%M") if isinstance(date, datetime) else date, None if isinstance(date, datetime) else (format(hour, ",.2f").replace('.', ',') if isinstance(hour, float) and hour != -1 else hour)])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ MatchIdByQueue(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getPlayer(self, player, portalId=None):
        """
        /getplayer[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{player}
        /getplayer[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{player}/{portalId}
            Returns league and other high level data for a particular player.

        This method can be used in two different ways:
            getPlayer(player)
            getPlayer(player, portalId)
        Keyword arguments / Parameters
        ------------------------------
            player: [:class:`str`] | [:class:`int`]: playerName or playerId of the player you want to get info on
            portalId: Optional[:class:`int`] | [:class:`pyrez.models.PortalId`]: The portalId that you want to looking for (Defaults to ``None``)
        Raises
        ------------------------------
            pyrez.exceptions.DailyLimitException:
                Daily request limit reached
            pyrez.exceptions.WrongCredentials:
                The wrong credentials are passed.
            pyrez.exceptions.NotFoundException:
                The wrong params are passed.
            TypeError:
                More than 2 parameters or less than 1 parameter passed.
        Returns
        ------------------------------
            pyrez.models.PlayerSmite | pyrez.models.PlayerPaladins object with league and other high level data for a particular player.
        """
        _ = self.makeRequest("getplayer", [player, portalId] if portalId else [player])
        return None if self._responseFormat.equal(Format.XML) or not _ else _
    def getPlayerAchievements(self, playerId):
        """
        /getplayerachievements[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
            Returns select achievement totals (Double kills, Tower Kills, First Bloods, etc) for the specified playerId.
        Keyword arguments/Parameters:
            playerId [int]:
        """
        _ = self.makeRequest("getplayerachievements", [playerId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        return PlayerAcheviements(**_) if str(_).startswith('{') else PlayerAcheviements(**_[0])
    def getPlayerId(self, playerName, portalId=None):
        """
        /getplayeridbyname[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{playerName}
            Function returns a list of Hi-Rez playerId values (expected list size = 1) for playerName provided. The playerId returned is
            expected to be used in various other endpoints to represent the player/individual regardless of platform.
        /getplayeridbyportaluserid[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{portalId}/{portalUserId}
            Function returns a list of Hi-Rez playerId values (expected list size = 1) for {portalId}/{portalUserId} combination provided.
            The playerId returned is expected to be used in various other endpoints to represent the player/individual regardless of platform.
        /getplayeridsbygamertag[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{portalId}/{gamerTag}
            Function returns a list of Hi-Rez playerId values for {portalId}/{portalUserId} combination provided. The appropriate
            playerId extracted from this list by the API end user is expected to be used in various other endpoints to represent the player/individual regardless of platform.
        Keyword arguments/Parameters:
            playerName [str] / [int]:
            portalId [int]:
        """
        _ = self.makeRequest("getplayeridbyname", [playerName]) if not portalId else self.makeRequest("getplayeridbyportaluserid" if str(playerName).isnumeric() else "getplayeridsbygamertag", [portalId, playerName])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ PlayerId(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getPlayerStatus(self, playerId):
        """
        /getplayerstatus[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        Returns player status as follows:
            0 - Offline, 1 - In Lobby, 2 - god Selection, 3 - In Game, 4 - Online, 5 - Player not found
        Keyword arguments/Parameters:
            playerId [int]:
        Returns:
            Object of pyrez.models.PlayerStatus
        """
        _ = self.makeRequest("getplayerstatus", [playerId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        return PlayerStatus(**_) if str(_).startswith('{') else PlayerStatus(**_[0])
    def getQueueStats(self, playerId, queueId):
        """
        /getqueuestats[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}/{queue}
            Returns match summary statistics for a (player, queue) combination grouped by gods played.
        Keyword arguments/Parameters:
            playerId [int]:
            queueId [int]:
        """
        _ = self.makeRequest("getqueuestats", [playerId, queueId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ QueueStats(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def searchPlayers(self, playerName):
        """
        /searchplayers[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerName}
        """
        _ = self.makeRequest("searchplayers", [playerName])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ Player(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
