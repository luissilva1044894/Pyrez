from datetime import datetime
from hashlib import md5
from json.decoder import JSONDecodeError
import os
from sys import version_info
from enum import Enum

import requests

import pyrez
from pyrez.enumerations import *
from pyrez.exceptions import PyrezException, DailyLimit, Deprecated, IdOrAuthEmpty, InvalidArgument, LiveMatchException, NoResult, NotFound, NotSupported, PaladinsOnly, PlayerNotFound, RealmRoyaleOnly, RequestError, SessionLimit, SmiteOnly, UnexpectedException, WrongCredentials
from pyrez.events import Event
from pyrez.models import *
from pyrez.models import MatchId as MatchIdByQueue
from pyrez.models.HiRez import AccountInfo, Transaction, UserInfo
from pyrez.models.StatusPage import Incidents, ScheduledMaintenances, StatusPage as SttsPg
from pyrez.models.RealmRoyale import Leaderboard as RealmRoyaleLeaderboard, MatchHistory as RealmMatchHistory, Player as RealmRoyalePlayer, Talent as RealmRoyaleTalent
from pyrez.models.Paladins import Champion, ChampionAbility, ChampionCard, ChampionSkin, Item as PaladinsItem, Post as PaladinsWebsitePost, Loadout as PlayerLoadout, Player as PaladinsPlayer
from pyrez.models.Smite import Player as SmitePlayer, Item as SmiteItem, TopMatch as SmiteTopMatch, God, GodLeaderboard, GodRank, GodRecommendedItem, GodSkin
class API:
    """
    DON'T INITALISE THIS YOURSELF!
    Attributes:
        headers [dict]:
        cookies [dict]:
    Methods:
        __init__(devId, header=None)
        _encode(string, encodeType="utf-8")
        _httpRequest(url, headers=None)
    """
    def __init__(self, headers=None, cookies=None):
        """
        The constructor for API class.
        Keyword arguments/Parameters:
            headers:
        """
        self.headers = headers if headers else { "user-agent": "{0} [Python/{1.major}.{1.minor} requests/{2}]".format(pyrez.__title__, version_info, requests.__version__) }
        self.cookies = cookies
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
    def _httpRequest(self, url, method="GET", params=None, data=None, headers=None, cookies=None, json=None, files=None, auth=None, timeout=None, allowRedirects=False, proxies=None, hooks=None, stream=False, verify=None, cert=None):
        httpResponse = requests.request(method=method, url=url.replace(' ', '%20'), params=params, json=json, data=data, headers=headers if headers else self.headers, cookies=cookies if cookies else self.cookies, files=files, auth=auth, timeout=timeout, allow_redirects=allowRedirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert)
        self.cookies = httpResponse.cookies
        #if httpResponse.status_code >= 400:
        #    raise NotFoundException("{}".format(httpResponse.text))
        httpResponse.raise_for_status()#https://2.python-requests.org/en/master/api/#requests.Response.raise_for_status
        try:
            return httpResponse.json()
        except (JSONDecodeError, ValueError):
            return httpResponse.text
class StatusPage(API):
    def __init__(self):
        super().__init__()
    def getComponents(self):
        return self._httpRequest(self._getEndpoint("components.json"))
    def _getEndpoint(self, endpoint=None, api=True):
        return "{}{}{}".format(Endpoint.STATUS_PAGE, "/api/v2" if api else "", "/{}".format(endpoint) if endpoint else "")
    def getHistory(self, fmr=ResponseFormat.JSON):
        return self._httpRequest(self._getEndpoint("history.{}".format(fmr), False))
    def getIncidents(self, unresolvedOnly=False):
        _ = self._httpRequest(self._getEndpoint("incidents{}.json".format("/unresolved" if unresolvedOnly else "")))
        return Incidents(**_) if _ else None
    def getScheduledMaintenances(self, activeOnly=False, upcomingOnly=False):
        _ = self._httpRequest(self._getEndpoint("scheduled-maintenances{}.json".format("/active" if activeOnly else "/upcoming" if upcomingOnly else "")))
        return ScheduledMaintenances(**_) if _ else None
    def getStatus(self):
        _ = self._httpRequest(self._getEndpoint("status.json"))
        return SttsPg(**_) if _ else None
    def getSummary(self):
        return self._httpRequest(self._getEndpoint("summary.json"))
class HiRezAPI(API):
    """docstring for HiRezAPI"""
    PYREZ_HEADER = { "user-agent": "{0} [Python/{1.major}.{1.minor} requests/{2}]".format(pyrez.__title__, version_info, requests.__version__), "Origin": "https://my.hirezstudios.com" }
    def __init__(self, username, password, webToken=None):
        super().__init__(self.PYREZ_HEADER)#super(HiRezAPI, self).__init__()
        self.username = username
        self.password = password
        self.webToken = webToken
    def _getEndpoint(self, endpoint=None, act="/acct"):
        return "{}{}{}".format(Endpoint.HIREZ, act if act else "", "/{}".format(endpoint) if endpoint else "")
    def _login(self):
        _ = self.makeRequest("login", {"username": self.username, "password": self.password})#data=json.dumps{"username": username, "password": password})
        return AccountInfo(**_) if _ else None
    def __getwebToken(self):
        if not self.webToken:
            self.webToken = self._login().webToken
        return self.webToken
    def makeRequest(self, endpoint, params=None, methodType="POST", action="/acct"):
        return self._httpRequest(method=methodType, url=self._getEndpoint(endpoint=endpoint, act=action), json=params)
    def changeEmail(self, newEmail):
        return self.makeRequest("changeEmail", {"webToken": self.__getwebToken(), "newEmail": newEmail, "password": self.password})
    @staticmethod
    def create(username, password, email=None):
        _ = requests.request(method="POST", url=self._getEndpoint(endpoint="create").replace(' ', '%20'), json={"username": username, "password": password, "confirmPassword": password,"email": email, "over13":"true", "subscribe":"on"}, headers=HiRezAPI.PYREZ_HEADER)
        return HiRezAPI(username, password, _.json().get("webToken", None))
    def createSingleUseCode(self):
        return self.makeRequest("createSingleUseCode", {"webToken": self.__getwebToken()})
    def createVerification(self):
        return self.makeRequest("createVerification", {"webToken": self.__getwebToken()})
    def getRewards(self):
        return self.makeRequest("rewards", {"webToken": self.__getwebToken()})
    def getTransactions(self):
        _ = self.makeRequest("transactions", {"webToken": self.__getwebToken()})
        __ = [ Transaction(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def info(self):
        _ = self.makeRequest("info", {"webToken": self.__getwebToken()})
        return UserInfo(**_) if _ else None
    def setBackupEmail(self, backupEmail):
        return self.makeRequest("setBackupEmail", {"webToken": self.__getwebToken(), "email": backupEmail})
    def subscribe(self, subscribe=False):
        return self.makeRequest("subscribe", {"webToken": self.__getwebToken(), "subscribe": subscribe})
    def twoFactor(notifyByEmail=True, notifyBySms=False, validationPeriod=1):
        return self.makeRequest("twoFactorOptIn", {"webToken": self.__getwebToken(), "notifyBySms": notifyBySms, "notifyByEmail": notifyByEmail, "validationPeriod": validationPeriod})
    def verify(self, key):
        return self.makeRequest("verify", {"key": key})
class APIBase(API):
    """
    Class for handling connections and requests to Hi-Rez Studios' APIs. IS BETTER DON'T INITALISE THIS YOURSELF!
    """
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
        self._responseFormat = ResponseFormat(responseFormat) if isinstance(responseFormat, ResponseFormat) else ResponseFormat.JSON
        self.useConfigIni = useConfigIni
        self.onSessionCreated = Event()
        self.currentSessionId = sessionId if sessionId else self._getSession() #if sessionId and self.testSession(sessionId)
    @classmethod
    def _getSession(cls):
        import json
        try:
            with open("{0}/session.json".format(os.path.dirname(os.path.abspath(__file__))), 'r', encoding="utf-8") as sessionJson:
                return Session(**json.load(sessionJson)).sessionId
        except (FileNotFoundError, ValueError):
            return None
    def __setSession(self, session):
        self.currentSessionId = session.sessionId
        if self.useConfigIni and session:
            with open("{0}/session.json".format(os.path.dirname(os.path.abspath(__file__))), 'w', encoding="utf-8") as sessionJson:
                sessionJson.write(str(session.json).replace("'", "\""))
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
        return md5(self._encode("{}{}{}{}".format(self._devId, methodName.lower(), self._authKey, timestamp if timestamp else self._createTimeStamp()))).hexdigest()
    def _sessionExpired(self):
        return not self.currentSessionId or not str(self.currentSessionId).isalnum()
    def _buildUrlRequest(self, apiMethod=None, params=()):
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
            if self._responseFormat.equal(ResponseFormat.XML):
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
        /createsession[ResponseFormat]/{devId}/{signature}/{timestamp}
        A required step to Authenticate the devId/signature for further API use.
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, ResponseFormat.JSON
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
        tempResponseFormat, self._responseFormat = self._responseFormat, ResponseFormat.JSON
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
        tempResponseFormat, self._responseFormat = self._responseFormat, ResponseFormat.JSON
        _ = self.makeRequest("getdataused")
        self._responseFormat = tempResponseFormat
        return DataUsed(**_) if str(_).startswith('{') else DataUsed(**_[0]) if _ else None
    def getHiRezServerStatus(self):
        """
        /gethirezserverstatus[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Function returns UP/DOWN status for the primary game/platform environments. Data is cached once a minute.
        Returns:
            Object of pyrez.models.HiRezServerStatus
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, ResponseFormat.JSON
        _ = self.makeRequest("gethirezserverstatus")
        self._responseFormat = tempResponseFormat
        __ = [ HiRezServerStatus(**___) for ___ in (_ if _ else []) ]
        return (__ if len(__) > 1 else __[0]) if __ else None
    def getPatchInfo(self):
        """
        /getpatchinfo[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Function returns information about current deployed patch. Currently, this information only includes patch version.
        Returns:
            Object of pyrez.models.PatchInfo
        """
        tempResponseFormat, self._responseFormat = self._responseFormat, ResponseFormat.JSON
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
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
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
        """
        _ = self.makeRequest("getmatchdetailsbatch", [','.join(matchId)]) if isinstance(matchId, (type(()), type([]))) else self.makeRequest("getmatchplayerdetails" if isLive else "getmatchdetails", [matchId])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
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
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ MatchHistory(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getMatchIds(self, queueId, date, hour=-1):
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
        _ = self.makeRequest("getmatchidsbyqueue", [queueId, date.strftime("%Y%m%d/%H,%M") if isinstance(date, datetime) else (date, format(hour, ",.2f").replace('.', ',') if isinstance(hour, float) and hour != -1 else hour)])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ MatchIdByQueue(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getPlayerAchievements(self, playerId):
        """
        /getplayerachievements[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
            Returns select achievement totals (Double kills, Tower Kills, First Bloods, etc) for the specified playerId.
        Keyword arguments/Parameters:
            playerId [int]:
        """
        _ = self.makeRequest("getplayerachievements", [playerId])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
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
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
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
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
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
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ QueueStats(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def searchPlayers(self, playerName):
        """
        /searchplayers[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerName}
        """
        _ = self.makeRequest("searchplayers", [playerName])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ Player(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
class BaseSmitePaladinsAPI(APIBase):
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
        _ = self.makeRequest("getdemodetails", [matchId])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ DemoDetails(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getEsportsProLeague(self):
        """
        /getesportsproleaguedetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Returns the matchup information for each matchup for the current eSports Pro League season.
            An important return value is “match_status” which represents a match being scheduled (1), in-progress (2), or complete (3)
        """
        _ = self.makeRequest("getesportsproleaguedetails")
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ EsportProLeague(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getGods(self, languageCode=LanguageCode.English):
        """
        /getgods[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{languageCode}
            Returns all Gods and their various attributes.
        Keyword arguments/Parameters:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        Returns:
            List of pyrez.models.God or pyrez.models.Champion objects
        """
        _ = self.makeRequest("getgods", [languageCode])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ God(**___) if isinstance(self, SmiteAPI) else Champion(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getGodLeaderboard(self, godId, queueId):
        """
        /getgodleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{queue}
            Returns the current season’s leaderboard for a god/queue combination. [SmiteAPI only; queues 440, 450, 451 only]
        Keyword arguments/Parameters:
            godId [int]:
            queueId [int]:
        """
        _ = self.makeRequest("getgodleaderboard", [godId, queueId])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ GodLeaderboard(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getGodRanks(self, playerId):
        """
        /getgodranks[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
            Returns the Rank and Worshippers value for each God a player has played.
        Keyword arguments/Parameters:
            playerId [int]:
        Returns:
            List of pyrez.models.GodRank objects
        """
        _ = self.makeRequest("getgodranks", [playerId])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ GodRank(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getGodSkins(self, godId, languageCode=LanguageCode.English):
        """
        /getgodskins[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
            Returns all available skins for a particular God.
        Keyword arguments/Parameters:
            godId [int]:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        _ = self.makeRequest("getgodskins", [godId, languageCode])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ GodSkin(**___) if isinstance(self, SmiteAPI) != -1 else ChampionSkin(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getItems(self, languageCode=LanguageCode.English):
        """
        /getitems[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{languageCode}
            Returns all Items and their various attributes.
        Keyword arguments/Parameters:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        _ = self.makeRequest("getitems", [languageCode])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ SmiteItem(**___) if isinstance(self, SmiteAPI) != -1 else PaladinsItem(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getLeagueLeaderboard(self, queueId, tier, split):
        """
        /getleagueleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queue}/{tier}/{split}
            Returns the top players for a particular league (as indicated by the queue/tier/split parameters).
        Keyword arguments/Parameters:
            queueId [int]:
            tier [int]:
            split [int]:
        """
        _ = self.makeRequest("getleagueleaderboard", [queueId, tier, split])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ LeagueLeaderboard(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getLeagueSeasons(self, queueId):
        """
        /getleagueseasons[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queueId}
            Provides a list of seasons (including the single active season) for a match queue.
        Keyword arguments/Parameters:
            queueId [int]:
        """
        _ = self.makeRequest("getleagueseasons", [queueId])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ LeagueSeason(**___) for ___ in (_ if _ else []) ]
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
        if not _:
            raise PlayerNotFound("Player don't exist or it's hidden")
        if self._responseFormat.equal(ResponseFormat.XML):# or not _:
            return _
        return SmitePlayer(**_[0]) if isinstance(self, SmiteAPI) else PaladinsPlayer(**_[0])#TypeError: type object argument after ** must be a mapping, not NoneType
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
        _ = self.makeRequest("https://cms.paladins.com/wp-json/api/get-posts/{}?tag=update-notes".format(str(languageCode)))
        if not _:
            return None
        __ = self.getWebsitePost(languageCode=languageCode, slug=PaladinsWebsitePost(**_[0]).slug)
        return __[0] if __ else None
    def getWebsitePost(self, languageCode=LanguageCode.English, slug=None, query=None):
        _ = self.makeRequest("https://cms.paladins.com/wp-json/api/get-post/{}?slug={}&search={}".format(str(languageCode), slug, query))
        if not _:
            return None
        __ = [ PaladinsWebsitePost(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getChampions(self, languageCode=LanguageCode.English):
        """
        /getchampions[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{languageCode}
            Returns all Champions and their various attributes. [PaladinsAPI only]
        Keyword arguments/Parameters:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        _ = self.makeRequest("getchampions", [languageCode])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ Champion(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getChampionCards(self, godId, languageCode=LanguageCode.English):
        """
        /getchampioncards[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
            Returns all Champion cards. [PaladinsAPI only]
        Keyword arguments/Parameters:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        _ = self.makeRequest("getchampioncards", [godId, languageCode])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ ChampionCard(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getChampionLeaderboard(self, godId, queueId=QueuePaladins.Live_Competitive_Keyboard):
        """
        /getchampionleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{queueId}
            Returns the current season’s leaderboard for a champion/queue combination. [PaladinsAPI; only queue 428]
        Keyword arguments/Parameters:
            godId [int]:
            queueId [int]:
        """
        _ = self.makeRequest("getchampionleaderboard", [godId, queueId])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ GodLeaderboard(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getChampionRanks(self, playerId):
        """
        /getchampionranks[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
            Returns the Rank and Worshippers value for each Champion a player has played. [PaladinsAPI only]
        Keyword arguments/Parameters:
            playerId [int]:
        """
        _ = self.makeRequest("getchampionranks", [playerId])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ GodRank(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getChampionSkins(self, godId, languageCode=LanguageCode.English):
        """
        /getchampionskins[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}
            Returns all available skins for a particular Champion. [PaladinsAPI only]
        Keyword arguments/Parameters:
            godId [int]:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        _ = self.makeRequest("getchampionskins", [godId, languageCode])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ ChampionSkin(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getPlayerIdInfoForXboxAndSwitch(self, playerName):
        """
        /getplayeridinfoforxboxandswitch[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerName}
            Meaningful only for the Paladins Xbox API. Paladins Xbox data and Paladins Switch data is stored in the same DB.
            Therefore a Paladins Gamer Tag value could be the same as a Paladins Switch Gamer Tag value.
            Additionally, there could be multiple identical Paladins Switch Gamer Tag values.
            The purpose of this method is to return all Player ID data associated with the playerName (gamer tag) parameter.
            The expectation is that the unique player_id returned could then be used in subsequent method calls. [PaladinsAPI only]
        """
        _ = self.makeRequest("getplayeridinfoforxboxandswitch", [playerName])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ PlayerId(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getPlayerLoadouts(self, playerId, languageCode=LanguageCode.English):
        """
        /getplayerloadouts[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/playerId}/{languageCode}
            Returns deck loadouts per Champion. [PaladinsAPI only]
        Keyword arguments/Parameters:
            playerId [int]:
            languageCode [int] or [pyrez.enumerations.LanguageCode]: (default pyrez.enumerations.LanguageCode.English)
        """
        _ = self.makeRequest("getplayerloadouts", [playerId, languageCode])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ PlayerLoadout(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
class RealmRoyaleAPI(APIBase):
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
        _ = self.makeRequest("getleaderboard", [queueId, rankingCriteria])
        return _ if self._responseFormat.equal(ResponseFormat.XML) or not _ else RealmRoyaleLeaderboard(**_) 
    def getPlayer(self, player, platform=None):
        """
        /getplayer[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{player}/{platform}
            Returns league and other high level data for a particular player.
        Keyword arguments/Parameters:
            player [int] or [str]:
        """
        plat = platform if platform else "hirez" if not str(player).isdigit() or str(player).isdigit() and len(str(player)) <= 8 else "steam"
        _ = self.makeRequest("getplayer", [player, plat])
        #raise PlayerNotFound("Player don't exist or it's hidden")
        return _ if self._responseFormat.equal(ResponseFormat.XML) or not _ else RealmRoyalePlayer(**_)
    def getMatchHistory(self, playerId, startDatetime=None):
        """
        /getplayermatchhistory[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        """
        methodName = "getplayermatchhistory" if not startDatetime else "getplayermatchhistoryafterdatetime"
        params = [playerId] if not startDatetime else [startDatetime.strftime("yyyyMMddHHmmss") if isinstance(startDatetime, datetime) else startDatetime, playerId]
        _ = self.makeRequest(methodName, params)
        return _ if self._responseFormat.equal(ResponseFormat.XML) or not _ else RealmMatchHistory(**_)
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
        _ = self.makeRequest("gettalents", [languageCode])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ RealmRoyaleTalent(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
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
        _ = self.makeRequest("getgodrecommendeditems", [godId, languageCode])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ GodRecommendedItem(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getMotd(self):
        """
        /getmotd[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Returns information about the 20 most recent Match-of-the-Days.
        """
        _ = self.makeRequest("getmotd")
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ MOTD(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getTeamDetails(self, clanId):
        """
        /getteamdetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{clanId}
            Lists the number of players and other high level details for a particular clan.
        Keyword arguments/Parameters:
            clanId [int]:
        """
        _ = self.makeRequest("getteamdetails", [clanId])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ TeamDetail(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getTeamPlayers(self, clanId):
        """
        /getteamplayers[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{clanId}
            Lists the players for a particular clan.
        Keyword arguments/Parameters:
            clanId [int]:
        """
        _ = self.makeRequest("getteamplayers", [clanId])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ TeamPlayer(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getTopMatches(self):
        """
        /gettopmatches[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Lists the 50 most watched / most recent recorded matches.
        """
        _ = self.makeRequest("gettopmatches")
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ SmiteTopMatch(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def searchTeams(self, teamId):
        """
        /searchteams[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{searchTeam}
            Returns high level information for Clan names containing the “searchTeam” string. [SmiteAPI only]
        Keyword arguments/Parameters:
            teamId [int]:
        """
        _ = self.makeRequest("searchteams", [teamId])
        if self._responseFormat.equal(ResponseFormat.XML) or not _:
            return _
        __ = [ TeamSearch(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
