from datetime import timedelta, datetime
from hashlib import md5 as getMD5Hash
from sys import version_info as pythonVersion

import pyrez
from pyrez.enumerations import *
from pyrez.exceptions import *
from pyrez.http import HttpRequest as HttpRequest
from pyrez.models import *
class BaseAPI:
    def __init__ (self, devId: int, authKey: str, endpoint: str, responseFormat = ResponseFormat.JSON):
        if not devId or not authKey:
            raise KeyOrAuthEmptyException ("DevKey or AuthKey not specified!")
        elif len (str (devId)) < 4 or len (str (devId)) > 5 or not str (devId).isnumeric ():
            raise InvalidArgumentException ("You need to pass a valid DevId!")
        elif len (str (authKey)) != 32 or not str (authKey).isalnum ():
            raise InvalidArgumentException ("You need to pass a valid AuthKey!")
        elif len (str (endpoint)) == 0 :
            raise InvalidArgumentException ("Endpoint can't be empty!")
        else:
            self.__devId__ = int (devId)
            self.__authKey__ = str (authKey)
            self.__endpointBaseURL__ = str (endpoint)
            self.__responseFormat__ = responseFormat if (responseFormat == ResponseFormat.JSON or responseFormat == ResponseFormat.XML) else ResponseFormat.JSON
    def __encode__ (self, string, encodeType: str = "utf-8"):
        return str (string).encode (encodeType)
    def __decode__ (self, string, encodeType: str = "utf-8"):
        return str (string).encode (encodeType)
    def __httpRequest__ (self, url: str, header = None):
        httpResponse = HttpRequest (header).get (url)
        if httpResponse.status_code == 200:
            try:
                return httpResponse.json ()
            except:
                return httpResponse.text
        else:
            raise NotFoundException ("Wrong URL: " + httpResponse.text)
class HiRezAPI (BaseAPI):
    __header__ = { "user-agent": "{0} [Python/{1.major}.{1.minor}]".format (pyrez.__title__, pythonVersion) }

    def __init__ (self, devId: int, authKey: str, endpoint: str, responseFormat = ResponseFormat.JSON):
        super ().__init__ (devId, authKey, endpoint, responseFormat)
        self.currentSession = None

    def __createTimeStamp__ (self, format: str = "%Y%m%d%H%M%S"):
        return self.__currentTime__ ().strftime (format)

    def __currentTime__ (self):
        return datetime.utcnow ()

    def __createSignature__ (self, method: str, timestamp = None):
        return getMD5Hash (self.__encode__ (str (self.__devId__) + str (method) + str (self.__authKey__) + str (timestamp if timestamp else self.__createTimeStamp__ ()))).hexdigest ()

    def __sessionExpired__ (self):
        #return self.currentSession is None or self.__currentTime__ () - self.currentSession.timeStamp >= timedelta (minutes = 15)
        return self.currentSession is None #or not str (self.currentSession.sessionID).isalnum ()
    def __buildUrlRequest__ (self, apiMethod: str, requireSession = True, params = ()): # [queue, date, hour]
        if len (str (apiMethod)) == 0:
            raise InvalidArgumentException ("No API method specified!")
        else:
            urlRequest = "{0}/{1}{2}".format (self.__endpointBaseURL__, apiMethod.lower (), self.__responseFormat__)
            if apiMethod.lower () != "ping":
                urlRequest += "/{0}/{1}".format (self.__devId__, self.__createSignature__ (apiMethod.lower ()))
                if requireSession:
                    if self.currentSession != None:
                        urlRequest += "/{0}".format (self.currentSession.sessionId)
                    else:
                        self.__createSession__ ()
                        return self.__buildUrlRequest__ (self, apiMethod, requireSession, params)
                urlRequest += "/{0}".format (self.__createTimeStamp__ ())
        
                if params:
                    for param in params:
                        if param != None:
                            urlRequest += "/" + str (param)
            return urlRequest

    def makeRequest (self, apiMethod: str, requireSession = True, params = ()):
        if len (str (apiMethod)) == 0:
            raise InvalidArgumentException ("No API method specified!")
        elif (apiMethod.lower () != "createsession" and self.__sessionExpired__ ()):
            self.__createSession__ ()
        result = self.__httpRequest__ (apiMethod if apiMethod.startswith ("http") else self.__buildUrlRequest__ (apiMethod, requireSession, params), self.__header__)
        if result:
            if str (self.__responseFormat__).lower () == "xml":
                return result
            else:
                if str (result).lower ().find ("ret_msg") == -1:
                    return result
                else:
                    foundProblem = False
                    hasError = APIResponse (** result) if str (result).startswith ("{") else APIResponse (** result [0])
                    if hasError != None and hasError.retMsg != None and hasError.retMsg.lower () != "approved":
                        foundProblem = not foundProblem
                        if hasError.retMsg.find ("dailylimit") != -1:
                            raise DailyLimitException ("Daily limit reached: " + hasError.retMsg)
                        elif hasError.retMsg.find ("Maximum number of active sessions reached") != -1:
                            raise SessionLimitException ("Concurrent sessions limit reached: " + hasError.retMsg)
                        elif hasError.retMsg.find ("Invalid session id") != -1:
                            self.__createSession__ ()
                            return self.makeRequest (apiMethod, requireSession, params)
                        elif hasError.retMsg.find ("Exception while validating developer access") != -1:
                            raise WrongCredentials ("Wrong credentials: " + hasError.retMsg)
                        elif hasError.retMsg.find ("404") != -1:
                            raise NotFoundException ("Not found: " + hasError.retMsg)
                    if not foundProblem:
                        return result

    # /createsession[ResponseFormat]/{developerId}/{signature}/{timestamp}        
    def __createSession__ (self):
        try:
            tempResponseFormat = self.__responseFormat__
            self.__responseFormat__ = "json"
            responseJSON = self.makeRequest ("createsession", False)
            if responseJSON:
                self.currentSession = Session (** responseJSON)
                # print (self.currentSession)
            self.__responseFormat__ = tempResponseFormat
        except WrongCredentials as x:
            raise x
    
    # /ping[ResponseFormat]
    def ping (self):
        tempResponseFormat = self.__responseFormat__
        self.__responseFormat__ = "json"
        responseJSON = self.makeRequest ("ping", False)
        self.__responseFormat__ = tempResponseFormat
        return Ping (responseJSON) if responseJSON else None
    
    #Se eu usar testSession primeiro, olhar se foi sucesso e setar o sessionId?
    # /testsession[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
    def testSession (self, sessionId: str = None):
        tempResponseFormat = self.__responseFormat__
        self.__responseFormat__ = "json"
        session = self.currentSession.sessionId if sessionId is None or not str (sessionId).isalnum () else sessionId
        uri = "{0}/testsession{1}/{2}/{3}/{4}/{5}".format (self.__endpointBaseURL__, self.__responseFormat__, self.__devId__, self.__createSignature__ ("testsession"), session, self.__createTimeStamp__ ())
        responseJSON = self.makeRequest (uri)
        self.__responseFormat__ = tempResponseFormat
        return TestSession (responseJSON) if responseJSON else None

    # /getdataused[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
    def getDataUsed (self):
        tempResponseFormat = self.__responseFormat__
        self.__responseFormat__ = "json"
        responseJSON = self.makeRequest ("getdataused")
        self.__responseFormat__ = tempResponseFormat
        return DataUsed (** responseJSON) if str (responseJSON).startswith ("{") else DataUsed (** responseJSON [0]) if responseJSON else None
    
    # /gethirezserverstatus[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
    def getHiRezServerStatus (self):
        tempResponseFormat = self.__responseFormat__
        self.__responseFormat__ = "json"
        responseJSON = self.makeRequest ("gethirezserverstatus")
        self.__responseFormat__ = tempResponseFormat
        return HiRezServerStatus (** responseJSON) if str (responseJSON).startswith ("{") else HiRezServerStatus (** responseJSON [0]) if responseJSON else None
    
    # /getpatchinfo[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
    def getPatchInfo (self):
        tempResponseFormat = self.__responseFormat__
        self.__responseFormat__ = "json"
        responseJSON = self.makeRequest ("getpatchinfo")
        self.__responseFormat__ = tempResponseFormat
        return PatchInfo (** responseJSON) if responseJSON else None

    # /getdemodetails[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{match_id}
    def getDemoDetails (self, matchID: int):
        return self.makeRequest ("getdemodetails", [matchID])

    # /getesportsproleaguedetails[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
    def getEsportsProLeagueDetails (self):
        return self.makeRequest ("getesportsproleaguedetails")

    # /getfriends[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
    def getFriends (self, playerID):
        if not playerID or len (playerID) <= 3:
            raise InvalidArgumentException ("Invalid player!")
        else:
            if str (self.__responseFormat__).lower () == "xml":
                return self.makeRequest ("getfriends", [playerID])
            else:
                responseJSON = self.makeRequest ("getfriends", [playerID])
                friends = []
                for friend in responseJSON:
                    friends.append (Friend (** friend))
                return friends if friends else None
    
    #/getgodleaderboard[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godId}/{queue}
    def getGodLeaderboard (self, godId: int, queueId: int):
        return self.makeRequest ("getgodleaderboard", [godId, queueId])
    
    # /getgods[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{languageCode}
    def getGods (self, language = LanguageCode.ENGLISH):
        getGodsResponse = self.makeRequest ("getgods", language)
        if str (self.__responseFormat__).lower () == "xml":
            return getGodsResponse
        else:
            gods = []
            for i in getGodsResponse:
                obj = God (** i) if isinstance (self, SmiteAPI) != -1 else Champion (** i)
                gods.append (obj)
            return gods if gods else None
    # /getchampions[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{languageCode}
    def getChampions (self, language = LanguageCode.ENGLISH):
        return self.makeRequest ("getchampions", language)

    # /getgodranks[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
    def getGodRanks (self, playerID):
        if not playerID or len (playerID) <= 3:
            raise InvalidArgumentException ("Invalid player!")
        getGodRanksResponse = self.makeRequest ("getgodranks", [playerID])
        if str (self.__responseFormat__).lower () == "xml":
            return getGodRanksResponse
        else:
            godRanks = []
            for i in getGodRanksResponse:
                obj = GodRank (** i)
                godRanks.append (obj)
            return godRanks if godRanks else None

    # /getchampionranks[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
    def getChampionRanks (self, playerID):
        return self.makeRequest ("getchampionranks", [playerID])
    
    # /getgodrecommendeditems[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godid}/{languageCode}
    # /getchampionecommendeditems[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godid}/{languageCode}
    def getGodRecommendedItems (self, godID: int):
        return self.makeRequest ("getgodrecommendeditems", [godID])
    
    # /getgodskins[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
    # /getchampionskins[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
    def getGodSkins (self, godID: int):
        return self.makeRequest ("getgodskins", [godID])
    
    # /getitems[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{languagecode}
    def getItems (self, language = LanguageCode.ENGLISH):
        return self.makeRequest ("getitems", [language])
    
    # /getleagueleaderboard[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{queue}/{tier}/{season}
    def getLeagueLeaderboard (self, queueID: int, tier, season):
        return self.makeRequest ("getleagueleaderboard", [queueID, tier, season])
    
    # /getleagueseasons[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{queue}
    def getLeagueSeasons (self, queueID: int):
        return self.makeRequest ("getleagueseasons", [queueID])
    
    # /getmatchdetails[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{match_id}
    def getMatchDetails (self, matchID: int):
        return self.makeRequest ("getmatchdetails", [matchID])
    
    # /getmatchdetailsbatch[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{match_id,match_id,match_id,...match_id}
    def getMatchDetailsBatch (self, matchID = ()): #5-10 partidas
        return self.makeRequest ("getmatchdetailsbatch", [matchID])

    # /getmatchhistory[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
    def getMatchHistory (self, playerID):
        if not playerID or len (playerID) <= 3:
            raise InvalidArgumentException ("Invalid player!")
        getMatchHistoryResponse = self.makeRequest ("getmatchhistory", [playerID])
        if str (self.__responseFormat__).lower () == "xml":
            return getMatchHistoryResponse
        else:
            matchHistorys = []
            for i in range (0, len (getMatchHistoryResponse)):
                obj = MatchHistory (** getMatchHistoryResponse [i])
                matchHistorys.append (obj)
            return matchHistorys if matchHistorys else None
    
    # /getmatchidsbyqueue[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{queue}/{date}/{hour}
    def getMatchIdsByQueue (self, queueID: int, date, hour: str = -1):
        return self.makeRequest ("getmatchidsbyqueue", [queueID, date.strftime ("%Y%m%d") if isinstance (date, datetime) else date, hour])
    
    # /getmatchplayerdetails[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{match_id}
    def getMatchPlayerDetails (self, matchID: int):
        return self.makeRequest ("getmatchplayerdetails", [matchID])
    
    # /getmotd[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
    def getMotd (self):
        return self.makeRequest ("getmotd")

    #/getplayeridinfoforxboxandswitch[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{playerName}
    def getPlayerIdInfoForXboxAndSwitch (self, playerName):
        return self.makeRequest ("getplayeridinfoforxboxandswitch", [playerName])
    
    # /getplayer[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
    def getPlayer (self, playerID):
        if not playerID or len (playerID) <= 3:
            raise InvalidArgumentException ("Invalid player!")
        else:
            if str (self.__responseFormat__).lower () == "xml":
                return getMatchHistoryResponse
            else:
                if isinstance (self, RealmRoyaleAPI):
                    plat = "hirez" if not str (playerID).isdigit () or str (playerID).isdigit () and len (str (playerID)) <= 8 else "steam"
                    return PlayerRealmRoyale (** self.makeRequest ("getplayer", [playerID, plat]))
                else:
                    res = self.makeRequest ("getplayer", [playerID]) [0]
                    return PlayerSmite (** res) if isinstance (self, SmiteAPI) else PlayerPaladins (** res)
    
    # /getplayerachievements[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{playerId}
    def getPlayerAchievements (self, playerID):
        if (len (playerID) <= 3):
            raise InvalidArgumentException ("Invalid player!")
        return self.makeRequest ("getplayerachievements", [playerID])

    # /getplayerloadouts[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/playerId}/{languageCode}
    def getPlayerLoadouts (self, playerID, language = LanguageCode.ENGLISH):
        getPlayerLoadoutsResponse = self.makeRequest ("getplayerloadouts", [playerID, language])
        if str (self.__responseFormat__).lower () == "xml":
            return getPlayerLoadoutsResponse
        else:
            playerLoadouts = []
            for i in range (0, len (getPlayerLoadoutsResponse)):
                obj = PlayerLoadouts (** getPlayerLoadoutsResponse [i])
                playerLoadouts.append (obj)
            return playerLoadouts if playerLoadouts else None
    
    # /getplayerstatus[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
    def getPlayerStatus (self, playerID):
        if not playerID or len (playerID) <= 3:
            raise InvalidArgumentException ("Invalid player!")
        else:
            if str (self.__responseFormat__).lower () == "xml":
                return self.makeRequest ("getplayerstatus", [playerID])
            else:
                return PlayerStatus (** self.makeRequest ("getplayerstatus", [playerID]) [0])
    
    # /getqueuestats[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}/{queue}
    def getQueueStats (self, playerID, queueID):
        if not playerID or len (playerID) <= 3:
            raise NotFoundException ("Invalid player!")
        return self.makeRequest ("getqueuestats", [playerID, queueID])
    
    # /getteamdetails[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{clanid}
    def getTeamDetails (self, clanID):
        return self.makeRequest ("getteamdetails", [clanID])
    
    # /getteammatchhistory[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{clanid}
    def getTeamMatchHistory (self, clanID):#deprecated
        return self.makeRequest ("getteammatchhistory", [clanID])
    
    # /getteamplayers[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{clanid}
    def getTeamPlayers (self, clanID):
        return self.makeRequest ("getteamplayers", [clanID])
    
    # /gettopmatches[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
    def getTopMatches (self):
        return self.makeRequest ("gettopmatches")
    
    # /searchteams[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{searchTeam}
    def searchTeams (self, teamID):
        return self.makeRequest ("searchteams", [teamID])
class HandOfTheGodsAPI (HiRezAPI):
    def __init__ (self, devId: int, authKey: str, responseFormat = ResponseFormat.JSON):
        super ().__init__ (int (devId), str (authKey), Endpoint.HAND_OF_THE_GODS_PC, responseFormat)
        raise NotSupported ("Not released yet!")
class PaladinsAPI (HiRezAPI):
    def __init__ (self, devId: int, authKey: str, platform = Platform.PC, responseFormat = ResponseFormat.JSON):
        if platform == Platform.MOBILE:
            raise NotSupported ("Not released yet!")
        else:
            endpoint = Endpoint.PALADINS_XBOX if platform == Platform.XBOX or platform == Platform.NINTENDO_SWITCH else Endpoint.PALADINS_PS4 if platform == Platform.PS4 else Endpoint.PALADINS_PC
            super ().__init__ (int (devId), str (authKey), endpoint, responseFormat)
class PaladinsStrikeAPI (HiRezAPI):
    def __init__ (self, devId: int, authKey: str, responseFormat = ResponseFormat.JSON):
        super ().__init__ (int (devId), str (authKey), Endpoint.PALADINS_STRIKE_MOBILE, responseFormat)
        raise NotSupported ("Not released yet!")
class RealmRoyaleAPI (HiRezAPI):
    def __init__ (self, devId: int, authKey: str, platform = Platform.PC, responseFormat = ResponseFormat.JSON):
        if platform == Platform.PC:
            endpoint = Endpoint.REALM_ROYALE_XBOX if (platform == Platform.XBOX) else Endpoint.REALM_ROYALE_PS4 if (platform == Platform.PS4) else Endpoint.REALM_ROYALE_PC
            super ().__init__ (int (devId), str (authKey), endpoint, responseFormat)
        else:
            raise NotSupported ("Not released yet!")
class SmiteAPI (HiRezAPI):
    def __init__ (self, devId: int, authKey: str, platform = Platform.PC, responseFormat = ResponseFormat.JSON):
        if platform == Platform.NINTENDO_SWITCH or platform == Platform.MOBILE:
            raise NotSupported ("Not released yet!")
        else:
            endpoint = Endpoint.SMITE_XBOX if (platform == Platform.XBOX) else Endpoint.SMITE_PS4 if (platform == Platform.PS4) else Endpoint.SMITE_PC
            super ().__init__ (int (devId), str (authKey), endpoint, responseFormat)
