import configparser
from datetime import datetime
from hashlib import md5 as getMD5Hash
from json.decoder import JSONDecodeError as JSONException
import os
from sys import version_info as pythonVersion

import requests

import pyrez
from pyrez.enumerations import *
from pyrez.exceptions import *
from pyrez.models import *
from pyrez.events import *

class BaseAPI:
    """
    DON'T INITALISE THIS YOURSELF!
    Attributes:
        _devId [int]: Used for authentication. This is the devId that you receive from Hi-Rez Studios.
        _authKey [str]: Used for authentication. This is the authKey that you receive from Hi-Rez Studios.
        _endpointBaseURL [str]: The endpoint that you want to access to retrieve information from the Hi-Rez Studios' APIs.
        _responseFormat [pyrez.enumerations.ResponseFormat]: The response format that will be used by default when making requests (default pyrez.enumerations.ResponseFormat.JSON)
        _header [str]:
    Methods:
        __init__(devId, authKey, endpoint, responseFormat=pyrez.enumerations.ResponseFormat.JSON, header=None)
        _encode(string, encodeType="utf-8")
        _httpRequest(url, header=None)
        _saveConfigIni(sessionId)
        _readConfigIni()
    """
    def __init__(self, devId, authKey, endpoint, responseFormat=ResponseFormat.JSON, header=None):
        """
        The constructor for BaseAPI class.
        Keyword arguments/Parameters:
            devId [int]: Used for authentication. This is the devId that you receive from Hi-Rez Studios.
            authKey [str]: Used for authentication. This is the authKey that you receive from Hi-Rez Studios.
            endpoint [str]: The endpoint that you want to access to retrieve information from the Hi-Rez Studios' APIs.
            responseFormat [pyrez.enumerations.ResponseFormat]: The response format that will be used by default when making requests (default pyrez.enumerations.ResponseFormat.JSON)
            header:
        """
        if devId is None or authKey is None:
            raise IdOrAuthEmptyException("DevId or AuthKey not specified!")
        if len(str(devId)) != 4 or not str(devId).isnumeric():
            raise InvalidArgumentException("You need to pass a valid DevId!")
        if len(str(authKey)) != 32 or not str(authKey).isalnum():
            raise InvalidArgumentException("You need to pass a valid AuthKey!")
        if endpoint is None:
            raise InvalidArgumentException("Endpoint can't be empty!")
        self._devId = int(devId)
        self._authKey = str(authKey)
        self._endpointBaseURL = str(endpoint)
        self._responseFormat = ResponseFormat(responseFormat) if isinstance(responseFormat, ResponseFormat) else ResponseFormat.JSON
        self._header = header
    @classmethod
    def _encode(cls, string, encodeType="utf-8"):
        """
        Keyword arguments/Parameters:
            string [str]:
            encodeType [str]:
        Returns:
            String encoded to format type
        """
        return str(string).encode(encodeType)
    @classmethod
    def _httpRequest(cls, url, method="GET", params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allowRedirects=False, proxies=None, hooks=None, stream=False, verify=None, cert=None):
        defaultHeaders = { "user-agent": "HttpRequestWrapper [Python/{0.major}.{0.minor} requests/{1}]".format(pythonVersion, requests.__version__) }
        hdrs = headers if headers else defaultHeaders
        httpResponse = requests.request(method=method, url=url.replace(' ', '%20'), params=params, data=data, headers=hdrs, cookies=cookies, files=files, auth=auth, timeout=timeout, allow_redirects=allowRedirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert)
        if httpResponse.status_code >= 400:
            raise NotFoundException("Wrong URL: {0}".format(httpResponse.text))
        try:
            return httpResponse.json()
        except JSONException:
            return httpResponse.text
class HiRezAPI(BaseAPI):
    """
    Class for handling connections and requests to Hi-Rez Studios' APIs. IS BETTER DON'T INITALISE THIS YOURSELF!
    """
    PYREZ_HEADER = { "user-agent": "{0} [Python/{1.major}.{1.minor} requests/{2}]".format(pyrez.__title__, pythonVersion, requests.__version__) }
    def __init__(self, devId, authKey, endpoint, responseFormat=ResponseFormat.JSON, sessionId=None, useConfigIni=False):
        """
        The constructor for HiRezAPI class.
        Keyword arguments/Parameters:
            devId [int]: Used for authentication. This is the devId that you receive from Hi-Rez Studios.
            authKey [str]: Used for authentication. This is the authKey that you receive from Hi-Rez Studios.
            endpoint [str]: The endpoint that you want to access to retrieve information from the Hi-Rez Studios' APIs.
            responseFormat [pyrez.enumerations.ResponseFormat]: The response format that will be used by default when making requests (default pyrez.enumerations.ResponseFormat.JSON)
            sessionId [str]: An active sessionId (default None)
            useConfigIni [bool]: (default False)
        """
        super().__init__(devId, authKey, endpoint, responseFormat, self.PYREZ_HEADER)
        self.useConfigIni = useConfigIni
        self.onSessionCreated = Event()
        if self.useConfigIni:
            self.__setSession(self._readConfigIni())
        else:
            self.__setSession(sessionId if sessionId and self.testSession(sessionId) else None)
    @classmethod
    def __getConfigIniFile(cls):
        conf = configparser.ConfigParser()#SafeConfigParser
        conf.read("{0}/conf.ini".format(os.path.dirname(os.path.abspath(__file__))))
        return conf if conf else None
    @classmethod
    def _saveConfigIni(cls, sessionId):
        conf = cls.__getConfigIniFile()
        if conf:
            try:
                conf.set("Session", "SessionId", str(sessionId))
            except (configparser.NoSectionError, configparser.NoOptionError):
                conf.add_section("Session")
                cls._saveConfigIni(sessionId)
            else:
                with open("{0}/conf.ini".format(os.path.dirname(os.path.abspath(__file__))), 'w') as configfile:
                    conf.write(configfile)
    @classmethod
    def _readConfigIni(cls):
        #https://docs.python.org/3/library/configparser.html
        conf = cls.__getConfigIniFile()
        if conf:
            try:
                keyValue = conf.get("Session", "SessionId")
            except (configparser.NoSectionError, configparser.NoOptionError, KeyError):
                return None
            else:
                return None if not keyValue or keyValue.lower()=="none" else keyValue
    @classmethod
    def _createTimeStamp(cls, timeFormat="%Y%m%d%H%M"):
        """
        Keyword arguments/Parameters:
            timeFormat [str]: Format of timeStamp (%Y%m%d%H%M%S)
        Returns:
            Returns the current UTC time (GMT+0) formatted to 'YYYYMMDDHHmmss'
        """
        return cls._getCurrentTime().strftime(timeFormat) + "00"
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
        return getMD5Hash(self._encode("{}{}{}{}".format(self._devId, methodName.lower(), self._authKey, timestamp if timestamp is not None else self._createTimeStamp()))).hexdigest()
    def _sessionExpired(self):
        return self.currentSessionId is None or not str(self.currentSessionId).isalnum()
    def _buildUrlRequest(self, apiMethod=None, params=()): # [queue, date, hour]
        if apiMethod is None:
            raise InvalidArgumentException("No API method specified!")
        urlRequest = "{}/{}{}".format(self._endpointBaseURL, apiMethod.lower(), self._responseFormat)
        if apiMethod.lower() != "ping":
            urlRequest += "/{}/{}".format(self._devId, self._createSignature(apiMethod.lower()))
            if self.currentSessionId is not None and apiMethod.lower() != "createsession":
                if apiMethod.lower() == "testsession":
                    return urlRequest + "/{}/{}".format(str(params[0]), self._createTimeStamp())
                urlRequest += "/{}".format(self.currentSessionId)
            urlRequest += "/{}".format(self._createTimeStamp())
            for param in params:
                if param is not None:
                    urlRequest += "/{0}".format(param.strftime("yyyyMMdd") if isinstance(param, datetime) else str(param.value) if isinstance(param, Enum) else str(param))
        return urlRequest.replace(' ', "%20")
    @classmethod
    def checkRetMsg(cls, retMsg):
        if retMsg.find("dailylimit") != -1:
            raise DailyLimitException("Daily limit reached: {}".format(retMsg))
        if retMsg.find("Maximum number of active sessions reached") != -1:
            raise SessionLimitException("Concurrent sessions limit reached: {}".format(retMsg))
        if retMsg.find("Exception while validating developer access") != -1:
            raise WrongCredentials("Wrong credentials: {}".format(retMsg))
        if retMsg.find("No match_queue returned.  It is likely that the match wasn't live when GetMatchPlayerDetails() was called") != -1:
            raise LiveMatchDetailsException("Match isn't live: {}".format(retMsg))
        if retMsg.find("Only training queues") != -1 and retMsg.find("are supported for GetMatchPlayerDetails()") != -1:
            raise LiveMatchDetailsException("Queue not supported by getLiveMatchDetails(): {}".format(retMsg))
        if retMsg.find("The server encountered an error processing the request") != -1:
            raise RequestErrorException("The server encountered an error processing the request: {}".format(retMsg))
        if retMsg.find("404") != -1:
            raise NotFoundException("{}".format(retMsg))
    def __setSession(self, sessionId):
        self.currentSessionId = sessionId
        if self.useConfigIni and sessionId:
            self._saveConfigIni(self.currentSessionId)
    def makeRequest(self, apiMethod=None, params=()):
        if apiMethod is None:
            raise InvalidArgumentException("No API method specified!")
        if(apiMethod.lower() != "createsession" and self._sessionExpired()):
            self._createSession()
        result = self._httpRequest(apiMethod if str(apiMethod).lower().startswith("http") else self._buildUrlRequest(apiMethod, params), headers=self.PYREZ_HEADER)
        if result:
            if self._responseFormat == ResponseFormat.XML:
                return result
            if str(result).lower().find("ret_msg") == -1:
                return None if len(str(result)) == 2 and str(result) == "[]" else result
            hasError = APIResponse(**result if str(result).startswith('{') else result[0])
            if hasError is not None and hasError.hasRetMsg():
                if hasError.retMsg == "Approved":
                    session = Session(**result)
                    self.__setSession(session.sessionId)
                    if self.onSessionCreated.hasHandlers():
                        self.onSessionCreated(session)
                elif hasError.retMsg.find("Invalid session id") != -1:
                    self._createSession()
                    return self.makeRequest(apiMethod, params)
                else:
                    self.checkRetMsg(hasError.retMsg)
            return result
    def switchEndpoint(self, endpoint):
        if not isinstance(endpoint, Endpoint):
            raise InvalidArgumentException("You need to use the Endpoint enum to switch endpoints")
        self._endpointBaseURL = str(endpoint)
    def _createSession(self):
        """
        /createsession[ResponseFormat]/{devId}/{signature}/{timestamp}
        A required step to Authenticate the devId/signature for further API use.
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, ResponseFormat.JSON
        response = self.makeRequest("createsession")
        self._responseFormat = tempResponseFormat
        return Session(**response) if response else None
    def ping(self):
        """
        /ping[ResponseFormat]
            A quick way of validating access to the Hi-Rez API.
        Returns:
            Object of pyrez.models.Ping: Returns the infos about the API.
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, ResponseFormat.JSON
        response = self.makeRequest("ping")
        self._responseFormat = tempResponseFormat
        return Ping(response) if response else None
    def testSession(self, sessionId=None):
        """
        /testsession[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            A means of validating that a session is established.
        Keyword arguments/Parameters:
            sessionId [str]: A sessionId to validate
        Returns:
            Returns a boolean that means if a sessionId is valid.
        """
        session = self.currentSessionId if sessionId is None or not str(sessionId).isalnum() else sessionId
        uri = "{0}/testsession{1}/{2}/{3}/{4}/{5}".format(self._endpointBaseURL, self._responseFormat, self._devId, self._createSignature("testsession"), session, self._createTimeStamp())
        result = self._httpRequest(uri, headers=self.PYREZ_HEADER)
        return result.find("successful test") != -1
    def getDataUsed(self):
        """
        /getdataused[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Returns API Developer daily usage limits and the current status against those limits.
        Returns:
            Returns a pyrez.models.DataUsed object containing resources used.
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, ResponseFormat.JSON
        response = self.makeRequest("getdataused")
        self._responseFormat = tempResponseFormat
        return DataUsed(**response) if str(response).startswith('{') else DataUsed(**response[0]) if response else None
    def getHiRezServerFeeds(self, fmr=ResponseFormat.JSON):
        req = self.makeRequest("http://status.hirezstudios.com/history.{0}".format(str(fmr)))
        return req
    def getHiRezServerStatus(self):
        """
        /gethirezserverstatus[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Function returns UP/DOWN status for the primary game/platform environments. Data is cached once a minute.
        Returns:
            Object of pyrez.models.HiRezServerStatus
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, ResponseFormat.JSON
        response = self.makeRequest("gethirezserverstatus")
        self._responseFormat = tempResponseFormat
        if response is None:
            return None
        servers = []
        for server in response:
            servers.append(HiRezServerStatus(**server))
        return servers if servers else None
    def getPatchInfo(self):
        """
        /getpatchinfo[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Function returns information about current deployed patch. Currently, this information only includes patch version.
        Returns:
            Object of pyrez.models.PatchInfo
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, ResponseFormat.JSON
        response = self.makeRequest("getpatchinfo")
        self._responseFormat = tempResponseFormat
        return PatchInfo(**response) if response is not None else None
    def getFriends(self, playerId):
        """
        /getfriends[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
            Returns the User names of each of the player’s friends of one player. [PC only]
        Returns:
            List of pyrez.models.Friend objects
        """
        response = self.makeRequest("getfriends", [playerId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        friends = []
        for friend in response:
            friends.append(Friend(**friend))
        return friends if friends else None
    def getMatchDetails(self, matchId):
        """
        /getmatchdetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{matchId}
            Returns the statistics for a particular completed match.
        Keyword arguments/Parameters:
            matchId [int]:
        """
        response = self.makeRequest("getmatchdetailsbatch", [','.join(matchId)]) if isinstance(matchId, (type(()), type([]))) else self.makeRequest("getmatchdetails", [matchId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        matchDetails = []
        for matchDetail in response:
            matchDetails.append(MatchDetail(**matchDetail))
        return matchDetails if matchDetails else None
    def getMatchHistory(self, playerId):
        """
        /getmatchhistory[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
            Gets recent matches and high level match statistics for a particular player.
        Keyword arguments/Parameters:
            playerId [int]:
        """
        response = self.makeRequest("getmatchhistory", [playerId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        matchHistorys = []
        for matchHistory in response:
            matchHistorys.append(MatchHistory(**matchHistory))
        return matchHistorys if matchHistorys else None
    def getMatchIdsByQueue(self, queueId, date, hour=-1):
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
        response = self.makeRequest("getmatchidsbyqueue", [queueId, date.strftime("%Y%m%d") if isinstance(date, datetime) else date, format(hour, ",.2f").replace('.', ',') if isinstance(hour, float) and hour != -1 else hour])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        matchIds = []
        for matchId in response:
            matchIds.append(MatchIdByQueue(**matchId))
        return matchIds if matchIds else None
    def getPlayerAchievements(self, playerId):
        """
        /getplayerachievements[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
            Returns select achievement totals (Double kills, Tower Kills, First Bloods, etc) for the specified playerId.
        Keyword arguments/Parameters:
            playerId [int]:
        """
        response = self.makeRequest("getplayerachievements", [playerId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        return PlayerAcheviements(**response) if str(response).startswith('{') else PlayerAcheviements(**response[0])
    def getPlayerIdByName(self, playerName):
        """
        /getplayeridbyname[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{playerName}
            Function returns a list of Hi-Rez playerId values (expected list size = 1) for playerName provided. The playerId returned is
            expected to be used in various other endpoints to represent the player/individual regardless of platform.
        Keyword arguments/Parameters:
            playerName [str]:
        """
        response = self.makeRequest("getplayeridbyname", [playerName])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        playerIds = []
        for playerId in response:
            playerIds.append(PlayerIdByX(**playerId))
        return playerIds if playerIds else None
    def getPlayerIdByPortalUserId(self, portalId, portalUserId):
        """
        /getplayeridbyportaluserid[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{portalId}/{portalUserId}
            Function returns a list of Hi-Rez playerId values (expected list size = 1) for {portalId}/{portalUserId} combination provided.
            The playerId returned is expected to be used in various other endpoints to represent the player/individual regardless of platform.
        Keyword arguments/Parameters:
            portalId [int]:
            portalUserId [int]:
        """
        response = self.makeRequest("getplayeridbyportaluserid", [portalId, portalUserId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        playerIds = []
        for playerId in response:
            playerIds.append(PlayerIdByX(**playerId))
        return playerIds if playerIds else None
    def getPlayerIdsByGamerTag(self, gamerTag, portalId):
        """
        /getplayeridsbygamertag[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{portalId}/{gamerTag}
            Function returns a list of Hi-Rez playerId values for {portalId}/{portalUserId} combination provided. The appropriate
            playerId extracted from this list by the API end user is expected to be used in various other endpoints to represent the player/individual regardless of platform.
        Keyword arguments/Parameters:
            gamerTag [str]:
        """
        response = self.makeRequest("getplayeridsbygamertag", [portalId, gamerTag])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        playerIds = []
        for playerId in response:
            playerIds.append(PlayerIdByX(**playerId))
        return playerIds if playerIds else None
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
        response = self.makeRequest("getplayerstatus", [playerId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        return PlayerStatus(**response) if str(response).startswith('{') else PlayerStatus(**response[0])
    def getQueueStats(self, playerId, queueId):
        """
        /getqueuestats[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}/{queue}
            Returns match summary statistics for a (player, queue) combination grouped by gods played.
        Keyword arguments/Parameters:
            playerId [int]:
            queueId [int]:
        """
        response = self.makeRequest("getqueuestats", [playerId, queueId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        queueStatsList = []
        for queueStat in response:
            queueStatsList.append(QueueStats(**queueStat))
        return queueStatsList if queueStatsList else None
    def searchPlayers(self, playerName):
        """
        /searchplayers[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerName}
        """
        response = self.makeRequest("searchplayers", [playerName])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        players = []
        for player in response:
            obj = Player(**player)
            players.append(obj)
        return players if players else None
class BaseSmitePaladinsAPI(HiRezAPI):
    """
    Class for handling connections and requests to Hi-Rez Studios APIs. IS BETTER DON'T INITALISE THIS YOURSELF!
    """
    def __init__(self, devId, authKey, endpoint, responseFormat=ResponseFormat.JSON, sessionId=None, useConfigIni=True):
        """
        The constructor for BaseSmitePaladinsAPI class.
        Keyword arguments/Parameters:
            devId [int]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            authKey [str]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            endpoint [str]: The endpoint that you want to access to retrieve information from the Hi-Rez Studios' API.
            responseFormat [pyrez.enumerations.ResponseFormat]: The response format that will be used by default when making requests (default pyrez.enumerations.ResponseFormat.JSON)
            sessionId [str]: An active sessionId (default None)
            useConfigIni [bool]: (default True)
        """
        super().__init__(devId, authKey, endpoint, responseFormat, sessionId, useConfigIni)

    def getDemoDetails(self, matchId):
        """
        /getdemodetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{matchId}
            Returns information regarding a particular match.  Rarely used in lieu of getmatchdetails().
        Keyword arguments/Parameters:
            matchId [int]:
        """
        response = self.makeRequest("getdemodetails", [matchId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        demoDetails = []
        for demoDetail in response:
            obj = SmiteDemoDetail(**demoDetail) if isinstance(self, SmiteAPI) else PaladinsDemoDetail(**demoDetail)
            demoDetails.append(obj)
        return demoDetails if demoDetails else None
    def getEsportsProLeagueDetails(self):
        """
        /getesportsproleaguedetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Returns the matchup information for each matchup for the current eSports Pro League season.
            An important return value is “match_status” which represents a match being scheduled (1), in-progress (2), or complete (3)
        """
        response = self.makeRequest("getesportsproleaguedetails")
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        details = []
        for detail in response:
            details.append(EsportProLeagueDetail(**detail))
        return details if details else None
    def getGods(self, languageCode=LanguageCode.English):
        """
        /getgods[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{languageCode}
            Returns all Gods and their various attributes.
        Keyword arguments/Parameters:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        Returns:
            List of pyrez.models.God or pyrez.models.Champion objects
        """
        response = self.makeRequest("getgods", [languageCode])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        gods = []
        for god in response:
            obj = God(**god) if isinstance(self, SmiteAPI) else Champion(**god)
            gods.append(obj)
        return gods if gods else None
    def getGodLeaderboard(self, godId, queueId):
        """
        /getgodleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{queue}
            Returns the current season’s leaderboard for a god/queue combination. [SmiteAPI only; queues 440, 450, 451 only]
        Keyword arguments/Parameters:
            godId [int]:
            queueId [int]:
        """
        response = self.makeRequest("getgodleaderboard", [godId, queueId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        godLeaderb = []
        for leader in response:
            obj = GodLeaderboard(**leader) if isinstance(self, SmiteAPI) else ChampionLeaderboard(**i)
            godLeaderb.append(obj)
        return godLeaderb if godLeaderb else None
    def getGodRanks(self, playerId):
        """
        /getgodranks[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
            Returns the Rank and Worshippers value for each God a player has played.
        Keyword arguments/Parameters:
            playerId [int]:
        Returns:
            List of pyrez.models.GodRank objects
        """
        response = self.makeRequest("getgodranks", [playerId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        godRanks = []
        for godRank in response:
            godRanks.append(GodRank(**godRank))
        return godRanks if godRanks else None
    def getGodSkins(self, godId, languageCode=LanguageCode.English):
        """
        /getgodskins[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
            Returns all available skins for a particular God.
        Keyword arguments/Parameters:
            godId [int]:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        response = self.makeRequest("getgodskins", [godId, languageCode])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        godSkins = []
        for godSkin in response:
            obj = GodSkin(**godSkin) if isinstance(self, SmiteAPI) != -1 else ChampionSkin(**godSkin)
            godSkins.append(obj)
        return godSkins if godSkins else None
    def getItems(self, languageCode=LanguageCode.English):
        """
        /getitems[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{languageCode}
            Returns all Items and their various attributes.
        Keyword arguments/Parameters:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        response = self.makeRequest("getitems", [languageCode])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        items = []
        for item in response:
            obj = SmiteItem(**item) if isinstance(self, SmiteAPI) != -1 else PaladinsItem(**item)
            items.append(obj)
        return items if items else None
    def getLeagueLeaderboard(self, queueId, tier, split):
        """
        /getleagueleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queue}/{tier}/{split}
            Returns the top players for a particular league (as indicated by the queue/tier/split parameters).
        Keyword arguments/Parameters:
            queueId [int]:
            tier [int]:
            split [int]:
        """
        response = self.makeRequest("getleagueleaderboard", [queueId, tier, split])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        leagueLeaderboards = []
        for leaderboard in response:
            leagueLeaderboards.append(LeagueLeaderboard(**leaderboard))
        return leagueLeaderboards if leagueLeaderboards else None
    def getLeagueSeasons(self, queueId):
        """
        /getleagueseasons[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queueId}
            Provides a list of seasons (including the single active season) for a match queue.
        Keyword arguments/Parameters:
            queueId [int]:
        """
        response = self.makeRequest("getleagueseasons", [queueId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        seasons = []
        for season in response:
            items.append(LeagueSeason(**season))
        return seasons if seasons else None
    def getLiveMatchDetails(self, matchId):
        """
        /getmatchplayerdetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{matchId}
            Returns player information for a live match.
        Keyword arguments/Parameters:
            matchId [int]:
        """
        response = self.makeRequest("getmatchplayerdetails", [matchId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        matchPlayerDetails = []
        for matchPlayerDetail in response:
            matchPlayerDetails.append(MatchPlayerDetail(**matchPlayerDetail))
        return matchPlayerDetails if matchPlayerDetails else None
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
        response = self.makeRequest("getplayer", [player, portalId] if portalId else [player])
        #raise PlayerNotFoundException("Player don't exist or it's hidden")
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        return SmitePlayer(**response[0]) if isinstance(self, SmiteAPI) else PaladinsPlayer(**response[0])#TypeError: type object argument after ** must be a mapping, not NoneType
class PaladinsAPI(BaseSmitePaladinsAPI):
    """
    Class for handling connections and requests to Paladins API.
    """
    def __init__(self, devId, authKey, responseFormat=ResponseFormat.JSON, sessionId=None, useConfigIni=True):
        """
        The constructor for PaladinsAPI class.
        Keyword arguments/Parameters:
            devId [int]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            authKey [str]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            responseFormat [pyrez.enumerations.ResponseFormat]: The response format that will be used by default when making requests (default pyrez.enumerations.ResponseFormat.JSON)
            sessionId [str]: An active sessionId (default None)
            useConfigIni [bool]: (default True)
        """
        super().__init__(devId, authKey, Endpoint.PALADINS, responseFormat, sessionId, useConfigIni)
    def getLatestPatchNotes(self, languageCode=LanguageCode.English):
        getLatestUpdateNotesResponse = self.makeRequest("https://cms.paladins.com/wp-json/api/get-posts/{0}?tag=update-notes".format(languageCode.value if isinstance(languageCode, LanguageCode) else languageCode))
        if getLatestUpdateNotesResponse is None:
            return None
        post = PaladinsWebsitePost(**getLatestUpdateNotesResponse[0])
        getLatestPatchNotesResponse = self.makeRequest("https://cms.paladins.com/wp-json/api/get-post/{0}?slug={1}".format(languageCode.value if isinstance(languageCode, LanguageCode) else languageCode, post.slug))
        return PaladinsWebsitePost(**getLatestPatchNotesResponse) if getLatestPatchNotesResponse is not None else None
    def getWebsitePostBySlug(self, slug, languageCode=LanguageCode.English):
        getPaladinsWebsitePostsResponse = self.makeRequest("https://cms.paladins.com/wp-json/api/get-post/{0}?slug={1}".format(languageCode.value if isinstance(languageCode, LanguageCode) else languageCode, slug))
        if getPaladinsWebsitePostsResponse is None:
            return None
        posts = []
        for post in getPaladinsWebsitePostsResponse:
            obj = PaladinsWebsitePost(**post)
            posts.append(obj)
        return posts if posts else None
    def getWebsitePosts(self, languageCode=LanguageCode.English):
        getPaladinsWebsitePostsResponse = self.makeRequest("https://cms.paladins.com/wp-json/api/get-posts/{0}".format(languageCode.value if isinstance(languageCode, LanguageCode) else languageCode))
        if getPaladinsWebsitePostsResponse is None:
            return None
        posts = []
        for post in getPaladinsWebsitePostsResponse:
            obj = PaladinsWebsitePost(**post)
            posts.append(obj)
        return posts if posts else None
    def getWebsitePostsByQuery(self, query, languageCode=LanguageCode.English):
        getPaladinsWebsitePostsResponse = self.makeRequest("https://cms.paladins.com/wp-json/api/get-posts/{0}?search={1}".format(languageCode.value if isinstance(languageCode, LanguageCode) else languageCode, query))
        if getPaladinsWebsitePostsResponse is None:
            return None
        posts = []
        for post in getPaladinsWebsitePostsResponse:
            obj = PaladinsWebsitePost(**post)
            posts.append(obj)
        return posts if posts else None
    def getChampions(self, languageCode=LanguageCode.English):
        """
        /getchampions[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{languageCode}
            Returns all Champions and their various attributes. [PaladinsAPI only]
        Keyword arguments/Parameters:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        response = self.makeRequest("getchampions", [languageCode]) # self.makeRequest("getgods", languageCode)
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        champs = []
        for champ in getChampionsResponse:
            champs.append(Champion(**champ))
        return champs if champs else None
    def getChampionCards(self, godId, languageCode=LanguageCode.English):
        """
        /getchampioncards[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
            Returns all Champion cards. [PaladinsAPI only]
        Keyword arguments/Parameters:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        response = self.makeRequest("getchampioncards", [godId, languageCode])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        cards = []
        for card in response:
            cards.append(ChampionCard(**card))
        return cards if cards else None
    def getChampionLeaderboard(self, godId, queueId=PaladinsQueue.Live_Competitive_Keyboard):
        """
        /getchampionleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{queueId}
            Returns the current season’s leaderboard for a champion/queue combination. [PaladinsAPI; only queue 428]
        Keyword arguments/Parameters:
            godId [int]:
            queueId [int]:
        """
        response = self.makeRequest("getchampionleaderboard", [godId, queueId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        champLeaderboards = []
        for champLeaderboard in response:
            champLeaderboards.append(ChampionLeaderboard(**champLeaderboard))
        return champLeaderboards if champLeaderboards else None
    def getChampionRanks(self, playerId):
        """
        /getchampionranks[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
            Returns the Rank and Worshippers value for each Champion a player has played. [PaladinsAPI only]
        Keyword arguments/Parameters:
            playerId [int]:
        """
        response = self.makeRequest("getgodranks", [playerId]) # self.makeRequest("getchampionranks", [playerId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        champRanks = []
        for champRank in response:
            champRanks.append(GodRank(**champRank))
        return champRanks if champRanks else None
    def getChampionSkins(self, godId, languageCode=LanguageCode.English):
        """
        /getchampionskins[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
            Returns all available skins for a particular Champion. [PaladinsAPI only]
        Keyword arguments/Parameters:
            godId [int]:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        response = self.makeRequest("getchampionskins", [godId, languageCode])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        champSkins = []
        for champSkin in response:
            champSkins.append(ChampionSkin(**champSkin))
        return champSkins if champSkins else None
    def getPlayerIdInfoForXboxAndSwitch(self, playerName):
        """
        /getplayeridinfoforxboxandswitch[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerName}
            Meaningful only for the Paladins Xbox API. Paladins Xbox data and Paladins Switch data is stored in the same DB.
            Therefore a Paladins Gamer Tag value could be the same as a Paladins Switch Gamer Tag value.
            Additionally, there could be multiple identical Paladins Switch Gamer Tag values.
            The purpose of this method is to return all Player ID data associated with the playerName (gamer tag) parameter.
            The expectation is that the unique player_id returned could then be used in subsequent method calls. [PaladinsAPI only]
        """
        response = self.makeRequest("getplayeridinfoforxboxandswitch", [playerName])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        playerIds = []
        for playerId in response:
            playerIds.append(PlayerIdInfoForXboxOrSwitch(**playerId))
        return playerIds if playerIds else None
    def getPlayerLoadouts(self, playerId, languageCode=LanguageCode.English):
        """
        /getplayerloadouts[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/playerId}/{languageCode}
            Returns deck loadouts per Champion. [PaladinsAPI only]
        Keyword arguments/Parameters:
            playerId [int]:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        response = self.makeRequest("getplayerloadouts", [playerId, languageCode])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        playerLoadouts = []
        for playerLoadout in response:
            playerLoadouts.append(PlayerLoadout(**playerLoadout))
        return playerLoadouts if playerLoadouts else None
class RealmRoyaleAPI(HiRezAPI):
    """
    Class for handling connections and requests to Realm Royale API.
    """
    def __init__(self, devId, authKey, responseFormat=ResponseFormat.JSON, sessionId=None, useConfigIni=True):
        """
        The constructor for RealmRoyaleAPI class.
        Keyword arguments/Parameters:
            devId [int]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            authKey [str]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            responseFormat [pyrez.enumerations.ResponseFormat]: The response format that will be used by default when making requests (default pyrez.enumerations.ResponseFormat.JSON)
            sessionId [str]: An active sessionId (default None)
            useConfigIni [bool]: (default True)
        """
        super().__init__(devId, authKey, Endpoint.REALM_ROYALE, responseFormat, sessionId, useConfigIni)
    def getLeaderboard(self, queueId, rankingCriteria):
        """
        /getleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queueId}/{ranking_criteria}
            - for duo and quad queues/modes the individual's placement results reflect their team/grouping; solo is self-explanatory
            - will limit results to the top 500 players (minimum 50 matches played per queue); we never like to expose weak/beginner players
            - players that select to be "private" will have their player_name and player_id values hidden
            - {ranking_criteria} can be: 1: team_wins, 2: team_average_placement (shown below), 3: individual_average_kills, 4. win_rate, possibly/probably others as desired
            - expect this data to be cached on an hourly basis because the query to acquire the data will be expensive; don't spam the calls
        """
        response = self.makeRequest("getleaderboard", [queueId, rankingCriteria])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        return RealmRoyaleLeaderboard(**response)
    def getPlayer(self, player, platform=None):
        """
        /getplayer[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{player}/{platform}
            Returns league and other high level data for a particular player.
        Keyword arguments/Parameters:
            player [int] or [str]:
        """
        plat = platform if platform else "hirez" if not str(player).isdigit() or str(player).isdigit() and len(str(player)) <= 8 else "steam"
        response = self.makeRequest("getplayer", [player, plat])
        #raise PlayerNotFoundException("Player don't exist or it's hidden")
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        return RealmRoyalePlayer(**response)
    def getPlayerMatchHistory(self, playerId, startDatetime=None):
        """
        /getplayermatchhistory[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        """
        methodName = "getplayermatchhistory" if startDatetime is None else "getplayermatchhistoryafterdatetime"
        params = [playerId] if startDatetime is None else [startDatetime.strftime("yyyyMMddHHmmss") if isinstance(startDatetime, datetime) else startDatetime, playerId]
        response = self.makeRequest(methodName, params)
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        return RealmMatchHistory(**response)
    def getPlayerStats(self, playerId):
        """
        /getplayerstats[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        """
        return self.makeRequest("getplayerstats", [playerId])
    def getTalents(self, languageCode=LanguageCode.English):
        """
        /gettalents[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{langId}
            Get all talents
        """
        response = self.makeRequest("gettalents", [languageCode])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        talents = []
        for talent in response:
            talents.append(RealmRoyaleTalent(**talent))
        return talents if talents else None
class SmiteAPI(BaseSmitePaladinsAPI):
    """
    Class for handling connections and requests to Smite API.
    """
    def __init__(self, devId, authKey, responseFormat=ResponseFormat.JSON, sessionId=None, useConfigIni=True):
        """
        The constructor for SmiteAPI class.
        Keyword arguments/Parameters:
            devId [int]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            authKey [str]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            responseFormat [pyrez.enumerations.ResponseFormat]: The response format that will be used by default when making requests (default pyrez.enumerations.ResponseFormat.JSON)
            sessionId [str]: An active sessionId (default None)
            useConfigIni [bool]: (default True)
        """
        super().__init__(devId, authKey, Endpoint.SMITE, responseFormat, sessionId, useConfigIni)
    def getGodRecommendedItems(self, godId, languageCode=LanguageCode.English):
        """
        /getgodrecommendeditems[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
            Returns the Recommended Items for a particular God. [SmiteAPI only]
        Keyword arguments/Parameters:
            godId [int]:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        response = self.makeRequest("getgodrecommendeditems", [godId, languageCode])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        recommendedItems = []
        for recommendedItem in response:
            recommendedItems.append(GodRecommendedItem(**recommendedItem))
        return recommendedItems if recommendedItems else None
    def getMotd(self):
        """
        /getmotd[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Returns information about the 20 most recent Match-of-the-Days.
        """
        response = self.makeRequest("getmotd")
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        motds = []
        for motd in response:
            obj = MOTD(**motd)
            motds.append(obj)
        return motds if motds else None
    def getTeamDetails(self, clanId):
        """
        /getteamdetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{clanId}
            Lists the number of players and other high level details for a particular clan.
        Keyword arguments/Parameters:
            clanId [int]:
        """
        response = self.makeRequest("getteamdetails", [clanId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        teamDetails = []
        for teamDetail in response:
            teamDetails.append(TeamDetail(**teamDetail))
        return teamDetails if teamDetails else None
    def getTeamPlayers(self, clanId):
        """
        /getteamplayers[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{clanId}
            Lists the players for a particular clan.
        Keyword arguments/Parameters:
            clanId [int]:
        """
        response = self.makeRequest("getteamplayers", [clanId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        teamPlayers = []
        for teamPlayer in response:
            teamPlayers.append(TeamPlayer(**teamPlayer))
        return teamPlayers if teamPlayers else None
    def getTopMatches(self):
        """
        /gettopmatches[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Lists the 50 most watched / most recent recorded matches.
        """
        response = self.makeRequest("gettopmatches")
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        topMatches = []
        for topMatch in response:
            topMatches.append(SmiteTopMatch(**topMatch))
        return topMatches if topMatches else None
    def searchTeams(self, teamId):
        """
        /searchteams[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{searchTeam}
            Returns high level information for Clan names containing the “searchTeam” string. [SmiteAPI only]
        Keyword arguments/Parameters:
            teamId [int]:
        """
        response = self.makeRequest("searchteams", [teamId])
        if self._responseFormat == ResponseFormat.XML or response is None:
            return response
        teams = []
        for team in response:
            teams.append(TeamSearch(**team))
        return teams if teams else None
class HandOfTheGodsAPI(HiRezAPI):
    """
    Class for handling connections and requests to Hand of the Gods API.
    """
    def __init__(self, devId, authKey, responseFormat=ResponseFormat.JSON, sessionId=None, useConfigIni=True):
        """
        The constructor for HandOfTheGodsAPI class.
        Keyword arguments/Parameters:
            devId [int]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            authKey [str]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            responseFormat [pyrez.enumerations.ResponseFormat]: The response format that will be used by default when making requests (default pyrez.enumerations.ResponseFormat.JSON)
            sessionId [str]: An active sessionId (default None)
            useConfigIni [bool]: (default True)
        """
        super().__init__(devId, authKey, Endpoint.HAND_OF_THE_GODS, responseFormat, sessionId, useConfigIni)
class PaladinsStrikeAPI(HiRezAPI):
    """
    Class for handling connections and requests to Paladins Strike API.
    """
    def __init__(self, devId, authKey, responseFormat=ResponseFormat.JSON, sessionId=None, useConfigIni=True):
        """
        The constructor for PaladinsStrikeAPI class.
        Keyword arguments/Parameters:
            devId [int]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            authKey [str]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            responseFormat [pyrez.enumerations.ResponseFormat]: The response format that will be used by default when making requests (default pyrez.enumerations.ResponseFormat.JSON)
            sessionId [str]: An active sessionId (default None)
            useConfigIni [bool]: (default True)
        """
        super().__init__(devId, authKey, Endpoint.PALADINS_STRIKE, responseFormat, sessionId, useConfigIni)
