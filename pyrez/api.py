from datetime import timedelta, datetime
from hashlib import md5 as getMD5Hash
from sys import version_info as pythonVersion
import requests
from enum import Enum, IntFlag

import pyrez
from pyrez.enumerations import *
from pyrez.exceptions import *
from pyrez.http import HttpRequest as HttpRequest
from pyrez.models import *

class BaseAPI:
    """
    DON'T INITALISE THIS YOURSELF!

    Parameters
    ----------
    devId : int
        Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
    authKey : str
        Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
    endpoint : class:`Endpoint`
        The endpoint that will be used by default for outgoing requests.
    responseFormat : [optional] : class:`ResponseFormat`
        The response format that will be used by default when making requests.
        Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
    """
    def __init__(self, devId, authKey, endpoint, responseFormat = ResponseFormat.JSON, header = None):
        """
        Parameters
        ----------
        devId : int
            Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
        authKey : str
            Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
        endpoint : class:`Endpoint`
            The endpoint that will be used by default for outgoing requests.
        responseFormat : [optional] : class:`ResponseFormat`
            The response format that will be used by default when making requests.
            Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
        """
        if not devId or not authKey:
            raise IdOrAuthEmptyException("DevId or AuthKey not specified!")
        elif len(str(devId)) != 4 or not str(devId).isnumeric():
            raise InvalidArgumentException("You need to pass a valid DevId!")
        elif len(str(authKey)) != 32 or not str(authKey).isalnum():
            raise InvalidArgumentException("You need to pass a valid AuthKey!")
        elif len(str(endpoint)) == 0 :
            raise InvalidArgumentException("Endpoint can't be empty!")
        self.__devId__ = int(devId)
        self.__authKey__ = str(authKey)
        self.__endpointBaseURL__ = str(endpoint)
        self.__responseFormat__ = ResponseFormat(responseFormat) if isinstance(responseFormat, ResponseFormat) else ResponseFormat.JSON
        self.__header__ = header
        
    def __encode__(self, string, encodeType = "utf-8"):
        return str(string).encode(encodeType)

    def __decode__(self, string, encodeType = "utf-8"):
        return str(string).encode(encodeType)

    def __httpRequest__(self, url, header = None):
        httpResponse = HttpRequest(header if header else self.__header__).get(url)
        if httpResponse.status_code >= 400:
            raise NotFoundException("Wrong URL: {0}".format(httpResponse.text))
        if httpResponse.status_code == 200:
            try:
                return httpResponse.json()
            except:
                return httpResponse.text

class HiRezAPI(BaseAPI):
    """
    Class for handling connections and requests to Hi-Rez Studios APIs. IS BETTER DON'T INITALISE THIS YOURSELF!

    Parameters
    ----------
    devId : int
        Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
    authKey : str
        Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
    endpoint : class:`Endpoint`
        The endpoint that will be used by default for outgoing requests.
    responseFormat : [optional] : class:`ResponseFormat`
        The response format that will be used by default when making requests.
        Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
    """

    PYREZ_HEADER = { "user-agent": "{0} [Python/{1.major}.{1.minor}]".format(pyrez.__title__, pythonVersion) }

    def __init__(self, devId, authKey, endpoint, responseFormat = ResponseFormat.JSON, sessionId = None):
        """
        Parameters
        ----------
        devId : int
            Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
        authKey : str
            Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
        endpoint : class:`Endpoint`
            The endpoint that will be used by default for outgoing requests.
        responseFormat : [optional] : class:`ResponseFormat`
            The response format that will be used by default when making requests.
            Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
        """
        super().__init__(devId, authKey, endpoint, responseFormat, self.PYREZ_HEADER)
        self.currentSessionId = sessionId if sessionId and str(sessionId).isalnum() and self.testSession(sessionId) else None

    def __createTimeStamp__(self, format = "%Y%m%d%H%M%S"):
        """
        Parameters
        ----------
        format : str
            Format of timeStamp

        Returns
        -------
            Returns the current time formatted
        """
        return self.__currentTime__().strftime(format)

    def __currentTime__(self):
        """
        
        Returns
        -------
            Returns the current UTC time
        """
        return datetime.utcnow()

    def __createSignature__(self, method, timestamp = None):
        """
        Parameters
        ----------
        method : str
            Method name
        timestamp : str
            Format of timeStamp
            
        Returns
        -------
            Returns a Signature hash of the method
        """
        return getMD5Hash(self.__encode__(str(self.__devId__) + str(method) + str(self.__authKey__) + str(timestamp if timestamp else self.__createTimeStamp__()))).hexdigest()

    def __sessionExpired__(self):
        return self.currentSessionId is None or not str(self.currentSessionId).isalnum()

    def __buildUrlRequest__(self, apiMethod, params =()): # [queue, date, hour]
        if len(str(apiMethod)) == 0:
            raise InvalidArgumentException("No API method specified!")
        #urlRequest = '/'.join(self.__endpointBaseURL__, apiMethod.lower(), self.__responseFormat__)
        urlRequest = "{0}/{1}{2}".format(self.__endpointBaseURL__, apiMethod.lower(), self.__responseFormat__)
        if apiMethod.lower() != "ping":
            urlRequest += "/{0}/{1}".format(self.__devId__, self.__createSignature__(apiMethod.lower()))
            if self.currentSessionId != None and apiMethod.lower() != "createsession":
                if apiMethod.lower() != "testsession":
                    urlRequest += "/{0}".format(self.currentSessionId)
                else:
                    return "{0}/{1}".format(str(params[0]), self.__createTimeStamp__())
            urlRequest += "/{0}".format(self.__createTimeStamp__())
            if params: #urlRequest += "/" + [str(param) for param in params]
                for param in params:
                    if param != None:
                        urlRequest += "/{0}".format(param.strftime("yyyyMMdd") if isinstance(param, datetime) else str(param.value) if isinstance(param, IntFlag) or isinstance(param, Enum) else str(param))
        return urlRequest.replace(' ', "%20")
    
    def makeRequest(self, apiMethod, params =()):
        if len(str(apiMethod)) == 0:
            raise InvalidArgumentException("No API method specified!")
        elif(apiMethod.lower() != "createsession" and self.__sessionExpired__()):
            self.__createSession__()
        result = self.__httpRequest__(apiMethod if str(apiMethod).lower().startswith("http") else self.__buildUrlRequest__(apiMethod, params))
        if result:
            if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
                return result
            else:
                if str(result).lower().find("ret_msg") == -1:
                    return None if len(str(result)) == 2 and str(result) == "[]" else result
                else:
                    #https://github.com/teamreflex/PaladinsPHP/blob/111a3ef8809d9ac0da85b3ad20ac14583fd1bc64/src/Request.php
                    hasError = APIResponse(**result) if str(result).startswith('{') else APIResponse(**result[0])
                    if hasError != None and hasError.hasRetMsg():
                        if hasError.retMsg == "Approved":
                            self.currentSessionId = Session(**result).sessionId
                        elif hasError.retMsg.find("dailylimit") != -1:
                            raise DailyLimitException("Daily limit reached: " + hasError.retMsg)
                        elif hasError.retMsg.find("Maximum number of active sessions reached") != -1:
                            raise SessionLimitException("Concurrent sessions limit reached: " + hasError.retMsg)
                        elif hasError.retMsg.find("Invalid session id") != -1:
                            self.__createSession__()
                            return self.makeRequest(apiMethod, params)
                        elif hasError.retMsg.find("Exception while validating developer access") != -1:
                            raise WrongCredentials("Wrong credentials: " + hasError.retMsg)
                        elif hasError.retMsg.find("No match_queue returned.  It is likely that the match wasn't live when GetMatchPlayerDetails() was called") != -1:
                            raise GetMatchPlayerDetailsException("Match isn't live: " + hasError.retMsg)
                        elif hasError.retMsg.find("Only training queues") != -1 and hasError.retMsg.find("are supported for GetMatchPlayerDetails()") != -1:
                            raise GetMatchPlayerDetailsException("Queue not supported by getMatchPlayerDetails(): " + hasError.retMsg)
                        elif hasError.retMsg.find("The server encountered an error processing the request") != -1:
                            raise RequestErrorException("The server encountered an error processing the request: " + hasError.retMsg)
                        elif hasError.retMsg.find("404") != -1:
                            raise NotFoundException("Not found: " + hasError.retMsg)
                    return result

    def switchEndpoint(self, endpoint):
        if not isinstance(endpoint, Endpoint):
            raise InvalidArgumentException("You need to use the Endpoint enum to switch endpoints")
        self.__endpointBaseURL__ = str(endpoint)

    def __createSession__(self):
        """
        /createsession[ResponseFormat]/{devId}/{signature}/{timestamp}
        A required step to Authenticate the devId/signature for further API use.
        """
        try:
            tempResponseFormat = self.__responseFormat__
            self.__responseFormat__ = ResponseFormat.JSON
            responseJSON = self.makeRequest("createsession")
            self.__responseFormat__ = tempResponseFormat
            return Session(**responseJSON) if responseJSON else None
        except WrongCredentials as x:
            raise x
    
    def ping(self):
        """
        /ping[ResponseFormat]
        A quick way of validating access to the Hi-Rez API.
        
        Returns
        -------
        Object of :class:`Ping`
            Returns the infos about the API.
        """
        tempResponseFormat = self.__responseFormat__
        self.__responseFormat__ = ResponseFormat.JSON
        responseJSON = self.makeRequest("ping")
        self.__responseFormat__ = tempResponseFormat
        return Ping(responseJSON) if responseJSON else None
    
    def testSession(self, sessionId = None):
        """
        /testsession[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
        A means of validating that a session is established.

        Parameters
        ----------
        sessionId : str
        
        Returns
        -------
        Object of :class:`TestSession`
        """
        session = self.currentSessionId if sessionId is None or not str(sessionId).isalnum() else sessionId
        uri = "{0}/testsession{1}/{2}/{3}/{4}/{5}".format(self.__endpointBaseURL__, self.__responseFormat__, self.__devId__, self.__createSignature__("testsession"), session, self.__createTimeStamp__())
        result = self.__httpRequest__(uri)
        return result.find("successful test") != -1

    def getDataUsed(self):
        """
        /getdataused[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
        Returns API Developer daily usage limits and the current status against those limits.
        
        Returns
        -------
        Object of :class:`DataUsed`

        """
        tempResponseFormat = self.__responseFormat__
        self.__responseFormat__ = ResponseFormat.JSON
        responseJSON = self.makeRequest("getdataused")
        self.__responseFormat__ = tempResponseFormat
        return None if responseJSON is None else DataUsed(**responseJSON) if str(responseJSON).startswith('{') else DataUsed(**responseJSON[0])
    
    def getHiRezServerFeeds(self):
        """
        A quick way of validating access to the Hi-Rez API.
        """
        req = self.__httpRequest__("http://status.hirezstudios.com/history.atom", self.__header__)
        return req
    
    def getHiRezServerStatus(self):
        """
        /gethirezserverstatus[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
        Function returns UP/DOWN status for the primary game/platform environments. Data is cached once a minute.
        
        Returns
        -------
        Object of :class:`HiRezServerStatus`

        """
        tempResponseFormat = self.__responseFormat__
        self.__responseFormat__ = ResponseFormat.JSON
        responseJSON = self.makeRequest("gethirezserverstatus")
        self.__responseFormat__ = tempResponseFormat
        if not responseJSON:
            return None
        servers = []
        for server in responseJSON:
            obj = HiRezServerStatus(**server)
            servers.append(obj)
        return servers if servers else None
        
    def getPatchInfo(self):
        """
        /getpatchinfo[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
        Function returns information about current deployed patch. Currently, this information only includes patch version.
        
        Returns
        -------
        Object of :class:`PatchInfo`

        """
        tempResponseFormat = self.__responseFormat__
        self.__responseFormat__ = ResponseFormat.JSON
        responseJSON = self.makeRequest("getpatchinfo")
        self.__responseFormat__ = tempResponseFormat
        return PatchInfo(**responseJSON) if responseJSON else None
    
    def getFriends(self, playerId):
        """
        /getfriends[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        Returns the User names of each of the player’s friends of one player. [PC only]
        
        Returns
        -------
        list of :class:`Friend` objects
            
        """

        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        responseJSON = self.makeRequest("getfriends", [playerId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return responseJSON
        else:
            if not responseJSON:
                return None
            friends = []
            for friend in responseJSON:
                obj = Friend(**friend)
                friends.append(obj)
            return friends if friends else None

    def getMatchDetails(self, matchId):
        """
        /getmatchdetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{matchId}
        Returns the statistics for a particular completed match.
        
        Parameters
        ----------
        matchId : int
        """
        if not matchId or not str(matchId).isnumeric():
            raise InvalidArgumentException("Invalid Match ID: matchId must to be numeric (int)!")
        responseJSON = self.makeRequest("getmatchdetails", [matchId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return responseJSON
        else:
            if not responseJSON:
                return None
            matchDetails = []
            for matchDetail in responseJSON:
                obj = MatchDetail(**matchDetails)
                matchDetails.append(obj)
            return matchDetails if matchDetails else None
    
    def getMatchDetailsBatch(self, matchIds =()):
        """
        /getmatchdetailsbatch[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{matchId,matchId,matchId,...matchId}
        Returns the statistics for a particular set of completed matches.

        Parameters
        ----------
        matchIds : list

        NOTE
        ----------
        There is a byte limit to the amount of data returned;
        Please limit the CSV parameter to 5 to 10 matches because of this and for Hi-Rez DB Performance reasons.
        
        """
        return self.makeRequest("getmatchdetailsbatch", [matchIds])

    def getMatchHistory(self, playerId):
        """
        /getmatchhistory[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        Gets recent matches and high level match statistics for a particular player.

        Parameters
        ----------
        playerId : int
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        getMatchHistoryResponse = self.makeRequest("getmatchhistory", [playerId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getMatchHistoryResponse
        else:
            if not getMatchHistoryResponse:
                return None
            matchHistorys = []
            for matchHistory in getMatchHistoryResponse:
                obj = MatchHistory(**matchHistory)
                matchHistorys.append(obj)
            return matchHistorys if matchHistorys else None

    def getMatchIdsByQueue(self, queueId, date, hour = -1):
        """
        /getmatchidsbyqueue[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queue}/{date}/{hour}
        Lists all Match IDs for a particular Match Queue; useful for API developers interested in constructing data by Queue.
        To limit the data returned, an {hour} parameter was added (valid values: 0 - 23).
        An {hour} parameter of -1 represents the entire day, but be warned that this may be more data than we can return for certain queues.
        Also, a returned “active_flag” means that there is no match information/stats for the corresponding match.
        Usually due to a match being in-progress, though there could be other reasons.

        Parameters
        ----------
        queueId : int
        date : int
        hour : int

        NOTE
        ----------
        To avoid HTTP timeouts in the GetMatchIdsByQueue() method, you can now specify a 10-minute window within the specified {hour} field to lessen the size of data returned by appending a “,mm” value to the end of {hour}.
        For example, to get the match Ids for the first 10 minutes of hour 3, you would specify {hour} as “3,00”.
        This would only return the Ids between the time 3:00 to 3:09.
        Rules below:
            Only valid values for mm are “00”, “10”, “20”, “30”, “40”, “50”
            To get the entire third hour worth of Match Ids, call GetMatchIdsByQueue() 6 times, specifying the following values for {hour}: “3,00”, “3,10”, “3,20”, “3,30”, “3,40”, “3,50”.
            The standard, full hour format of {hour} = “hh” is still supported.
        """
        getMatchIdsByQueueResponse = self.makeRequest("getmatchidsbyqueue", [queueId, date.strftime("%Y%m%d") if isinstance(date, datetime) else date, hour])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getMatchIdsByQueueResponse
        else:
            if not getMatchIdsByQueueResponse:
                return None
            queueIds = []
            for i in getMatchIdsByQueueResponse:
                obj = MatchIdByQueue(**i)
                queueIds.append(obj)
            return queueIds if queueIds else None

    def getPlayer(self, playerId, portalId = None):
        """
        /getplayer[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{player}
        /getplayer[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{player}/{portalId}
        Returns league and other high level data for a particular player.

        Parameters
        ----------
        playerId : int or str
        """
        if not playerId or len(str(playerId)) <= 3:
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return self.makeRequest("getplayer", [playerId, portalId]) if portalId else self.makeRequest("getplayer", [playerId])
        else:
            if isinstance(self, RealmRoyaleAPI):
                plat = "hirez" if not str(playerId).isdigit() or str(playerId).isdigit() and len(str(playerId)) <= 8 else "steam"
                return PlayerRealmRoyale(**self.makeRequest("getplayer", [playerId, plat]))
            else:
                res = self.makeRequest("getplayer", [playerId, portalId]) if portalId else self.makeRequest("getplayer", [playerId])
                return None if not res else PlayerSmite(**res[0]) if isinstance(self, SmiteAPI) else PlayerPaladins(**res[0])

    def getPlayerAchievements(self, playerId):
        """
        /getplayerachievements[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        Returns select achievement totals (Double kills, Tower Kills, First Bloods, etc) for the specified playerId.

        Parameters
        ----------
        playerId : int
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        getPlayerAchievementsResponse = self.makeRequest("getplayerachievements", [playerId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getPlayerAchievementsResponse
        else:
            if not getPlayerAchievementsResponse:
                return None
            return PlayerAcheviements(**getPlayerAchievementsResponse) if str(getPlayerAchievementsResponse).startswith('{') else PlayerAcheviements(**getPlayerAchievementsResponse[0])

    def getPlayerIdByName(self, playerName):
        """
        /getplayeridbyname[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{playerName}
        Function returns a list of Hi-Rez playerId values (expected list size = 1) for playerName provided. The playerId returned is
        expected to be used in various other endpoints to represent the player/individual regardless of platform.

        Parameters
        ----------
        playerName : str
        """
        getPlayerIdByNameResponse = self.makeRequest("getplayeridbyname", [playerName])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getPlayerIdByNameResponse
        else:
            if not getPlayerIdByNameResponse:
                return None
            playerIds = []
            for i in getPlayerIdByNameResponse:
                obj = PlayerIdByX(**i)
                playerIds.append(obj)
            return playerIds if playerIds else None

    def getPlayerIdByPortalUserId(self, portalId, portalUserId):
        """
        /getplayeridbyportaluserid[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{portalId}/{portalUserId}
        Function returns a list of Hi-Rez playerId values (expected list size = 1) for {portalId}/{portalUserId} combination provided.
        The playerId returned is expected to be used in various other endpoints to represent the player/individual regardless of platform.

        Parameters
        ----------
        portalId : int or str
        portalUserId : int or str
        """
        getPlayerIdByPortalUserIdResponse = self.makeRequest("getplayeridbyportaluserid", [portalId, portalUserId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getPlayerIdByPortalUserIdResponse
        else:
            if not getPlayerIdByPortalUserIdResponse:
                return None
            playerIds = []
            for i in getPlayerIdByPortalUserIdResponse:
                obj = PlayerIdByX(**i)
                playerIds.append(obj)
            return playerIds if playerIds else None

    def getPlayerIdsByGamerTag(self, gamerTag, portalId):
        """
        /getplayeridsbygamertag[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{portalId}/{gamerTag}
        Function returns a list of Hi-Rez playerId values for {portalId}/{portalUserId} combination provided. The appropriate
        playerId extracted from this list by the API end user is expected to be used in various other endpoints to represent the player/individual regardless of platform.

        Parameters
        ----------
        gamerTag : str
        """
        getPlayerIdsByGamerTagResponse = self.makeRequest("getplayeridsbygamertag", [portalId, gamerTag])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getPlayerIdsByGamerTagResponse
        else:
            if not getPlayerIdsByGamerTagResponse:
                return None
            playerIds = []
            for i in getPlayerIdsByGamerTagResponse:
                obj = PlayerIdByX(**i)
                playerIds.append(obj)
            return playerIds if playerIds else None

    def getPlayerStatus(self, playerId):
        """
        /getplayerstatus[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        Returns player status as follows:
            0 - Offline
            1 - In Lobby  (basically anywhere except god selection or in game)
            2 - god Selection (player has accepted match and is selecting god before start of game)
            3 - In Game (match has started)
            4 - Online (player is logged in, but may be blocking broadcast of player state)
            5 - Unknown (player not found)

        Parameters
        ----------
        playerId : int or str
        
        Returns
        -------
        Object of :class:`PlayerStatus`
            
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        getPlayerStatusResponse = self.makeRequest("getplayerstatus", [playerId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getPlayerStatusResponse
        else:
            if not getPlayerStatusResponse:
                return None
            return PlayerStatus(**getPlayerStatusResponse) if str(getPlayerStatusResponse).startswith('{') else PlayerStatus(**getPlayerStatusResponse[0]) if getPlayerStatusResponse else None

    def getQueueStats(self, playerId, queueId):
        """
        /getqueuestats[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}/{queue}
        Returns match summary statistics for a (player, queue) combination grouped by gods played.

        Parameters
        ----------
        playerId : int or str
        queueId : int
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")

        getQueueStatsResponse = self.makeRequest("getqueuestats", [playerId, queueId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getQueueStatsResponse
        else:
            if not getQueueStatsResponse:
                return None
            QueueStats = []
            for i in getQueueStatsResponse:
                obj = QueueStats(**i)
                QueueStats.append(obj)
            return QueueStats if QueueStats else None

class BaseSmitePaladinsAPI(HiRezAPI):
    """
    Class for handling connections and requests to Hi-Rez Studios APIs. IS BETTER DON'T INITALISE THIS YOURSELF!

    Parameters
    ----------
    devId : int
        Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
    authKey : str
        Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
    endpoint : class:`Endpoint`
        The endpoint that will be used by default for outgoing requests.
    responseFormat : [optional] : class:`ResponseFormat`
        The response format that will be used by default when making requests.
        Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
    """
    def __init__(self, devId, authKey, endpoint, responseFormat = ResponseFormat.JSON, sessionId = None):
        """
        Parameters
        ----------
        devId : int
            Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
        authKey : str
            Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
        endpoint : class:`Endpoint`
            The endpoint that will be used by default for outgoing requests.
        responseFormat : [optional] : class:`ResponseFormat`
            The response format that will be used by default when making requests.
            Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
        """
        super().__init__(devId, authKey, endpoint, responseFormat, sessionId)

    def getDemoDetails(self, matchId):
        """
        /getdemodetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{matchId}
        Returns information regarding a particular match.  Rarely used in lieu of getmatchdetails().
        
        Parameters
        ----------
        matchId : int 
        
        """
        if not isinstance(self, PaladinsAPI) and not isinstance(self, SmiteAPI):
            raise NotSupported("This method is just for Paladins and Smite API's!")
        elif not matchId or not str(matchId).isnumeric():
            raise InvalidArgumentException("Invalid Match ID: matchId must to be numeric (int)!")
        getDemoDetailsResponse = self.makeRequest("getdemodetails", [matchId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getDemoDetailsResponse
        else:
            if not getDemoDetailsResponse:
                return None
            demoDetails = []
            for demoDetail in getDemoDetailsResponse:
                obj = SmiteDemoDetail(**demoDetail) if isinstance(self, SmiteAPI) else PaladinsDemoDetail(**demoDetail)
                demoDetails.append(obj)
            return demoDetails if demoDetails else None

    def getEsportsProLeagueDetails(self):
        """
        /getesportsproleaguedetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
        Returns the matchup information for each matchup for the current eSports Pro League season.
        An important return value is “match_status” which represents a match being scheduled (1), in-progress (2), or complete (3)
        """
        if not isinstance(self, PaladinsAPI) and not isinstance(self, SmiteAPI):
            raise NotSupported("This method is just for Paladins and Smite API's!")
        getEsportsProLeagueDetailsResponse = self.makeRequest("getesportsproleaguedetails")
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getEsportsProLeagueDetailsResponse
        else:
            if not getEsportsProLeagueDetailsResponse:
                return None
            details = []
            for detail in getEsportsProLeagueDetailsResponse:
                obj = EsportProLeagueDetail(**detail)
                details.append(obj)
            return details if details else None

    def getGods(self, languageCode = LanguageCode.English):
        """
        /getgods[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{languageCode}
        Returns all Gods and their various attributes.
        
        Parameters
        ----------
        languageCode: [optional] : class: `LanguageCode` : 
        
        Returns
        -------
        Object of :class:`God` or :class:`Champion`
            Returns the infos about the API.

        """
        if not isinstance(self, PaladinsAPI) and not isinstance(self, SmiteAPI):
            raise NotSupported("This method is just for Paladins and Smite API's!")
        getGodsResponse = self.makeRequest("getgods", [languageCode])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getGodsResponse
        else:
            if not getGodsResponse:
                return None
            gods = []
            for i in getGodsResponse:
                obj = God(**i) if isinstance(self, SmiteAPI) else Champion(**i)
                gods.append(obj)
            return gods if gods else None

    def getGodLeaderboard(self, godId, queueId):
        """
        /getgodleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{queue}
        Returns the current season’s leaderboard for a god/queue combination. [SmiteAPI only; queues 440, 450, 451 only]
        
        Parameters
        ----------
        godId: int 
        queueId: int
        """
        getGodLeaderboardResponse = self.makeRequest("getgodleaderboard", [godId, queueId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getGodLeaderboardResponse
        else:
            if not getGodLeaderboardResponse:
                return None
            godLeaderb = []
            for leader in getGodLeaderboardResponse:
                obj = GodLeaderboard(**leader) if isinstance(self, SmiteAPI) else ChampionLeaderboard(**i)
                godLeaderb.append(obj)
            return godLeaderb if godLeaderb else None
    
    def getGodRanks(self, playerId):
        """
        /getgodranks[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        Returns the Rank and Worshippers value for each God a player has played.
        
        Parameters
        ----------
        playerId : int or str
        
        Returns
        -------
        Object of :class:`GodRank`

        """
        if not isinstance(self, PaladinsAPI) and not isinstance(self, SmiteAPI):
            raise NotSupported("This method is just for Paladins and Smite API's!")
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        getGodRanksResponse = self.makeRequest("getgodranks", [playerId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getGodRanksResponse
        else:
            if not getGodRanksResponse:
                return None
            godRanks = []
            for i in getGodRanksResponse:
                godRanks.append(GodRank(**i))
            return godRanks if godRanks else None

    def getGodSkins(self, godId, languageCode = LanguageCode.English):
        """
        /getgodskins[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
        Returns all available skins for a particular God.
        
        Parameters
        ----------
        godId: int : 
        languageCode: :class:`LanguageCode`
        """
        getGodSkinsResponse = self.makeRequest("getgodskins", [godId, languageCode])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getGodSkinsResponse
        else:
            if not getGodSkinsResponse:
                return None
            godSkins = []
            for godSkin in getGodSkinsResponse:
                obj = GodSkin(**godSkin) if isinstance(self, SmiteAPI) != -1 else ChampionSkin(**godSkin)
                godSkins.append(obj)
            return godSkins if godSkins else None

    def getItems(self, languageCode = LanguageCode.English):
        """
        /getitems[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{languageCode}
        Returns all Items and their various attributes.
        
        Parameters
        ----------
        languageCode : [optional] :class:`LanguageCode`
        """
        getItemsResponse = self.makeRequest("getitems", [languageCode])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getItemsResponse
        else:
            if not getItemsResponse:
                return None
            items = []
            for item in getItemsResponse:
                obj = SmiteItem(**item) if isinstance(self, SmiteAPI) != -1 else PaladinsItem(**item)
                items.append(obj)
            return items if items else None

    def getLeagueLeaderboard(self, queueId, tier, split):
        """
        /getleagueleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queue}/{tier}/{split}
        Returns the top players for a particular league (as indicated by the queue/tier/split parameters).

        Parameters
        ----------
        queueId : int
        tier : int
        split : int
        """
        getLeagueLeaderboardResponse = self.makeRequest("getleagueleaderboard", [queueId, tier, split])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getLeagueLeaderboardResponse
        else:
            if not getLeagueLeaderboardResponse:
                return None
            leagueLeaderboards = []
            for leaderboard in getLeagueLeaderboardResponse:
                obj = LeagueLeaderboard(**leaderboard)
                leagueLeaderboards.append(obj)
            return leagueLeaderboards if leagueLeaderboards else None
        
    def getLeagueSeasons(self, queueId):
        """
        /getleagueseasons[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queueId}
        Provides a list of seasons (including the single active season) for a match queue.

        Parameters
        ----------
        queueId : int
        """
        getLeagueSeasonsResponse = self.makeRequest("getleagueseasons", [queueId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getLeagueSeasonsResponse
        else:
            if not getLeagueSeasonsResponse:
                return None
            seasons = []
            for season in getLeagueSeasonsResponse:
                obj = LeagueSeason(**season)
                items.append(obj)
            return seasons if seasons else None

    def getMatchPlayerDetails(self, matchId):
        """
        /getmatchplayerdetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{matchId}
        Returns player information for a live match.

        Parameters
        ----------
        matchId : int
        """
        if not matchId or not str(matchId).isnumeric():
            raise InvalidArgumentException("Invalid Match ID: matchId must to be numeric (int)!")
        responseJSON = self.makeRequest("getmatchplayerdetails", [matchId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return responseJSON
        else:
            if not responseJSON:
                return None
            players = []
            for player in responseJSON:
                obj = MatchPlayerDetail(**player)
                players.append(obj)
            return players if players else None

class PaladinsAPI(BaseSmitePaladinsAPI):
    """
    Class for handling connections and requests to Paladins API.

    Parameters
    ----------
    devId : int
        Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
    authKey : str
        Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
    endpoint : class:`Endpoint`
        The endpoint that will be used by default for outgoing requests.
    responseFormat : [optional] : class:`ResponseFormat`
        The response format that will be used by default when making requests.
        Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
    """
    def __init__(self, devId, authKey, responseFormat = ResponseFormat.JSON, sessionId = None):
        """
        Parameters
        ----------
        devId : int
            Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
        authKey : str
            Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
        endpoint : class:`Endpoint`
            The endpoint that will be used by default for outgoing requests.
        responseFormat : [optional] : class:`ResponseFormat`
            The response format that will be used by default when making requests.
            Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
        """
        super().__init__(devId, authKey, Endpoint.PALADINS, responseFormat, sessionId)

    def getLatestPatchNotes(self, languageCode = LanguageCode.English):
        getLatestUpdateNotesResponse = self.makeRequest("https://cms.paladins.com/wp-json/api/get-posts/{0}?tag=update-notes".format(languageCode.value if isinstance(languageCode, LanguageCode) else languageCode))
        if not getLatestUpdateNotesResponse:
            return None
        post = PaladinsWebsitePost(**getLatestUpdateNotesResponse[0])
        getLatestPatchNotesResponse = self.makeRequest("https://cms.paladins.com/wp-json/api/get-post/{0}?slug={1}".format(languageCode.value if isinstance(languageCode, LanguageCode) else languageCode, post.slug))
        return PaladinsWebsitePost(**getLatestPatchNotesResponse) if  getLatestPatchNotesResponse else None
    def getPaladinsWebsitePostBySlug(self, slug, languageCode = LanguageCode.English):
        getPaladinsWebsitePostsResponse = self.makeRequest("https://cms.paladins.com/wp-json/api/get-post/{0}?slug={1}".format(languageCode.value if isinstance(languageCode, LanguageCode) else languageCode, slug))
        if not getPaladinsWebsitePostsResponse:
            return None
        posts = []
        for post in getPaladinsWebsitePostsResponse:
            obj = PaladinsWebsitePost(**post)
            posts.append(obj)
        return posts if posts else None
    def getPaladinsWebsitePosts(self, languageCode = LanguageCode.English):
        getPaladinsWebsitePostsResponse = self.makeRequest("https://cms.paladins.com/wp-json/api/get-posts/{0}".format(languageCode.value if isinstance(languageCode, LanguageCode) else languageCode))
        if not getPaladinsWebsitePostsResponse:
            return None
        posts = []
        for post in getPaladinsWebsitePostsResponse:
            obj = PaladinsWebsitePost(**post)
            posts.append(obj)
        return posts if posts else None
    def getPaladinsWebsitePostsByQuery(self, query, languageCode = LanguageCode.English):
        getPaladinsWebsitePostsResponse = self.makeRequest("https://cms.paladins.com/wp-json/api/get-posts/{0}?search={1}".format(languageCode.value if isinstance(languageCode, LanguageCode) else languageCode, query))
        if not getPaladinsWebsitePostsResponse:
            return None
        posts = []
        for post in getPaladinsWebsitePostsResponse:
            obj = PaladinsWebsitePost(**post)
            posts.append(obj)
        return posts if posts else None
    
    def getChampions(self, languageCode = LanguageCode.English):
        """
        /getchampions[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{languageCode}
        Returns all Champions and their various attributes. [PaladinsAPI only]

        Parameters
        ----------
        languageCode: [optional] : class:`LanguageCode`:  
        """
        getChampionsResponse = self.makeRequest("getchampions", [languageCode]) # self.makeRequest("getgods", languageCode)
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getChampionsResponse
        else:
            if not getChampionsResponse:
                return None
            champions = []
            for i in getChampionsResponse:
                obj = Champion(**i)
                champions.append(obj)
            return champions if champions else None

    def getChampionsCards(self, godId, languageCode = LanguageCode.English):
        """
        /getchampioncards[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
        Returns all Champion cards. [PaladinsAPI only]

        Parameters
        ----------
        languageCode: [optional] : class:`LanguageCode`:  
        """
        getChampionsCardsResponse = self.makeRequest("getchampioncards", [godId, languageCode])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getChampionsCardsResponse
        else:
            if not getChampionsCardsResponse:
                return None
            cards = []
            for i in getChampionsCardsResponse:
                obj = ChampionCard(**i)
                cards.append(obj)
            return cards if cards else None

    def getChampionLeaderboard(self, godId, queueId = PaladinsQueue.Live_Competitive_Keyboard):
        """
        /getchampionleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{queueId}
        Returns the current season’s leaderboard for a champion/queue combination. [PaladinsAPI; only queue 428]
        
        Parameters
        ----------
        godId : int
        queueId : int
        """
        if not godId or len(str(godId)) != 4:
            raise InvalidArgumentException("Invalid God ID: godId must to be numeric (int)!")
        getChampionLeaderboardResponse = self.makeRequest("getchampionleaderboard", [godId, queueId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getChampionLeaderboardResponse
        else:
            if not getChampionLeaderboardResponse:
                return None
            getChampionLeaderboard = []
            for i in getChampionLeaderboardResponse:
                obj = ChampionLeaderboard(**i)
                getChampionLeaderboard.append(obj)
            return getChampionLeaderboard if getChampionLeaderboard else None

    def getChampionRanks(self, playerId):
        """
        /getchampionranks[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        Returns the Rank and Worshippers value for each Champion a player has played. [PaladinsAPI only]
        
        Parameters
        ----------
        playerId : int or str
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        getChampionsRanksResponse = self.makeRequest("getgodranks", [playerId]) # self.makeRequest("getchampionranks", [playerId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getChampionsRanksResponse
        else:
            if not getChampionsRanksResponse:
                return None
            championRanks = []
            for i in getChampionsRanksResponse:
                championRanks.append(GodRank(**i))
            return championRanks if championRanks else None

    def getChampionRecommendedItems(self, godId, languageCode = LanguageCode.English):
        """
        /getchampionrecommendeditems[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
        Returns the Recommended Items for a particular Champion. [PaladinsAPI only]
        
        Parameters
        ----------
        godId : int 
        languageCode : class:`LanguageCode`
        
        Warning
        ----------
        OSBSOLETE - NO DATA RETURNED
        """
        raise DeprecatedException("OSBSOLETE - NO DATA RETURNED")
        return self.makeRequest("getchampionrecommendeditems", [godId, languageCode])
        
    def getChampionSkins(self, godId, languageCode = LanguageCode.English):
        """
        /getchampionskins[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
        Returns all available skins for a particular Champion. [PaladinsAPI only]
        
        Parameters
        ----------
        godId : int
        languageCode :class:`LanguageCode`
        """
        getChampSkinsResponse = self.makeRequest("getchampionskins", [godId, languageCode])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getChampSkinsResponse
        else:
            if not getChampSkinsResponse:
                return None
            champSkins = []
            for champSkin in getChampSkinsResponse:
                obj = ChampionSkin(**champSkin)
                champSkins.append(obj)
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
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getPlayerIdInfoForXboxAndSwitchResponse
        else:
            if not getPlayerIdInfoForXboxAndSwitchResponse:
                return None
            playerIds = []
            for playerId in getPlayerIdInfoForXboxAndSwitchResponse:
                obj = PlayerIdInfoForXboxOrSwitch(**playerId)
                playerIds.append(obj)
            return playerIds if playerIds else None

    def getPlayerLoadouts(self, playerId, languageCode = LanguageCode.English):
        """
        /getplayerloadouts[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/playerId}/{languageCode}
        Returns deck loadouts per Champion. [PaladinsAPI only]
        
        Parameters
        ----------
        playerId : int or str
        languageCode: :class:`LanguageCode`
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        getPlayerLoadoutsResponse = self.makeRequest("getplayerloadouts", [playerId, languageCode])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getPlayerLoadoutsResponse
        else:
            if not getPlayerLoadoutsResponse:
                return None
            playerLoadouts = []
            for playerLoadout in getPlayerLoadoutsResponse:
                obj = PlayerLoadout(**playerLoadout)
                playerLoadouts.append(obj)
            return playerLoadouts if playerLoadouts else None
        
class RealmRoyaleAPI(HiRezAPI):
    """
    Class for handling connections and requests to Realm Royale API.

    Parameters
    ----------
    devId : int
        Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
    authKey : str
        Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
    endpoint : class:`Endpoint`
        The endpoint that will be used by default for outgoing requests.
    responseFormat : [optional] : class:`ResponseFormat`
        The response format that will be used by default when making requests.
        Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
    """
    def __init__(self, devId, authKey, responseFormat = ResponseFormat.JSON, sessionId = None):
        """
        Parameters
        ----------
        devId : int
            Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
        authKey : str
            Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
        endpoint : class:`Endpoint`
            The endpoint that will be used by default for outgoing requests.
        responseFormat : [optional] : class:`ResponseFormat`
            The response format that will be used by default when making requests.
            Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
        """
        super().__init__(devId, authKey, Endpoint.REALM_ROYALE, responseFormat, sessionId)

    def getLeaderboard(self, queueId, rankingCriteria):
        """
        /getleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queueId}/{ranking_criteria}

        - for duo and quad queues/modes the individual's placement results reflect their team/grouping; solo is self-explanatory
        - will limit results to the top 500 players (minimum 50 matches played per queue); we never like to expose weak/beginner players
        - players that select to be "private" will have their player_name and player_id values hidden
        - {ranking_criteria} can be: 1: team_wins, 2: team_average_placement (shown below), 3: individual_average_kills, 4. win_rate, possibly/probably others as desired
        - expect this data to be cached on an hourly basis because the query to acquire the data will be expensive; don't spam the calls
        """
        getLeaderboardResponse = self.makeRequest("getleaderboard", [queueId, rankingCriteria])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getLeaderboardResponse
        else:
            return RealmRoyaleLeaderboard(**getLeaderboardResponse) if getLeaderboardResponse else None

    def getPlayerMatchHistory(self, playerId):
        """
        /getplayermatchhistory[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        getPlayerMatchHistoryResponse = self.makeRequest("getplayermatchhistory", [playerId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getPlayerMatchHistoryResponse
        else:
            return RealmMatchHistory(**getPlayerMatchHistoryResponse) if getPlayerMatchHistoryResponse else None

    def getPlayerMatchHistoryAfterDatetime(self, playerId, startDatetime):
        """
        /getplayermatchhistoryafterdatetime[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}/{startDatetime}
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        getPlayerMatchHistoryAfterDatetimeResponse = self.makeRequest("getplayermatchhistoryafterdatetime", [playerId, startDatetime.strftime("yyyyMMddHHmmss") if isinstance(startDatetime, datetime) else startDatetime])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getPlayerMatchHistoryAfterDatetimeResponse
        else:
            return RealmMatchHistory(**getPlayerMatchHistoryAfterDatetimeResponse) if getPlayerMatchHistoryAfterDatetimeResponse else None

    def getPlayerStats(self, playerId):
        """ 
       /getplayerstats[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        """
        if not playerId or not str(playerId).isnumeric():
            raise InvalidArgumentException("Invalid player: playerId must to be numeric (int)!")
        return self.makeRequest("getplayerstats", [playerId])

    def getTalents(self, languageCode = LanguageCode.English):
        """
        /gettalents[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{langId}
        Get all talents
        """
        if not languageCode or not str(languageCode).isnumeric() or not isinstance(language, LanguageCode):
            raise InvalidArgumentException("Invalid LangId!")
        responseJSON = self.makeRequest("gettalents", [languageCode])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return responseJSON
        else:
            if not responseJSON:
                return None
            talents = []
            for talent in responseJSON:
                obj = RealmRoyaleTalent(**talent)
                talents.append(obj)
            return talents if talents else None

    def searchPlayers(self, playerName):
        """
        /searchplayers[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerName}
        """
        searchPlayerResponse = self.makeRequest("searchplayers", [playerName])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return searchPlayerResponse
        else:
            if not searchPlayerResponse:
                return None
            players = []
            for player in searchPlayerResponse:
                obj = Player(**player)
                players.append(obj)
            return players if players else None

class SmiteAPI(BaseSmitePaladinsAPI):
    """
    Class for handling connections and requests to Smite API.

    Parameters
    ----------
    devId : int
        Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
    authKey : str
        Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
    endpoint : class:`Endpoint`
        The endpoint that will be used by default for outgoing requests.
    responseFormat : [optional] : class:`ResponseFormat`
        The response format that will be used by default when making requests.
        Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
    """
    def __init__(self, devId, authKey, responseFormat = ResponseFormat.JSON, sessionId = None):
        """
        Parameters
        ----------
        devId : int
            Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
        authKey : str
            Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
        endpoint : class:`Endpoint`
            The endpoint that will be used by default for outgoing requests.
        responseFormat : [optional] : class:`ResponseFormat`
            The response format that will be used by default when making requests.
            Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
        """
        super().__init__(devId, authKey, Endpoint.SMITE, responseFormat, sessionId)

    def getGodRecommendedItems(self, godId, languageCode = LanguageCode.English):
        """
        /getgodrecommendeditems[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
        Returns the Recommended Items for a particular God. [SmiteAPI only]
        
        Parameters
        ----------
        godId : int
        languageCode : [optional] : class: `LanguageCode` : 
        """
        getGodRecommendedItemsResponse = self.makeRequest("getgodrecommendeditems", [godId, languageCode])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getGodRecommendedItemsResponse
        else:
            if not getGodRecommendedItemsResponse:
                return None
            recommendedItems = []
            for recommendedItem in getGodRecommendedItemsResponse:
                obj = GodRecommendedItem(**recommendedItem)
                recommendedItems.append(obj)
            return recommendedItems if recommendedItems else None

    def getMotd(self):
        """
        /getmotd[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
        Returns information about the 20 most recent Match-of-the-Days.
        """
        getMOTDResponse = self.makeRequest("getmotd")
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getMOTDResponse
        else:
            if not getMOTDResponse:
                return None
            motds = []
            for motd in getMOTDResponse:
                obj = MOTD(**motd)
                motds.append(obj)
            return motds if motds else None

    def getTeamDetails(self, clanId):
        """
        /getteamdetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{clanId}
        Lists the number of players and other high level details for a particular clan.
        
        Parameters
        ----------
        clanId: int
        """
        if not clanId or not str(clanId).isnumeric():
            raise InvalidArgumentException("Invalid Clan ID: clanId must to be numeric (int)!")
        getTeamDetailsResponse = self.makeRequest("getteamdetails", [clanId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getTeamDetailsResponse
        else:
            if not getTeamDetailsResponse:
                return None
            teamDetails = []
            for teamDetail in getTeamDetailsResponse:
                obj = TeamDetail(**teamDetail)
                teamDetails.append(obj)
            return teamDetails if teamDetails else None
    
    def getTeamMatchHistory(self, clanId):
        """
        *DEPRECATED*

        /getteammatchhistory[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{clanId}
        Gets recent matches and high level match statistics for a particular clan/team.
        """
        raise DeprecatedException("*DEPRECATED* - As of 2.14 Patch, /getteammatchhistory is no longer supported and will return a NULL dataset.")
        if not clanId or not str(clanId).isnumeric():
            raise InvalidArgumentException("Invalid Clan ID: clanId must to be numeric (int)!")
        return self.makeRequest("getteammatchhistory", [clanId])

    def getTeamPlayers(self, clanId):
        """
        /getteamplayers[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{clanId}
        Lists the players for a particular clan.
        
        Parameters
        ----------
        clanId: int
        """
        if not clanId or not str(clanId).isnumeric():
            raise InvalidArgumentException("Invalid Clan ID: clanId must to be numeric (int)!")
        getTeamPlayers = self.makeRequest("getteamplayers", [clanId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getTeamPlayers
        else:
            if not getTeamPlayers:
                return None
            teamPlayers = []
            for teamPlayer in getTeamPlayers:
                obj = TeamPlayer(**teamPlayer)
                teamPlayers.append(obj)
            return teamPlayers if teamPlayers else None

    def getTopMatches(self):
        """
        /gettopmatches[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
        Lists the 50 most watched / most recent recorded matches.
        """
        getTopMatchesResponse = self.makeRequest("gettopmatches")
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getTopMatchesResponse
        else:
            if not getTopMatchesResponse:
                return None
            matches = []
            for match in getTopMatchesResponse:
                obj = SmiteTopMatch(**match)
                matches.append(obj)
            return matches if matches else None
    def searchTeams(self, teamId):
        """
        /searchteams[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{searchTeam}
        Returns high level information for Clan names containing the “searchTeam” string. [SmiteAPI only]
        
        Parameters
        ----------
        teamId: int
        """
        getSearchTeamsResponse = self.makeRequest("searchteams", [teamId])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.XML).lower():
            return getSearchTeamsResponse
        else:
            if not getSearchTeamsResponse:
                return None
            teams = []
            for team in getSearchTeamsResponse:
                obj = TeamSearch(**team)
                teams.append(obj)
            return teams if teams else None

class HandOfTheGodsAPI(HiRezAPI):
    """
    Class for handling connections and requests to Hand of the Gods API.

    Parameters
    ----------
    devId : int
        Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
    authKey : str
        Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
    endpoint : class:`Endpoint`
        The endpoint that will be used by default for outgoing requests.
    responseFormat : [optional] : class:`ResponseFormat`
        The response format that will be used by default when making requests.
        Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
    """
    def __init__(self, devId, authKey, responseFormat = ResponseFormat.JSON, sessionId = None):
        """
        Parameters
        ----------
        devId : int
            Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
        authKey : str
            Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
        endpoint : class:`Endpoint`
            The endpoint that will be used by default for outgoing requests.
        responseFormat : [optional] : class:`ResponseFormat`
            The response format that will be used by default when making requests.
            Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
        """
        raise NotSupported("Not released yet!")
        super().__init__(devId, authKey, Endpoint.HAND_OF_THE_GODS, responseFormat, sessionId)

class PaladinsStrikeAPI(HiRezAPI):
    """
    Class for handling connections and requests to Paladins Strike API.

    Parameters
    ----------
    devId : int
        Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
    authKey : str
        Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
    endpoint : class:`Endpoint`
        The endpoint that will be used by default for outgoing requests.
    responseFormat : [optional] : class:`ResponseFormat`
        The response format that will be used by default when making requests.
        Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
    """
    def __init__(self, devId, authKey, responseFormat = ResponseFormat.JSON, sessionId = None):
        """
        Parameters
        ----------
        devId : int
            Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
        authKey : str
            Used for authentication. This is the authentication key that you receive from Hi-Rez Studios.
        endpoint : class:`Endpoint`
            The endpoint that will be used by default for outgoing requests.
        responseFormat : [optional] : class:`ResponseFormat`
            The response format that will be used by default when making requests.
            Otherwise, this will be used. It defaults to class:`ResponseFormat.JSON`.
        """
        raise NotSupported("Not released yet!")
        super().__init__(devId, authKey, Endpoint.PALADINS_STRIKE, responseFormat, sessionId)
