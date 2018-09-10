from datetime import timedelta, datetime
from hashlib import md5 as getMD5Hash
from sys import version_info as pythonVersion
import requests

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
            raise KeyOrAuthEmptyException("DevKey or AuthKey not specified!")
        elif len(str(devId)) < 4 or len(str(devId)) > 5 or not str(devId).isnumeric():
            raise InvalidArgumentException("You need to pass a valid DevId!")
        elif len(str(authKey)) != 32 or not str(authKey).isalnum():
            raise InvalidArgumentException("You need to pass a valid AuthKey!")
        elif len(str(endpoint)) == 0 :
            raise InvalidArgumentException("Endpoint can't be empty!")
        self.__devId__ = int(devId)
        self.__authKey__ = str(authKey)
        self.__endpointBaseURL__ = str(endpoint)
        self.__responseFormat__ = ResponseFormat(responseFormat) if(responseFormat == ResponseFormat.JSON or responseFormat == ResponseFormat.XML) else ResponseFormat.JSON
        self.__header__ = header

    def __encode__(self, string, encodeType = "utf-8"):
        return str(string).encode(encodeType)

    def __decode__(self, string, encodeType = "utf-8"):
        return str(string).encode(encodeType)

    def __httpRequest__(self, url, header = None):
        httpResponse = HttpRequest(header if header else self.__header__).get(url)
        if httpResponse.status_code >= 400:
            raise NotFoundException("Wrong URL: " + httpResponse.text)
        if httpResponse.status_code == 200:
            try:
                return httpResponse.json()
            except:
                return httpResponse.text
        
class HiRezAPI(BaseAPI):
    """
    Class for handling connections and requests to Hi Rez Studios APIs. IS BETTER DON'T INITALISE THIS YOURSELF!

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

    def __init__(self, devId, authKey, endpoint, responseFormat = ResponseFormat.JSON):
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
        return self.currentSession is None
        #return self.currentSession is None or self.currentSession.isApproved() and self.__currentTime__() - self.currentSession.timeStamp >= timedelta(minutes = 15)

    def __buildUrlRequest__(self, apiMethod, params =()): # [queue, date, hour]
        if len(str(apiMethod)) == 0:
            raise InvalidArgumentException("No API method specified!")
        #urlRequest = '/'.join(self.__endpointBaseURL__, apiMethod.lower(), self.__responseFormat__)
        urlRequest = "{0}/{1}{2}".format(self.__endpointBaseURL__, apiMethod.lower(), self.__responseFormat__)
        if apiMethod.lower() != "ping":
            urlRequest += "/{0}/{1}".format(self.__devId__, self.__createSignature__(apiMethod.lower()))
            if self.currentSession != None and apiMethod.lower() != "createsession":
                urlRequest += "/{0}".format(self.currentSession.sessionId)
            urlRequest += "/{0}".format(self.__createTimeStamp__())
            #if self.currentSession != None and apiMethod.lower() != "createsession":
                #urlRequest = [ self.__endpointBaseURL__, apiMethod.lower(), self.__responseFormat__, self.dev_id, self.__createSignature__(apiMethod.lower()), self.currentSession.sessionId, self.currentSession.sessionId, self.__createTimeStamp__() ]
            #else:
                #urlRequest = [ self.__endpointBaseURL__, apiMethod.lower(), self.__responseFormat__, self.dev_id, self.__createSignature__(apiMethod.lower()), self.currentSession.sessionId, self.__createTimeStamp__() ]
            if params:
                #urlRequest += "/" + [str(param) for param in params]
                #stringParam += param.strftime("yyyyMMdd") if isinstance(param, datetime) else(param is Enums.QueueType || param is Enums.eLanguageCode) ?((int) param).ToString() : str(param);
                for param in params:
                    if param != None:
                        urlRequest += '/' + str(param)
        return urlRequest.replace(' ', "%20")

    def makeRequest(self, apiMethod, params =()):
        if len(str(apiMethod)) == 0:
            raise InvalidArgumentException("No API method specified!")
        elif(apiMethod.lower() != "createsession" and self.__sessionExpired__):
            self.__createSession__()
        result = self.__httpRequest__(apiMethod if str(apiMethod).lower().startswith("http") else self.__buildUrlRequest__(apiMethod, params))
        if result:
            if str(self.__responseFormat__).lower() == str(ResponseFormat.JSON).lower():
                if str(result).lower().find("ret_msg") == -1:
                    return None if len(str(result)) == 2 and str(result) == "[]" else result
                else:
                    foundProblem = False
                    hasError = APIResponse(**result) if str(result).startswith('{') else APIResponse(**result[0])
                    if hasError != None and hasError.retMsg != None and hasError.retMsg.lower() != "approved":
                        foundProblem = not foundProblem
                        if hasError.retMsg.find("dailylimit") != -1:
                            raise DailyLimitException("Daily limit reached: " + hasError.retMsg)
                        elif hasError.retMsg.find("Maximum number of active sessions reached") != -1:
                            raise SessionLimitException("Concurrent sessions limit reached: " + hasError.retMsg)
                        elif hasError.retMsg.find("Invalid session id") != -1:
                            self.__createSession__()
                            return self.makeRequest(apiMethod, params)
                        elif hasError.retMsg.find("Exception while validating developer access") != -1:
                            raise WrongCredentials("Wrong credentials: " + hasError.retMsg)
                        elif hasError.retMsg.find("404") != -1:
                            raise NotFoundException("Not found: " + hasError.retMsg)
                    if not foundProblem:
                        return result
            else:
                return result

    def setSession(self, sessionID):
        if not str(sessionID).isalnum():
            raise InvalidArgumentException("SessionID invalid! It need to be alphanum!")
        newSession = Session ()
        newSession.sessionId = sessionID
        self.currentSession = newSession

    def switchEndpoint(self, endpoint):
        if not isinstance(endpoint, Endpoint):
            raise InvalidArgumentException("You need to use the Endpoint enum to switch endpoints")
        self.__endpointBaseURL__ = str(endpoint)

    def __createSession__(self):
        """
        /createsession[ResponseFormat]/{developerId}/{signature}/{timestamp}
        A required step to Authenticate the developerId/signature for further API use.
        """
        try:
            tempResponseFormat = self.__responseFormat__
            self.__responseFormat__ = ResponseFormat.JSON
            responseJSON = self.makeRequest("createsession")
            if responseJSON:
                self.currentSession = Session(**responseJSON)
            self.__responseFormat__ = tempResponseFormat
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
    
    #Se eu usar testSession primeiro, olhar se foi sucesso e setar o sessionId?
    def testSession(self, sessionId = None):
        """
        /testsession[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
        A means of validating that a session is established.

        Parameters
        ----------
        sessionId : str
        
        Returns
        -------
        Object of :class:`TestSession`
        """
        tempResponseFormat = self.__responseFormat__
        self.__responseFormat__ = ResponseFormat.JSON
        session = self.currentSession.sessionId if sessionId is None or not str(sessionId).isalnum() else sessionId
        uri = "{0}/testsession{1}/{2}/{3}/{4}/{5}".format(self.__endpointBaseURL__, self.__responseFormat__, self.__devId__, self.__createSignature__("testsession"), session, self.__createTimeStamp__())
        responseJSON = self.makeRequest(uri)
        self.__responseFormat__ = tempResponseFormat
        return TestSession(responseJSON) if responseJSON else None

    def getDataUsed(self):
        """
        /getdataused[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
        Returns API Developer daily usage limits and the current status against those limits.
        
        Returns
        -------
        Object of :class:`DataUsed`

        """
        tempResponseFormat = self.__responseFormat__
        self.__responseFormat__ = ResponseFormat.JSON
        responseJSON = self.makeRequest("getdataused")
        self.__responseFormat__ = tempResponseFormat
        return DataUsed(**responseJSON) if str(responseJSON).startswith('{') else DataUsed(**responseJSON[0]) if responseJSON else None
    
    def getHiRezServerFeeds(self):
        """
        A quick way of validating access to the Hi-Rez API.
        """
        req = self.__httpRequest__("http://status.hirezstudios.com/history.atom", self.__header__)
        return req
    
    def getHiRezServerStatus(self):
        """
        /gethirezserverstatus[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
        Function returns UP/DOWN status for the primary game/platform environments. Data is cached once a minute.
        
        Returns
        -------
        Object of :class:`HiRezServerStatus`

        """
        tempResponseFormat = self.__responseFormat__
        self.__responseFormat__ = ResponseFormat.JSON
        responseJSON = self.makeRequest("gethirezserverstatus")
        self.__responseFormat__ = tempResponseFormat
        return HiRezServerStatus(**responseJSON) if str(responseJSON).startswith('{') else HiRezServerStatus(**responseJSON[0]) if responseJSON else None

    def getPatchInfo(self):
        """
        /getpatchinfo[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
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
    
    def getEsportsProLeagueDetails(self):
        """
        /getesportsproleaguedetails[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
        Returns the matchup information for each matchup for the current eSports Pro League season.
        An important return value is “match_status” which represents a match being scheduled (1), in-progress (2), or complete (3)
        """
        return self.makeRequest("getesportsproleaguedetails")

    def getFriends(self, playerID):
        """
        /getfriends[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
        Returns the User names of each of the player’s friends of one player. [PC only]
        
        Returns
        -------
        list of :class:`Friend` objects
            
        """

        if not playerID or len(playerID) <= 3:
            raise InvalidArgumentException("Invalid player!")
        else:
            if str(self.__responseFormat__).lower() == str(ResponseFormat.JSON).lower():
                responseJSON = self.makeRequest("getfriends", [playerID])
                friends = []
                for friend in responseJSON:
                    friends.append(Friend(**friend))
                return friends if friends else None
            else:
                return self.makeRequest("getfriends", [playerID])

    def getItems(self, language = LanguageCode.English):
        """
        /getitems[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{languagecode}
        Returns all Items and their various attributes.
        
        Parameters
        ----------
        language : [optional] :class:`LanguageCode`
        """
        return self.makeRequest("getitems", [language])

    def getLeagueLeaderboard(self, queueID, tier, season):
        """
        /getleagueleaderboard[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{queue}/{tier}/{season}
        Returns the top players for a particular league (as indicated by the queue/tier/season parameters).

        Parameters
        ----------
        queueID : int
        tier : int
        season : int
        """
        return self.makeRequest("getleagueleaderboard", [queueID, tier, season])

    def getLeagueSeasons(self, queueID):
        """
        /getleagueseasons[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{queue}
        Provides a list of seasons (including the single active season) for a match queue.

        Parameters
        ----------
        queueID : int
        """
        return self.makeRequest("getleagueseasons", [queueID])
    
    def getMatchDetails(self, matchID):
        """
        /getmatchdetails[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{match_id}
        Returns the statistics for a particular completed match.
        
        Parameters
        ----------
        matchID : int
        """
        return self.makeRequest("getmatchdetails", [matchID])
    
    def getMatchDetailsBatch(self, matchID =()): #5-10 partidas
        """
        /getmatchdetailsbatch[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{match_id,match_id,match_id,...match_id}
        Returns the statistics for a particular set of completed matches.

        Parameters
        ----------
        matchID : list

        NOTE
        ----------
        There is a byte limit to the amount of data returned;
        Please limit the CSV parameter to 5 to 10 matches because of this and for Hi-Rez DB Performance reasons.
        
        """
        return self.makeRequest("getmatchdetailsbatch", [matchID])

    def getMatchHistory(self, playerID):
        """
        /getmatchhistory[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
        Gets recent matches and high level match statistics for a particular player.

        Parameters
        ----------
        playerID : int
        """
        if not playerID or len(playerID) <= 3:
            raise InvalidArgumentException("Invalid player!")
        getMatchHistoryResponse = self.makeRequest("getmatchhistory", [playerID])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.JSON).lower():
            matchHistorys = []
            for i in range(0, len(getMatchHistoryResponse)):
                obj = MatchHistory(**getMatchHistoryResponse[i])
                matchHistorys.append(obj)
            return matchHistorys if matchHistorys else None
        else:
            return getMatchHistoryResponse

    def getMatchIdsByQueue(self, queueID, date, hour = -1):
        """
        /getmatchidsbyqueue[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{queue}/{date}/{hour}
        Lists all Match IDs for a particular Match Queue; useful for API developers interested in constructing data by Queue.
        To limit the data returned, an {hour} parameter was added (valid values: 0 - 23).
        An {hour} parameter of -1 represents the entire day, but be warned that this may be more data than we can return for certain queues.
        Also, a returned “active_flag” means that there is no match information/stats for the corresponding match.
        Usually due to a match being in-progress, though there could be other reasons.

        Parameters
        ----------
        queueID : int
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
        return self.makeRequest("getmatchidsbyqueue", [queueID, date.strftime("%Y%m%d") if isinstance(date, datetime) else date, hour])

    def getMatchPlayerDetails(self, matchID):
        """
        /getmatchplayerdetails[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{match_id}
        Returns player information for a live match.

        Parameters
        ----------
        matchID : int
        """
        return self.makeRequest("getmatchplayerdetails", [matchID])

    def getPlayer(self, playerID):
        """
        /getplayer[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
        Returns league and other high level data for a particular player.

        Parameters
        ----------
        playerID : int or str
        """
        if not playerID or len(playerID) <= 3:
            raise InvalidArgumentException("Invalid player!")
        if str(self.__responseFormat__).lower() == str(ResponseFormat.JSON).lower():
            if isinstance(self, RealmRoyaleAPI):
                plat = "hirez" if not str(playerID).isdigit() or str(playerID).isdigit() and len(str(playerID)) <= 8 else "steam"
                return PlayerRealmRoyale(**self.makeRequest("getplayer", [playerID, plat]))
            else:
                res = self.makeRequest("getplayer", [playerID])[0]
                return PlayerSmite(**res) if isinstance(self, SmiteAPI) else BasePSPlayer(**res)
        else:
            return self.makeRequest("getplayer", [playerID])

    def getPlayerAchievements(self, playerID):
        """
        /getplayerachievements[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{playerId}
        Returns select achievement totals (Double kills, Tower Kills, First Bloods, etc) for the specified playerId.

        Parameters
        ----------
        playerID : int or str
        """
        if(len(playerID) <= 3):
            raise InvalidArgumentException("Invalid player!")
        return self.makeRequest("getplayerachievements", [playerID])

    def getPlayerStatus(self, playerID):
        """
        /getplayerstatus[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
        Returns player status as follows:
            0 - Offline
            1 - In Lobby  (basically anywhere except god selection or in game)
            2 - god Selection (player has accepted match and is selecting god before start of game)
            3 - In Game (match has started)
            4 - Online (player is logged in, but may be blocking broadcast of player state)
            5 - Unknown (player not found)

        Parameters
        ----------
        playerID : int or str
        
        Returns
        -------
        Object of :class:`PlayerStatus`
            
        """
        if not playerID or len(playerID) <= 3:
            raise InvalidArgumentException("Invalid player!")
        if str(self.__responseFormat__).lower() == str(ResponseFormat.JSON).lower():
            responseJSON = self.makeRequest("getplayerstatus", [playerID])
            return PlayerStatus(**responseJSON) if str(responseJSON).startswith('{') else PlayerStatus(**responseJSON[0]) if responseJSON else None
        else:
            return self.makeRequest("getplayerstatus", [playerID])

    def getQueueStats(self, playerID, queueID):
        """
        /getqueuestats[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}/{queue}
        Returns match summary statistics for a (player, queue) combination grouped by gods played.

        Parameters
        ----------
        playerID : int or str
        queueID : int
        """
        if not playerID or len(playerID) <= 3:
            raise NotFoundException("Invalid player!")
        return self.makeRequest("getqueuestats", [playerID, queueID])

class PaladinsAPI(HiRezAPI):
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
    def __init__(self, devId, authKey, platform = Platform.PC, responseFormat = ResponseFormat.JSON):
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
        if platform == Platform.MOBILE:
            raise NotSupported("Not released yet!")
        else:
            endpoint = Endpoint.PALADINS_XBOX if platform == Platform.XBOX or platform == Platform.NINTENDO_SWITCH else Endpoint.PALADINS_PS4 if platform == Platform.PS4 else Endpoint.PALADINS_PC
            super().__init__(int(devId), str(authKey), endpoint, responseFormat)

    def switchPlatform(self, platform):
        if not isinstance(endpoint, Platform):
            raise InvalidArgumentException("You need to use the Platform enum to switch platforms")
        self.__endpointBaseURL__ = str(Endpoint.PALADINS_XBOX) if platform == Platform.XBOX or platform == Platform.NINTENDO_SWITCH else str(Endpoint.PALADINS_PS4) if platform == Platform.PS4 else str(Endpoint.PALADINS_PC)

    def getChampions(self, language = LanguageCode.English):
        """
        /getchampions[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{languageCode}
        Returns all Champions and their various attributes. [PaladinsAPI only]

        Parameters
        ----------
        language: [optional] : class:`LanguageCode`:  
        """
        return self.makeRequest("getchampions", language)

    def getChampionRanks(self, playerID):
        """
        /getchampionranks[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
        Returns the Rank and Worshippers value for each Champion a player has played. [PaladinsAPI only]
        
        Parameters
        ----------
        playerID : int or str
        """
        return self.makeRequest("getchampionranks", [playerID])

    def getChampionRecommendedItems(self, champID, language = LanguageCode.English):
        """
        /getchampionrecommendeditems[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godid}/{languageCode}
        Returns the Recommended Items for a particular Champion. [PaladinsAPI only; Osbsolete - no data returned]
        
        Parameters
        ----------
        champID : int 
        language : class:`LanguageCode`
        """
        #return self.makeRequest("getgodrecommendeditems", [champID, language])
        raise DeprecatedException("Osbsolete - no data returned")

    def getChampionSkins(self, champID, language = LanguageCode.English):
        """
        /getchampionskins[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
        Returns all available skins for a particular Champion. [PaladinsAPI only]
        
        Parameters
        ----------
        champID : int
        language :class:`LanguageCode`
        """
        return self.makeRequest("getgodskins", [godID, language])

    def getPlayerIdInfoForXboxAndSwitch(self, playerName):
        """
        /getplayeridinfoforxboxandswitch[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{playerName}
        Meaningful only for the Paladins Xbox API. Paladins Xbox data and Paladins Switch data is stored in the same DB.
        Therefore a Paladins Gamer Tag value could be the same as a Paladins Switch Gamer Tag value.
        Additionally, there could be multiple identical Paladins Switch Gamer Tag values.
        The purpose of this method is to return all Player ID data associated with the playerName (gamer tag) parameter.
        The expectation is that the unique player_id returned could then be used in subsequent method calls. [PaladinsAPI only]
        """
        return self.makeRequest("getplayeridinfoforxboxandswitch", [playerName])

    def getPlayerLoadouts(self, playerID, language = LanguageCode.English):
        """
        /getplayerloadouts[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/playerId}/{languageCode}
        Returns deck loadouts per Champion. [PaladinsAPI only]
        
        Parameters
        ----------
        playerID : int or str
        language: :class:`LanguageCode`
        """
        getPlayerLoadoutsResponse = self.makeRequest("getplayerloadouts", [playerID, language])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.JSON).lower():
            playerLoadouts = []
            for i in range(0, len(getPlayerLoadoutsResponse)):
                obj = PlayerLoadouts(**getPlayerLoadoutsResponse[i])
                playerLoadouts.append(obj)
            return playerLoadouts if playerLoadouts else None
        else:
            return getPlayerLoadoutsResponse
        
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
    def __init__(self, devId, authKey, platform = Platform.PC, responseFormat = ResponseFormat.JSON):
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
        if platform == Platform.PC:
            endpoint = Endpoint.REALM_ROYALE_XBOX if(platform == Platform.XBOX) else Endpoint.REALM_ROYALE_PS4 if(platform == Platform.PS4) else Endpoint.REALM_ROYALE_PC
            super().__init__(int(devId), str(authKey), endpoint, responseFormat)
        else:
            raise NotSupported("Not released yet!")

    # /getplayermatchhistory[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
    def getPlayerMatchHistory (self, playerID):
        return self.makeRequest("getplayermatchhistory", [playerID])
    
    # /getplayermatchhistoryafterdatetime[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}/{startDatetime}
    def getPlayerMatchHistoryAfterDatetime (self, playerID):
        return self.makeRequest("getplayermatchhistoryafterdatetime", [playerID])

    # /getplayerstats[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
    def getPlayerStats (self, playerID):
        return self.makeRequest("getplayerstats", [playerID])

    # /searchplayers[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
    def searchPlayers(self, playerID):
        if not playerID or len(playerID) <= 3:
            raise InvalidArgumentException("Invalid player!")
        else:
            searchPlayerResponse = self.makeRequest("searchplayers", [playerID])
            if str(self.__responseFormat__).lower() == str(ResponseFormat.JSON).lower():
                players = []
                for player in searchPlayerResponse:
                    obj = Player(**player)
                    players.append(obj)
                    return players if players else None
            else:
                return searchPlayerResponse

class SmiteAPI(HiRezAPI):
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
    def __init__(self, devId, authKey, platform = Platform.PC, responseFormat = ResponseFormat.JSON):
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
        if platform == Platform.NINTENDO_SWITCH or platform == Platform.MOBILE:
            raise NotSupported("Not released yet!")
        endpoint = Endpoint.SMITE_XBOX if(platform == Platform.XBOX) else Endpoint.SMITE_PS4 if(platform == Platform.PS4) else Endpoint.SMITE_PC
        super().__init__(int(devId), str(authKey), endpoint, responseFormat)

    def switchPlatform(self, platform):
        if not isinstance(endpoint, Platform):
            raise InvalidArgumentException("You need to use the Platform enum to switch platforms")
        self.__endpointBaseURL__ = str(Endpoint.SMITE_XBOX) if platform == Platform.XBOX else str(Endpoint.SMITE_PS4) if platform == Platform.PS4 else str(Endpoint.SMITE_PC)

    def getDemoDetails(self, matchID):
        """
        /getdemodetails[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{match_id}
        Returns information regarding a particular match.  Rarely used in lieu of getmatchdetails().
        
        Parameters
        ----------
        matchID : int 
        
        """
        return self.makeRequest("getdemodetails", [matchID])

    def getGods(self, language = LanguageCode.English):
        """
        /getgods[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{languageCode}
        Returns all Gods and their various attributes.
        
        Parameters
        ----------
        language: [optional] : class: `LanguageCode` : 
        
        Returns
        -------
        Object of :class:`God` or :class:`Champion`
            Returns the infos about the API.

        """
        getGodsResponse = self.makeRequest("getgods", language)
        if str(self.__responseFormat__).lower() == str(ResponseFormat.JSON).lower():
            gods = []
            for i in getGodsResponse:
                obj = God(**i) if isinstance(self, SmiteAPI) != -1 else Champion(**i)
                gods.append(obj)
            return gods if gods else None
        else:
            return getGodsResponse

    def getGodLeaderboard(self, godId, queueId):
        """
        /getgodleaderboard[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godId}/{queue}
        Returns the current season’s leaderboard for a god/queue combination. [SmiteAPI only; queues 440, 450, 451 only]
        
        Parameters
        ----------
        godId: int 
        queueId: int
        """
        return self.makeRequest("getgodleaderboard", [godId, queueId])
    
    def getGodRanks(self, playerID):
        """
        /getgodranks[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
        Returns the Rank and Worshippers value for each God a player has played.
        
        Parameters
        ----------
        playerID : int or str
        
        Returns
        -------
        Object of :class:`GodRank`

        """
        if not playerID or len(playerID) <= 3:
            raise InvalidArgumentException("Invalid player!")
        getGodRanksResponse = self.makeRequest("getgodranks", [playerID])
        if str(self.__responseFormat__).lower() == str(ResponseFormat.JSON).lower():
            godRanks = []
            for i in getGodRanksResponse:
                obj = GodRank(**i)
                godRanks.append(obj)
            return godRanks if godRanks else None
        else:
            return getGodRanksResponse

    def getGodRecommendedItems(self, godID: int, language = LanguageCode.English):
        """
        /getgodrecommendeditems[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godid}/{languageCode}
        Returns the Recommended Items for a particular God. [SmiteAPI only]
        
        Parameters
        ----------
        godID : int
        language : [optional] : class: `LanguageCode` : 
        """
        return self.makeRequest("getgodrecommendeditems", [godID, language])
    
    def getGodSkins(self, godID, language = LanguageCode.English):
        """
        /getgodskins[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
        Returns all available skins for a particular God.
        
        Parameters
        ----------
        godID: int : 
        language: :class:`LanguageCode`
        """
        return self.makeRequest("getgodskins", [godID, language])
    
    def getMotd(self):
        """
        /getmotd[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
        Returns information about the 20 most recent Match-of-the-Days.
        """
        return self.makeRequest("getmotd")

    def getTeamDetails(self, clanID):
        """
        /getteamdetails[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{clanid}
        Lists the number of players and other high level details for a particular clan.
        
        Parameters
        ----------
        clanID: int
        """
        return self.makeRequest("getteamdetails", [clanID])
    
    def getTeamMatchHistory(self, clanID):
        """
        *DEPRECATED*

        /getteammatchhistory[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{clanid}
        Gets recent matches and high level match statistics for a particular clan/team.
        """
        raise DeprecatedException("*DEPRECATED* - As of 2.14 Patch, /getteammatchhistory is no longer supported and will return a NULL dataset.")
        #return self.makeRequest("getteammatchhistory", [clanID])

    def getTeamPlayers(self, clanID):
        """
        /getteamplayers[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{clanid}
        Lists the players for a particular clan.
        
        Parameters
        ----------
        clanID: int
        """
        return self.makeRequest("getteamplayers", [clanID])

    def getTopMatches(self):
        """
        /gettopmatches[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
        Lists the 50 most watched / most recent recorded matches.
        """
        return self.makeRequest("gettopmatches")

    def searchTeams(self, teamID):
        """
        /searchteams[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{searchTeam}
        Returns high level information for Clan names containing the “searchTeam” string. [SmiteAPI only]
        
        Parameters
        ----------
        teamID: int
        """
        return self.makeRequest("searchteams", [teamID])

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
    def __init__(self, devId, authKey, responseFormat = ResponseFormat.JSON):
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
        super().__init__(int(devId), str(authKey), Endpoint.HAND_OF_THE_GODS_PC, responseFormat)

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
    def __init__(self, devId, authKey, responseFormat = ResponseFormat.JSON):
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
        super().__init__(int(devId), str(authKey), Endpoint.PALADINS_STRIKE_MOBILE, responseFormat)

