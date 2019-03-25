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
        if not devId or not authKey:
            raise IdOrAuthEmptyException("DevId or AuthKey not specified!")
        if int(devId) < 999 and int(devId) > 9999 or not str(devId).isnumeric():
            raise InvalidArgumentException("You need to pass a valid DevId!")
        if len(str(authKey)) != 32 or not str(authKey).isalnum():
            raise InvalidArgumentException("You need to pass a valid AuthKey!")
        if not endpoint:
            raise InvalidArgumentException("Endpoint can't be empty!")
        if not isinstance(responseFormat, ResponseFormat):
            try:
                responseFormat = ResponseFormat(responseFormat)
            except ValueError:
                raise InvalidArgumentException("You need to pass a valid ResponseFormat!")
        self._devId = int(devId)
        self._authKey = str(authKey)
        self._endpointBaseURL = str(endpoint)
        self._responseFormat = responseFormat if responseFormat in [ResponseFormat.JSON, ResponseFormat.XML] else ResponseFormat.JSON
        self._header = header
    @classmethod
    def __getConfigIniFile(cls):
        conf = configparser.ConfigParser()
        conf.read("{0}/conf.ini".format(os.path.dirname(os.path.abspath(__file__))))
        return conf
    @classmethod
    def _saveConfigIni(cls, sessionId):
        conf = cls.__getConfigIniFile()
        conf["Session"]["SessionId"] = sessionId
        with open("{0}/conf.ini".format(os.path.dirname(os.path.abspath(__file__))), 'w') as configfile:
            conf.write(configfile)
    @classmethod
    def _readConfigIni(cls):
        conf = cls.__getConfigIniFile()
        return conf["Session"]["SessionId"] if conf["Session"]["SessionId"] else None
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
        hdrs = defaultHeaders if not headers else headers
        httpResponse = requests.request(method=method, url=url.replace(' ', '%20'), params=params, data=data, headers=hdrs, cookies=cookies, files=files, auth=auth, timeout=timeout, allow_redirects=allowRedirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert)
        if httpResponse.status_code >= 400:
            raise NotFoundException("Wrong URL: {0}".format(httpResponse.text))
        try:
            return httpResponse.json()
        except (JSONException, ValueError):
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
            endpoint [str]: The endpoint that you want to access to retrieve information from the Hi-Rez Studios' API.
            responseFormat [pyrez.enumerations.ResponseFormat]: The response format that will be used by default when making requests (default pyrez.enumerations.ResponseFormat.JSON)
            sessionId [str]: An active sessionId (default None)
            useConfigIni [bool]: (default False)
        """
        super().__init__(devId, authKey, endpoint, responseFormat, self.PYREZ_HEADER)
        self.useConfigIni = useConfigIni
        if self.useConfigIni:
            self.__setSession(self._readConfigIni())
        else:
            sId = None if not sessionId or not str(sessionId).isalnum() and not self.testSession(sessionId) else sessionId
            self.__setSession(sId)
    @classmethod
    def _createTimeStamp(cls, frmt="%Y%m%d%H%M%S"):
        """
        Keyword arguments/Parameters:
            frmt [str]: Format of timeStamp
        Returns:
            Returns the current UTC time (GMT+0) formatted to 'YYYYMMDDHHmmss'
        """
        return cls._getCurrentTime().strftime(frmt)
    @classmethod
    def _getCurrentTime(cls):
        """        
        Returns:
            Returns the current UTC time (GMT+0)
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
        return getMD5Hash(self._encode("{0}{1}{2}{3}".format(self._devId, methodName.lower(), self._authKey, timestamp if timestamp is not None else self._createTimeStamp()))).hexdigest()
    def _sessionExpired(self):
        return str(self.sessionId).isalnum() or not self.sessionId
    @classmethod
    def extractParam(cls, param):
        return param.strftime("yyyyMMdd") if isinstance(param, datetime) else str(param) if isinstance(param, BaseEnum) else str(param.value) if isinstance(param, (IntFlag, Enum)) else str(param)
    def _buildUrlRequest(self, apiMethod=None, params=()): # [queue, date, hour]
        if not apiMethod:
            raise InvalidArgumentException("No API method specified!")
        urlRequest = "{0}/{1}{2}".format(self._endpointBaseURL, apiMethod.lower(), self._responseFormat)
        if apiMethod.lower() != "ping":
            urlRequest += "/{0}/{1}".format(self._devId, self._createSignature(apiMethod.lower()))
            if not self._sessionExpired and apiMethod.lower() != "createsession":
                if apiMethod.lower() == "testsession":
                    return urlRequest + "/{0}/{1}".format(str(params[0]), self._createTimeStamp())
                urlRequest += "/{0}".format(self.sessionId)
            urlRequest += "/{0}".format(self._createTimeStamp())
            for param in params:
                if not param:
                    urlRequest += "/{0}".format(self.extractParam(param))
        return urlRequest.replace(' ', "%20")
    @classmethod
    def checkRetMsg(cls, retMsg):
        if retMsg.find("dailylimit") != -1:
            raise DailyLimitException("Daily limit reached: " + retMsg)
        if retMsg.find("Maximum number of active sessions reached") != -1:
            raise SessionLimitException("Concurrent sessions limit reached: " + retMsg)
        if retMsg.find("Exception while validating developer access") != -1:
            raise WrongCredentials("Wrong credentials: " + retMsg)
        if retMsg.find("No match_queue returned.  It is likely that the match wasn't live when GetMatchPlayerDetails() was called") != -1:
            raise GetMatchPlayerDetailsException("Match isn't live: " + retMsg)
        if retMsg.find("Only training queues") != -1 and retMsg.find("are supported for GetMatchPlayerDetails()") != -1:
            raise GetMatchPlayerDetailsException("Queue not supported by getMatchPlayerDetails(): " + retMsg)
        if retMsg.find("The server encountered an error processing the request") != -1:
            raise RequestErrorException("The server encountered an error processing the request: " + retMsg)
        if retMsg.find("404") != -1:
            raise NotFoundException("Not found: " + retMsg)
    def __setSession(self, sessionId):
        self.sessionId = sessionId
        if self.useConfigIni:
            self._saveConfigIni(self.sessionId)
    def makeRequest(self, apiMethod=None, params=()):
        if not apiMethod:
            raise InvalidArgumentException("No API method specified!")
        if(apiMethod.lower() != "createsession" and self._sessionExpired()):
            self._createSession()
        result = self._httpRequest(apiMethod if str(apiMethod).lower().startswith("http") else self._buildUrlRequest(apiMethod, params), headers=self.PYREZ_HEADER)
        if result:
            if str(self._responseFormat).lower() == str(ResponseFormat.XML).lower():
                return result
            if str(result).lower().find("ret_msg") == -1:
                return None if len(str(result)) == 2 and str(result) == "[]" else result
            hasError = APIResponse(**result if str(result).startswith('{') else result[0])
            if not not hasError and hasError.hasRetMsg():
                if hasError.retMsg == "Approved":
                    self.__setSession(Session(**result).sessionId)
                elif hasError.retMsg.find("Invalid session id") != -1:
                    self._createSession()
                    return self.makeRequest(apiMethod, params)
                else:
                    self.checkRetMsg(hasError.retMsg)
            return result
        return None
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
        responseJSON = self.makeRequest("createsession")
        self._responseFormat = tempResponseFormat
        return None if not responseJSON else Session(**responseJSON)
    def ping(self):
        """
        /ping[ResponseFormat]
        A quick way of validating access to the Hi-Rez API.
        
        Returns:
            Object of pyrez.models.Ping: Returns the infos about the API.
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, ResponseFormat.JSON
        responseJSON = self.makeRequest("ping")
        self._responseFormat = tempResponseFormat
        return None if not responseJSON else Ping(responseJSON)
    def testSession(self, sessionId=None):
        """
        /testsession[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
        A means of validating that a session is established.

        Keyword arguments/Parameters:
            sessionId [str]: A sessionId to validate
        Returns:
            Returns a boolean that means if a sessionId is valid.
        """
        session = sessionId if not not sessionId or str(sessionId).isalnum() else self.sessionId
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
        responseJSON = self.makeRequest("getdataused")
        self._responseFormat = tempResponseFormat
        if not responseJSON:
            return None
        try:
            return DataUsed(**responseJSON)
        except TypeError:
            return DataUsed(**responseJSON[0])
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
        responseJSON = self.makeRequest("gethirezserverstatus")
        self._responseFormat = tempResponseFormat
        if not responseJSON:
            return None
        servers = []
        for server in responseJSON:
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
        responseJSON = self.makeRequest("getpatchinfo")
        self._responseFormat = tempResponseFormat
        return None if not responseJSON else PatchInfo(**responseJSON)
    def getFriends(self, playerId):
        """
        /getfriends[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        Returns the User names of each of the player’s friends of one player. [PC only]
        
        Returns:
            List of pyrez.models.Friend objects
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        responseJSON = self.makeRequest("getfriends", [playerId])
        if self._responseFormat == ResponseFormat.XML or not responseJSON:
            return responseJSON
        friends = []
        for friend in responseJSON:
            friends.append(Friend(**friend))
        return friends if friends else None
    def getMatchDetails(self, matchId):
        """
        /getmatchdetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{matchId}
        Returns the statistics for a particular completed match.
        
        Keyword arguments/Parameters:
            matchId [int]:
        """
        if not matchId or not str(matchId).isnumeric():
            raise InvalidArgumentException("Invalid Match ID: matchId must to be numeric (int)!")
        responseJSON = self.makeRequest("getmatchdetails", [matchId])
        if self._responseFormat == ResponseFormat.XML or not responseJSON:
            return responseJSON
        matchDetails = []
        for matchDetail in responseJSON:
            matchDetails.append(MatchDetail(**matchDetail))
        return matchDetails if matchDetails else None
    def getMatchDetailsBatch(self, matchIds=()):
        """
        /getmatchdetailsbatch[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{matchId,matchId,matchId,...matchId}
        Returns the statistics for a particular set of completed matches.

        Keyword arguments/Parameters:
            matchIds [list]:
        NOTE:
            There is a byte limit to the amount of data returned;
            Please limit the CSV parameter to 5 to 10 matches because of this and for Hi-Rez DB Performance reasons.
        """
        responseJSON = self.makeRequest("getmatchdetailsbatch", [','.join(matchIds)])
        if self._responseFormat == ResponseFormat.XML or not responseJSON:
            return responseJSON
        matchDetails = []
        for matchDetail in responseJSON:
            matchDetails.append(MatchDetail(**matchDetail))
        return matchDetails if matchDetails else None
    def getMatchHistory(self, playerId):
        """
        /getmatchhistory[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        Gets recent matches and high level match statistics for a particular player.

        Keyword arguments/Parameters:
            playerId [int]:
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        getMatchHistoryResponse = self.makeRequest("getmatchhistory", [playerId])
        if self._responseFormat == ResponseFormat.XML or not getMatchHistoryResponse:
            return getMatchHistoryResponse
        matchHistorys = []
        for matchHistory in getMatchHistoryResponse:
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
        if not queueId or not str(queueId).isnumeric() or not isinstance(queueId, (RealmRoyaleQueue, SmiteQueue, PaladinsQueue)):
            raise InvalidArgumentException("Invalid Queue ID: queueId must to be numeric (int)!")
        getMatchIdsByQueueResponse = self.makeRequest("getmatchidsbyqueue", [queueId, date.strftime("%Y%m%d") if isinstance(date, datetime) else date, hour])
        if self._responseFormat == ResponseFormat.XML or not getMatchIdsByQueueResponse:
            return getMatchIdsByQueueResponse
        queueIds = []
        for i in getMatchIdsByQueueResponse:
            queueIds.append(MatchIdByQueue(**i))
        return queueIds if queueIds else None
    def getPlayer(self, player, portalId=None):
        """
        /getplayer[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{player}
        /getplayer[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{player}/{portalId}
        Returns league and other high level data for a particular player.

        Keyword arguments/Parameters:
            player [int] or [str]:
        """
        if not player or len(str(player)) <= 3:
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        if str(self._responseFormat).lower() == str(ResponseFormat.XML).lower():
            return self.makeRequest("getplayer", [portalId, player] if portalId else [player])
        #raise PlayerNotFoundException("Player don't exist or it's hidden")
        if isinstance(self, RealmRoyaleAPI):
            plat = "hirez" if not str(player).isdigit() or str(player).isdigit() and len(str(player)) <= 8 else "steam"
            return PlayerRealmRoyale(**self.makeRequest("getplayer", [player, plat]))
        res = self.makeRequest("getplayer", [player, portalId] if portalId else [player])
        return None if not res else PlayerSmite(**res[0]) if isinstance(self, SmiteAPI) else PlayerPaladins(**res[0])
    def getPlayerAchievements(self, playerId):
        """
        /getplayerachievements[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        Returns select achievement totals (Double kills, Tower Kills, First Bloods, etc) for the specified playerId.

        Keyword arguments/Parameters:
            playerId [int]:
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        getPlayerAchievementsResponse = self.makeRequest("getplayerachievements", [playerId])
        if self._responseFormat == ResponseFormat.XML or not getPlayerAchievementsResponse:
            return getPlayerAchievementsResponse
        try:
            return PlayerAcheviements(**getPlayerAchievementsResponse)
        except TypeError:
            return PlayerAcheviements(**getPlayerAchievementsResponse[0])
    def getPlayerIdByName(self, playerName):
        """
        /getplayeridbyname[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{playerName}
        Function returns a list of Hi-Rez playerId values (expected list size = 1) for playerName provided. The playerId returned is
        expected to be used in various other endpoints to represent the player/individual regardless of platform.

        Keyword arguments/Parameters:
            playerName [str]:
        """
        getPlayerIdByNameResponse = self.makeRequest("getplayeridbyname", [playerName])
        if self._responseFormat == ResponseFormat.XML or not getPlayerIdByNameResponse:
            return getPlayerIdByNameResponse
        playerIds = []
        for i in getPlayerIdByNameResponse:
            playerIds.append(PlayerIdByX(**i))
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
        getPlayerIdByPortalUserIdResponse = self.makeRequest("getplayeridbyportaluserid", [portalId, portalUserId])
        if self._responseFormat == ResponseFormat.XML or not getPlayerIdByPortalUserIdResponse:
            return getPlayerIdByPortalUserIdResponse
        playerIds = []
        for i in getPlayerIdByPortalUserIdResponse:
            playerIds.append(PlayerIdByX(**i))
        return playerIds if playerIds else None
    def getPlayerIdsByGamerTag(self, gamerTag, portalId):
        """
        /getplayeridsbygamertag[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{portalId}/{gamerTag}
        Function returns a list of Hi-Rez playerId values for {portalId}/{portalUserId} combination provided. The appropriate
        playerId extracted from this list by the API end user is expected to be used in various other endpoints to represent the player/individual regardless of platform.

        Keyword arguments/Parameters:
            gamerTag [str]:
        """
        getPlayerIdsByGamerTagResponse = self.makeRequest("getplayeridsbygamertag", [portalId, gamerTag])
        if self._responseFormat == ResponseFormat.XML or not getPlayerIdsByGamerTagResponse:
            return getPlayerIdsByGamerTagResponse
        playerIds = []
        for i in getPlayerIdsByGamerTagResponse:
            playerIds.append(PlayerIdByX(**i))
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
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        getPlayerStatusResponse = self.makeRequest("getplayerstatus", [playerId])
        if self._responseFormat == ResponseFormat.XML or not getPlayerStatusResponse:
            return getPlayerStatusResponse
        try:
            return PlayerStatus(**getPlayerStatusResponse)
        except TypeError:
            return PlayerStatus(**getPlayerStatusResponse[0])
    def getQueueStats(self, playerId, queueId):
        """
        /getqueuestats[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}/{queue}
        Returns match summary statistics for a (player, queue) combination grouped by gods played.

        Keyword arguments/Parameters:
            playerId [int]:
            queueId [int]:
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        #if not queueId or not str(queueId).isnumeric() or not isinstance(queueId, (RealmRoyaleQueue, SmiteQueue, PaladinsQueue)):
        #    raise InvalidArgumentException("Invalid Queue ID: queueId must to be numeric (int)!")
        getQueueStatsResponse = self.makeRequest("getqueuestats", [playerId, queueId])
        if self._responseFormat == ResponseFormat.XML or not getQueueStatsResponse:
            return getQueueStatsResponse
        queueStatsList = []
        for i in getQueueStatsResponse:
            queueStatsList.append(QueueStats(**i))
        return queueStatsList if queueStatsList else None
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
        if not isinstance(self, (PaladinsAPI, SmiteAPI)):
            raise NotSupported("This method is just for Paladins and Smite API's!")
        if not matchId or not str(matchId).isnumeric():
            raise InvalidArgumentException("Invalid Match ID: matchId must to be numeric (int)!")
        getDemoDetailsResponse = self.makeRequest("getdemodetails", [matchId])
        if self._responseFormat == ResponseFormat.XML or not getDemoDetailsResponse:
            return getDemoDetailsResponse
        demoDetails = []
        for demoDetail in getDemoDetailsResponse:
            demoDetails.append(SmiteDemoDetail(**demoDetail) if isinstance(self, SmiteAPI) else PaladinsDemoDetail(**demoDetail))
        return demoDetails if demoDetails else None
    def getEsportsProLeagueDetails(self):
        """
        /getesportsproleaguedetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
        Returns the matchup information for each matchup for the current eSports Pro League season.
        An important return value is “match_status” which represents a match being scheduled (1), in-progress (2), or complete (3)
        """
        if not isinstance(self, (PaladinsAPI, SmiteAPI)):
            raise NotSupported("This method is just for Paladins and Smite API's!")
        getEsportsProLeagueDetailsResponse = self.makeRequest("getesportsproleaguedetails")
        if self._responseFormat == ResponseFormat.XML and not getEsportsProLeagueDetailsResponse:
            return getEsportsProLeagueDetailsResponse
        details = []
        for detail in getEsportsProLeagueDetailsResponse:
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
        if not isinstance(self, (PaladinsAPI, SmiteAPI)):
            raise NotSupported("This method is just for Paladins and Smite API's!")
        getGodsResponse = self.makeRequest("getgods", [languageCode])
        if self._responseFormat == ResponseFormat.XML or not getGodsResponse:
            return getGodsResponse
        gods = []
        for i in getGodsResponse:
            gods.append(God(**i) if isinstance(self, SmiteAPI) else Champion(**i))
        return gods if gods else None
    def getGodLeaderboard(self, godId, queueId):
        """
        /getgodleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{queue}
        Returns the current season’s leaderboard for a god/queue combination. [SmiteAPI only; queues 440, 450, 451 only]
        
        Keyword arguments/Parameters:
            godId [int]:
            queueId [int]:
        """
        if not godId or not str(godId).isnumeric() or not isinstance(godId, (Gods, Champions)):
            raise InvalidArgumentException("Invalid God ID: godId must to be numeric (int)!")
        if not queueId or not str(queueId).isnumeric() or not isinstance(queueId, (SmiteQueue, PaladinsQueue)):
            raise InvalidArgumentException("Invalid Queue ID: queueId must to be numeric (int)!")
        getGodLeaderboardResponse = self.makeRequest("getgodleaderboard", [godId, queueId])
        if self._responseFormat == ResponseFormat.XML or not getGodLeaderboardResponse:
            return getGodLeaderboardResponse
        godLeaderb = []
        for leader in getGodLeaderboardResponse:
            godLeaderb.append(GodLeaderboard(**leader) if isinstance(self, SmiteAPI) else ChampionLeaderboard(**i))
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
        if not isinstance(self, (PaladinsAPI, SmiteAPI)):
            raise NotSupported("This method is just for Paladins and Smite API's!")
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        getGodRanksResponse = self.makeRequest("getgodranks", [playerId])
        if self._responseFormat == ResponseFormat.XML or not getGodRanksResponse:
            return getGodRanksResponse
        godRanks = []
        for i in getGodRanksResponse:
            godRanks.append(GodRank(**i))
        return godRanks if godRanks else None
    def getGodSkins(self, godId, languageCode=LanguageCode.English):
        """
        /getgodskins[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
        Returns all available skins for a particular God.
        
        Keyword arguments/Parameters:
            godId [int]:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        if not godId or not str(godId).isnumeric() or not isinstance(godId, (Gods, Champions)):
            raise InvalidArgumentException("Invalid Queue ID: queueId must to be numeric (int)!")
        getGodSkinsResponse = self.makeRequest("getgodskins", [godId, languageCode])
        if self._responseFormat == ResponseFormat.XML or not getGodSkinsResponse:
            return getGodSkinsResponse
        godSkins = []
        for godSkin in getGodSkinsResponse:
            godSkins.append(GodSkin(**godSkin) if isinstance(self, SmiteAPI) else ChampionSkin(**godSkin))
        return godSkins if godSkins else None
    def getItems(self, languageCode=LanguageCode.English):
        """
        /getitems[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{languageCode}
        Returns all Items and their various attributes.
        
        Keyword arguments/Parameters:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        getItemsResponse = self.makeRequest("getitems", [languageCode])
        if self._responseFormat == ResponseFormat.XML or not getItemsResponse:
            return getItemsResponse
        items = []
        for item in getItemsResponse:
            items.append(SmiteItem(**item) if isinstance(self, SmiteAPI) != -1 else PaladinsItem(**item))
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
        if not queueId or not str(queueId).isnumeric() or not isinstance(queueId, (SmiteQueue, PaladinsQueue)):
            raise InvalidArgumentException("Invalid Queue ID: queueId must to be numeric (int)!")
        getLeagueLeaderboardResponse = self.makeRequest("getleagueleaderboard", [queueId, tier, split])
        if self._responseFormat == ResponseFormat.XML or not getLeagueLeaderboardResponse:
            return getLeagueLeaderboardResponse
        leagueLeaderboards = []
        for leaderboard in getLeagueLeaderboardResponse:
            leagueLeaderboards.append(LeagueLeaderboard(**leaderboard))
        return leagueLeaderboards if leagueLeaderboards else None
    def getLeagueSeasons(self, queueId):
        """
        /getleagueseasons[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queueId}
        Provides a list of seasons (including the single active season) for a match queue.

        Keyword arguments/Parameters:
            queueId [int]:
        """
        if not queueId or not str(queueId).isnumeric() or not isinstance(queueId, (SmiteQueue, PaladinsQueue)):
            raise InvalidArgumentException("Invalid Queue ID: queueId must to be numeric (int)!")
        getLeagueSeasonsResponse = self.makeRequest("getleagueseasons", [queueId])
        if self._responseFormat == ResponseFormat.XML or not getLeagueSeasonsResponse:
            return getLeagueSeasonsResponse
        seasons = []
        for season in getLeagueSeasonsResponse:
            items.append(LeagueSeason(**season))
        return seasons if seasons else None
    def getLiveMatchDetails(self, matchId):
        """
        /getmatchplayerdetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{matchId}
        Returns player information for a live match.

        Keyword arguments/Parameters:
            matchId [int]:
        """
        if not matchId or not str(matchId).isnumeric():
            raise InvalidArgumentException("Invalid Match ID: matchId must to be numeric (int)!")
        responseJSON = self.makeRequest("getmatchplayerdetails", [matchId])
        if self._responseFormat == ResponseFormat.XML or not responseJSON:
            return responseJSON
        players = []
        for player in responseJSON:
            players.append(MatchPlayerDetail(**player))
        return players if players else None
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
        if not getLatestUpdateNotesResponse:
            return None
        post = PaladinsWebsitePost(**getLatestUpdateNotesResponse[0])
        getLatestPatchNotesResponse = self.makeRequest("https://cms.paladins.com/wp-json/api/get-post/{0}?slug={1}".format(languageCode.value if isinstance(languageCode, LanguageCode) else languageCode, post.slug))
        return None if not getLatestPatchNotesResponse else PaladinsWebsitePost(**getLatestPatchNotesResponse)
    def getWebsitePostBySlug(self, slug, languageCode=LanguageCode.English):
        getPaladinsWebsitePostsResponse = self.makeRequest("https://cms.paladins.com/wp-json/api/get-post/{0}?slug={1}".format(languageCode.value if isinstance(languageCode, LanguageCode) else languageCode, slug))
        if not getPaladinsWebsitePostsResponse:
            return None
        posts = []
        for post in getPaladinsWebsitePostsResponse:
            obj = PaladinsWebsitePost(**post)
            posts.append(obj)
        return posts if posts else None
    def getWebsitePosts(self, languageCode=LanguageCode.English):
        getPaladinsWebsitePostsResponse = self.makeRequest("https://cms.paladins.com/wp-json/api/get-posts/{0}".format(languageCode.value if isinstance(languageCode, LanguageCode) else languageCode))
        if not getPaladinsWebsitePostsResponse:
            return None
        posts = []
        for post in getPaladinsWebsitePostsResponse:
            obj = PaladinsWebsitePost(**post)
            posts.append(obj)
        return posts if posts else None
    def getWebsitePostsByQuery(self, query, languageCode=LanguageCode.English):
        getPaladinsWebsitePostsResponse = self.makeRequest("https://cms.paladins.com/wp-json/api/get-posts/{0}?search={1}".format(languageCode.value if isinstance(languageCode, LanguageCode) else languageCode, query))
        if not getPaladinsWebsitePostsResponse:
            return None
        posts = []
        for post in getPaladinsWebsitePostsResponse:
            posts.append(PaladinsWebsitePost(**post))
        return posts if posts else None
    def getChampions(self, languageCode=LanguageCode.English):
        """
        /getchampions[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{languageCode}
        Returns all Champions and their various attributes. [PaladinsAPI only]

        Keyword arguments/Parameters:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        getChampionsResponse = self.makeRequest("getchampions", [languageCode]) # self.makeRequest("getgods", languageCode)
        if self._responseFormat == ResponseFormat.XML or not getChampionsResponse:
            return getChampionsResponse
        champions = []
        for i in getChampionsResponse:
            champions.append(Champion(**i))
        return champions if champions else None
    def getChampionCards(self, godId, languageCode=LanguageCode.English):
        """
        /getchampioncards[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
        Returns all Champion cards. [PaladinsAPI only]

        Keyword arguments/Parameters:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        if not godId or not str(godId).isnumeric() or not isinstance(godId, Champions):
            raise InvalidArgumentException("Invalid Queue ID: queueId must to be numeric (int)!")
        getChampionsCardsResponse = self.makeRequest("getchampioncards", [godId, languageCode])
        if self._responseFormat == ResponseFormat.XML or not getChampionsCardsResponse:
            return getChampionsCardsResponse
        cards = []
        for i in getChampionsCardsResponse:
            cards.append(ChampionCard(**i))
        return cards if cards else None
    def getChampionLeaderboard(self, godId, queueId=PaladinsQueue.Live_Competitive_Keyboard):
        """
        /getchampionleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{queueId}
        Returns the current season’s leaderboard for a champion/queue combination. [PaladinsAPI; only queue 428]
        
        Keyword arguments/Parameters:
            godId [int]:
            queueId [int]:
        """
        if not godId or not str(godId).isnumeric() or not isinstance(godId, Champions):
            raise InvalidArgumentException("Invalid Queue ID: queueId must to be numeric (int)!")
        getChampionLeaderboardResponse = self.makeRequest("getchampionleaderboard", [godId, queueId])
        if self._responseFormat == ResponseFormat.XML or not getChampionLeaderboardResponse:
            return getChampionLeaderboardResponse
        getChampionLeaderboard = []
        for i in getChampionLeaderboardResponse:
            getChampionLeaderboard.append(ChampionLeaderboard(**i))
        return getChampionLeaderboard if getChampionLeaderboard else None
    def getChampionRanks(self, playerId):
        """
        /getchampionranks[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        Returns the Rank and Worshippers value for each Champion a player has played. [PaladinsAPI only]
        
        Keyword arguments/Parameters:
            playerId [int]:
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        getChampionsRanksResponse = self.makeRequest("getgodranks", [playerId]) # self.makeRequest("getchampionranks", [playerId])
        if self._responseFormat == ResponseFormat.XML or not getChampionsRanksResponse:
            return getChampionsRanksResponse
        championRanks = []
        for i in getChampionsRanksResponse:
            championRanks.append(GodRank(**i))
        return championRanks if championRanks else None
    def getChampionSkins(self, godId, languageCode=LanguageCode.English):
        """
        /getchampionskins[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
        Returns all available skins for a particular Champion. [PaladinsAPI only]
        
        Keyword arguments/Parameters:
            godId [int]:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        if not godId or not str(godId).isnumeric() or not isinstance(godId, Champions):
            raise InvalidArgumentException("Invalid Queue ID: queueId must to be numeric (int)!")
        getChampSkinsResponse = self.makeRequest("getchampionskins", [godId, languageCode])
        if self._responseFormat == ResponseFormat.XML or not getChampSkinsResponse:
            return getChampSkinsResponse
        champSkins = []
        for champSkin in getChampSkinsResponse:
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
        getPlayerIdInfoForXboxAndSwitchResponse = self.makeRequest("getplayeridinfoforxboxandswitch", [playerName])
        if self._responseFormat == ResponseFormat.XML or not getPlayerIdInfoForXboxAndSwitchResponse:
            return getPlayerIdInfoForXboxAndSwitchResponse
        playerIds = []
        for playerId in getPlayerIdInfoForXboxAndSwitchResponse:
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
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        getPlayerLoadoutsResponse = self.makeRequest("getplayerloadouts", [playerId, languageCode])
        if self._responseFormat == ResponseFormat.XML or not getPlayerLoadoutsResponse:
            return getPlayerLoadoutsResponse
        playerLoadouts = []
        for playerLoadout in getPlayerLoadoutsResponse:
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
        if not queueId or not str(queueId).isnumeric() or not isinstance(queueId, RealmRoyaleQueue):
            raise InvalidArgumentException("Invalid Queue ID: queueId must to be numeric (int)!")
        getLeaderboardResponse = self.makeRequest("getleaderboard", [queueId, rankingCriteria])
        if self._responseFormat == ResponseFormat.XML or not getLeaderboardResponse:
            return getLeaderboardResponse
        return RealmRoyaleLeaderboard(**getLeaderboardResponse)
    def getPlayerMatchHistory(self, playerId, startDatetime=None):
        """
        /getplayermatchhistory[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        methodName = "getplayermatchhistory" if not startDatetime else "getplayermatchhistoryafterdatetime"
        params = [playerId] if not startDatetime else [startDatetime.strftime("yyyyMMddHHmmss") if isinstance(startDatetime, datetime) else startDatetime, playerId]
        getPlayerMatchHistoryResponse = self.makeRequest(methodName, params)
        if self._responseFormat == ResponseFormat.XML or not getPlayerMatchHistoryResponse:
            return getPlayerMatchHistoryResponse
        return RealmMatchHistory(**getPlayerMatchHistoryResponse)
    def getPlayerStats(self, playerId):
        """ 
        /getplayerstats[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        return self.makeRequest("getplayerstats", [playerId])
    def getTalents(self, languageCode=LanguageCode.English):
        """
        /gettalents[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{langId}
        Get all talents
        """
        if not languageCode or not str(languageCode).isnumeric() or not isinstance(language, LanguageCode):
            raise InvalidArgumentException("Invalid LangId!")
        responseJSON = self.makeRequest("gettalents", [languageCode])
        if self._responseFormat == ResponseFormat.XML or not responseJSON:
            return responseJSON
        talents = []
        for talent in responseJSON:
            talents.append(RealmRoyaleTalent(**talent))
        return talents if talents else None
    def searchPlayers(self, playerName):
        """
        /searchplayers[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerName}
        """
        searchPlayerResponse = self.makeRequest("searchplayers", [playerName])
        if self._responseFormat == ResponseFormat.XML or not searchPlayerResponse:
            return searchPlayerResponse
        players = []
        for player in searchPlayerResponse:
            players.append(Player(**player))
        return players if players else None
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
        getGodRecommendedItemsResponse = self.makeRequest("getgodrecommendeditems", [godId, languageCode])
        if self._responseFormat == ResponseFormat.XML or not getGodRecommendedItemsResponse:
            return getGodRecommendedItemsResponse
        recommendedItems = []
        for recommendedItem in getGodRecommendedItemsResponse:
            recommendedItems.append(GodRecommendedItem(**recommendedItem))
        return recommendedItems if recommendedItems else None
    def getMotd(self):
        """
        /getmotd[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
        Returns information about the 20 most recent Match-of-the-Days.
        """
        getMOTDResponse = self.makeRequest("getmotd")
        if self._responseFormat == ResponseFormat.XML or not getMOTDResponse:
            return getMOTDResponse
        motds = []
        for motd in getMOTDResponse:
            motds.append(MOTD(**motd))
        return motds if motds else None
    def getTeamDetails(self, clanId):
        """
        /getteamdetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{clanId}
        Lists the number of players and other high level details for a particular clan.
        
        Keyword arguments/Parameters:
            clanId [int]:
        """
        if not clanId or not str(clanId).isnumeric():
            raise InvalidArgumentException("Invalid Clan ID: clanId must to be numeric (int)!")
        getTeamDetailsResponse = self.makeRequest("getteamdetails", [clanId])
        if self._responseFormat == ResponseFormat.XML or not getTeamDetailsResponse:
            return getTeamDetailsResponse
        teamDetails = []
        for teamDetail in getTeamDetailsResponse:
            teamDetails.append(TeamDetail(**teamDetail))
        return teamDetails if teamDetails else None
    def getTeamPlayers(self, clanId):
        """
        /getteamplayers[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{clanId}
        Lists the players for a particular clan.
        
        Keyword arguments/Parameters:
            clanId [int]:
        """
        if not clanId or not str(clanId).isnumeric():
            raise InvalidArgumentException("Invalid Clan ID: clanId must to be numeric (int)!")
        getTeamPlayers = self.makeRequest("getteamplayers", [clanId])
        if self._responseFormat == ResponseFormat.XML or not getTeamPlayers:
            return getTeamPlayers
        teamPlayers = []
        for teamPlayer in getTeamPlayers:
            teamPlayers.append(TeamPlayer(**teamPlayer))
        return teamPlayers if teamPlayers else None
    def getTopMatches(self):
        """
        /gettopmatches[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
        Lists the 50 most watched / most recent recorded matches.
        """
        getTopMatchesResponse = self.makeRequest("gettopmatches")
        if self._responseFormat == ResponseFormat.XML or not getTopMatchesResponse:
            return getTopMatchesResponse
        matches = []
        for match in getTopMatchesResponse:
            matches.append(SmiteTopMatch(**match))
        return matches if matches else None
    def searchTeams(self, teamId):
        """
        /searchteams[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{searchTeam}
        Returns high level information for Clan names containing the “searchTeam” string. [SmiteAPI only]
        
        Keyword arguments/Parameters:
            teamId [int]:
        """
        getSearchTeamsResponse = self.makeRequest("searchteams", [teamId])
        if self._responseFormat == ResponseFormat.XML or not getSearchTeamsResponse:
            return getSearchTeamsResponse
        teams = []
        for team in getSearchTeamsResponse:
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
