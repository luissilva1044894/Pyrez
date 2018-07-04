from datetime import timedelta, datetime
from hashlib import md5 as getMD5Hash
import pyrez
from pyrez.enumerations import Champions, Status, Tier, Classes, ItemType, RealmRoyaleQueue, SmiteQueue, PaladinsQueue
from pyrez.enumerations import Endpoint, Platform, ResponseFormat, LanguageCode
from pyrez.exceptions import CustomException, DailyLimitException, InvalidArgumentException, KeyOrAuthEmptyException, NotFoundException, NotSupported, SessionLimitException, WrongCredentials
from pyrez.http import HttpRequest as HttpRequest
from pyrez.models import APIResponse, HiRezServerStatus, Champion, ChampionSkin, God, DataUsed, PlayerPaladins, PlayerStatus, PlayerSmite, Friend, GodRank, Session, PatchInfo, PaladinsItem, SmiteItem, PlayerLoadouts, MatchHistory, PlayerRealmRoyale, Leaderboard
from sys import version_info as pythonVersion
class BaseAPI:
    """Class for all of the outgoing requests from the library. An instance of
    this is created by the Client class. Do not initialise this yourself.

    Parameters
    ----------
        devId : str or int
            Develop ID used for authentication.
        authKey : str
            Authentication Key used for authentication.
        endpoint: str
        responseFormat: [optional] : str
        language: [optional] : int

    """
    def __init__ (self, devId, authKey, endpoint, responseFormat = ResponseFormat.JSON):
        if not devId or not authKey:
            raise KeyOrAuthEmptyException ("DevKey or AuthKey not specified!")
        elif len (str (devId)) < 4 or not str (devId).isnumeric ():
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
    def __encode__ (self, string, encodeType = "utf-8"):
        return str (string).encode (encodeType)
    def __decode__ (self, string, encodeType = "utf-8"):
        return str (string).encode (encodeType)

class HiRezAPI (BaseAPI):
    __header__ = { "user-agent": "{0} [Python/{1.major}.{1.minor}]".format (pyrez.__title__, pythonVersion) }

    def __init__ (self, devId, authKey, endpoint, responseFormat = ResponseFormat.JSON):
        super ().__init__ (devId, authKey, endpoint, responseFormat)
        self.__lastSession__ = None
        self.currentSession = None
        # print ("{0} [Python/{1.major}.{1.minor}]".format (pyrez.__title__, pythonVersion))

    def __createTimeStamp__ (self, format: str = "%Y%m%d%H%M%S"):
        return self.__currentTime__ ().strftime (format)

    def __currentTime__ (self):
        return datetime.utcnow ()

    def __createSignature__ (self, method: str):
        return getMD5Hash (self.__encode__ (str (self.__devId__) + str (method) + str (self.__authKey__) + str (self.__createTimeStamp__ ()))).hexdigest ()

    def __sessionExpired__ (self):
        return self.__lastSession__ is None or self.__currentTime__ () - self.__lastSession__ >= timedelta (minutes = 15)

    def __buildUrlRequest__ (self, apiMethod: str, params = ()):#requireSession = True, params = ()):
        if len (str (apiMethod)) == 0:
            raise InvalidArgumentException ("No API method specified!")
        else:
            urlRequest = "{0}/{1}{2}".format (self.__endpointBaseURL__, apiMethod.lower (), self.__responseFormat__)
            if apiMethod.lower () != "ping":
                urlRequest += "/{0}/{1}".format (self.__devId__, self.__createSignature__ (apiMethod.lower ()))
                if self.currentSession != None and apiMethod.lower () != "createsession":#requireSession:
                    urlRequest += "/{0}".format (self.currentSession)
                urlRequest += "/{0}".format (self.__createTimeStamp__ ())
        
                if params:
                    for param in params:
                        if param != None:
                            urlRequest += "/" + str (param)
            return urlRequest

    def makeRequest (self, apiMethod: str, params = ()):
        if len (str (apiMethod)) == 0:
            raise InvalidArgumentException ("No API method specified!")
        elif (apiMethod.lower () != "createsession" and self.__sessionExpired__ ()):
            self.__createSession__ ()
        result = HttpRequest (self.__header__).get (apiMethod if apiMethod.find ("http") != -1 else self.__buildUrlRequest__ (apiMethod, params))
        if result.status_code == 200:
            if str (self.__responseFormat__).lower () == "xml":
                return result.text
            else:
                makeRequestJSON = result.json ()
                if len (makeRequestJSON) == 0:
                    raise NotFoundException ("Successful request, but 0 results")
                else:
                    if apiMethod.lower () == "testsession" or apiMethod.lower () == "ping":
                        return makeRequestJSON
                    else:
                        foundProblem = False
                        hasError = APIResponse (** makeRequestJSON) if str (makeRequestJSON).startswith ("{") else APIResponse (** makeRequestJSON [0])
                        if hasError != None and hasError.retMsg != None:
                            if hasError.retMsg.lower () != "approved":
                                foundProblem = not foundProblem

                                if hasError.retMsg.find ("dailylimit") != -1:
                                    raise DailyLimitException ("Daily limit reached: " + hasError.retMsg)
                                elif hasError.retMsg.find ("Maximum number of active sessions reached") != -1:
                                    raise SessionLimitException ("Concurrent sessions limit reached: " + hasError.retMsg)
                                elif hasError.retMsg.find ("Invalid session id") != -1:
                                    self.__createSession__ ()
                                    return self.makeRequest (apiMethod, params)
                                elif hasError.retMsg.find ("Exception while validating developer access") != -1:
                                    raise WrongCredentials ("Wrong credentials: " + hasError.retMsg)
                                elif hasError.retMsg.find ("404") != -1:
                                    raise NotFoundException ("Not found: " + hasError.retMsg)
                        if not foundProblem:
                            return makeRequestJSON
                        else:
                            raise NotFoundException ("FoundProblem: " + hasError.json)
        elif result.status_code == 404:
            raise NotFoundException ("Wrong URL: " + result.text)

    #/getgodleaderboard[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godId}/{queue}

    # /createsession[ResponseFormat]/{developerId}/{signature}/{timestamp}
    def __createSession__ (self):
        try:
            createSessionResponse = self.makeRequest ("createsession")
            if createSessionResponse:
                self.currentSession = Session (** createSessionResponse).sessionID
                self.__lastSession__ = self.__currentTime__( )
        except WrongCredentials as x:
            raise x

    # /ping[ResponseFormat]
    def ping (self):
        return self.makeRequest ("ping")

    # /testsession[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
    def testSession (self, sessionId = None):
        session = self.currentSession if sessionId is None else sessionId
        uri = "{0}/testsession{1}/{2}/{3}/{4}/{5}".format (self.__endpointBaseURL__, self.__responseFormat__, self.__devId__, self.__createSignature__ ("testsession"), session, self.__createTimeStamp__ ())
        testSessionResponse = self.makeRequest (uri)
        return testSessionResponse
    
    # /getdataused[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
    def getDataUsed (self):
        if str (self.__responseFormat__).lower () == "json":
            return DataUsed (** self.makeRequest ("getdataused") [0])
        else:
            return self.makeRequest ("getdataused")
    
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
            getFriendsResponse = self.makeRequest ("getfriends", [playerID])
            if str (self.__responseFormat__).lower () == "json":
                friends = []
                for friend in getFriendsResponse:
                    friends.append (Friend (** friend))
                return friends if friends else None
            else:
                return getFriendsResponse
    
    # /getgods[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{languageCode}
    # /getchampions[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{languageCode}
    def getGods (self, language = LanguageCode.ENGLISH):
        getGodsResponse = self.makeRequest ("getgods", language)
        if str (self.__responseFormat__).lower () == "json":
            if not getGodsResponse:
                return None
            else:
                gods = []
                for i in getGodsResponse:
                    if i ["id"] == "0":  # privacy settings active, skip
                        continue
                    obj = God (** i) if isinstance (self, SmiteAPI) != -1 else Champion (** i)
                    gods.append (obj)
                return gods if gods else None
        else:
            return getGodsResponse
    # /getgodranks[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
    # /getchampionranks[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
    def getGodRanks (self, playerID):
        if not playerID or len (playerID) <= 3:
            raise InvalidArgumentException ("Invalid player!")
        getGodRanksResponse = self.makeRequest ("getgodranks", [playerID])
        if not getGodRanksResponse:
            return None
        else:
            godRanks = []
            for i in getGodRanksResponse:
                obj = GodRank (** i)
                godRanks.append (obj)
            return godRanks if godRanks else None
    
    # /getgodrecommendeditems[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godid}/{languageCode}
    # /getchampionecommendeditems[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godid}/{languageCode}
    def getGodRecommendedItems (self, godID: int):
        return self.makeRequest ("getgodrecommendeditems", [godID])
    
    # /getgodskins[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
    # /getchampionskins[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
    def getGodSkins (self, godID: int):
        return self.makeRequest ("getgodskins", [godID])
    
    # /gethirezserverstatus[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
    def getHiRezServerStatus (self):
        return HiRezServerStatus (** self.makeRequest ("gethirezserverstatus") [0])
    
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
    # /getmatchdetailsbatch[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{match_id,match_id,match_id,...match_id}
    def getMatchDetails (self, matchID: int):
        return self.makeRequest ("getmatchdetails", [matchID])
    
    # /getmatchhistory[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
    def getMatchHistory (self, playerID):
        if not playerID or len (playerID) <= 3:
            raise InvalidArgumentException ("Invalid player!")
        getMatchHistoryResponse = self.makeRequest ("getmatchhistory", [playerID])
        if not getMatchHistoryResponse:
            return None
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
    
    # /getpatchinfo[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}
    def getPatchInfo (self):
        getPatchInfoResponse = self.makeRequest ("getpatchinfo")
        return PatchInfo (** getPatchInfoResponse) if getPatchInfoResponse else None
    
    # /getplayer[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
    def getPlayer (self, playerID):
        if not playerID or len (playerID) <= 3:
            raise InvalidArgumentException ("Invalid player!")
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
    # /getplayerloadouts[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/playerId}/{languageCode}
    def getPlayerLoadouts (self, playerID, language = LanguageCode.ENGLISH):
        if isinstance (self, PaladinsAPI):
            getPlayerLoadoutsResponse = self.makeRequest ("getplayerloadouts", [playerID, language])
            if not getPlayerLoadoutsResponse:
                return None
            else:
                playerLoadouts = []
                for i in range (0, len (getPlayerLoadoutsResponse)):
                    obj = PlayerLoadouts (** getPlayerLoadoutsResponse [i])
                    playerLoadouts.append (obj)
                return playerLoadouts if playerLoadouts else None
        else:
            raise NotSupported ("PALADINS ONLY")
    
    # /getplayerstatus[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{player}
    def getPlayerStatus (self, playerID):
        if not playerID or len (playerID) <= 3:
            raise InvalidArgumentException ("Invalid player!")
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
    def getTeamMatchHistory (self, clanID):
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

    def setPlatform (self, platform = Platform.PC):
        self.__init__ (self.__devId__, self.__authKey__, platform, self.__responseFormat__)
    def setEndpoint (self, endpoint):
        if endpoint != self.__endpointBaseURL__ and len (str (endpoint)) > 0:
            super ().__init__ (self.__devId__, self.__authKey__, endpoint, self.__responseFormat__)
    def setSession (self, sessionId: str):
        if sessionId and str (sessionId).isalnum ():
            testSessionResponse = self.testSession (sessionId)
            if testSessionResponse.lower ().find ("successful test") != -1:
                self.currentSession = str (sessionId)
class PaladinsAPI (HiRezAPI):
    def __init__ (self, devId: int, authKey: str, platform = Platform.PC, responseFormat = ResponseFormat.JSON):
        endpoint = Endpoint.PALADINS_XBOX if platform == Platform.XBOX or platform == Platform.NINTENDO_SWITCH else Endpoint.PALADINS_PS4 if platform == Platform.PS4 else Endpoint.PALADINS_PC
        super ().__init__ (devId, authKey, endpoint, responseFormat)
class SmiteAPI (HiRezAPI):
    def __init__ (self, devId: int, authKey: str, platform = Platform.PC, responseFormat = ResponseFormat.JSON):
        if platform == Platform.NINTENDO_SWITCH:
            raise NotSupported ("Not implemented!") 
        else:
            endpoint = Endpoint.SMITE_XBOX if (platform == Platform.XBOX) else Endpoint.SMITE_PS4 if (platform == Platform.PS4) else Endpoint.SMITE_PC
            super ().__init__ (devId, authKey, endpoint, responseFormat)
class RealmRoyaleAPI (HiRezAPI):
    def __init__ (self, devId: int, authKey: str, platform = Platform.PC, responseFormat = ResponseFormat.JSON):
        if platform == Platform.PC:
            # endpoint = Endpoint.REALM_ROYALE_XBOX if (platform == Platform.XBOX) else Endpoint.REALM_ROYALE_PS4 if (platform == Platform.PS4) else Endpoint.REALM_ROYALE_PC
            endpoint = Endpoint.REALM_ROYALE_PC
            super ().__init__ (devId, authKey, endpoint, responseFormat)
        else:
            raise NotSupported ("Not implemented!")
