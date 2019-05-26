from datetime import datetime

from pyrez.enumerations import Format, Endpoint, Language
from pyrez.models.RealmRoyale import Leaderboard as RealmRoyaleLeaderboard, MatchHistory as RealmMatchHistory, Player as RealmRoyalePlayer, Talent as RealmRoyaleTalent

from .API import API
class RealmRoyaleAPI(API):
    """
    Represents a client that connects to RealmRoyale_ API.

    NOTE
    -------
        |PrivacyMode|
    Keyword arguments
    -------
    devId : |INT|
        |DevIdConstruct|
    authKey : |STR|
        |AuthKeyConstruct|
    responseFormat : Optional :class:`.Format`
        |FormatConstruct|
    sessionId : Optional |STR|
        Manually sets an active sessionId. Passing in ``None`` or an invalid sessionId will use the default instead of the passed in value.
    storeSession : Optional |BOOL|
        Allows Pyrez to read and store sessionId in a .json file. Defaults to ``False``.
    Raises
    -------
    pyrez.exceptions.IdOrAuthEmpty
        Raised when the ``Developer ID`` or ``Authentication Key`` is not specified.
    pyrez.exceptions.InvalidArgument
        Raised when an invalid ``Credentials`` is passed.
    Attributes
    -----------
    authKey
        |AuthKeyAtrib|
    devId
        |DevIdAtrib|
    onSessionCreated
        :class:`pyrez.events.Event` – A decorator that registers an event to listen to.
    responseFormat:
        |FormatAtrib|
    sessionId
        |STR| – The active sessionId.
    statusPage
        :class:`pyrez.api.StatusPageAPI` – An object that represents :class:`pyrez.api.StatusPageAPI` client.
    storeSession
        |BOOL| – Allows Pyrez to read and store sessionId in a .json file.
    """
    def __init__(self, devId, authKey, responseFormat=Format.JSON, sessionId=None, storeSession=True):
        super().__init__(devId, authKey, Endpoint.REALM_ROYALE, responseFormat, sessionId, storeSession)
    def getLeaderboard(self, queueId, rankingCriteria):
        """
        /getleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queueId}/{ranking_criteria}
            - for duo and quad queues/modes the individual's placement results reflect their team/grouping; solo is self-explanatory
            - will limit results to the top 500 players (minimum 50 matches played per queue); we never like to expose weak/beginner players
            - players that select to be "private" will have their player_name and player_id values hidden
            - {ranking_criteria} can be: 1: team_wins, 2: team_average_placement (shown below), 3: individual_average_kills, 4. win_rate, possibly/probably others as desired
        Warning
        --------
        Expect this data to be cached on an hourly basis because the query to acquire the data will be expensive; don't spam the calls

        Raises
        -------
        pyrez.exceptions.DailyLimit
            |DailyExceptionDescrip|
        TypeError
            |TypeErrorB|
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        _ = self.makeRequest("getleaderboard", [queueId, rankingCriteria])
        return _ if self._responseFormat.equal(Format.XML) or not _ else RealmRoyaleLeaderboard(**_)
    def getPlayer(self, player, platform=None):
        """
        /getplayer[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{player}/{platform}
            Returns league and other high level data for a particular player.
        Parameters
        -------
        player : |INT| or |STR|
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            |DailyExceptionDescrip|
        TypeError
            |TypeErrorB|
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        plat = platform if platform else "hirez" if not str(player).isdigit() or str(player).isdigit() and len(str(player)) <= 8 else "steam"
        _ = self.makeRequest("getplayer", [player, plat])
        #raise PlayerNotFound("Player don't exist or it's hidden")
        return _ if self._responseFormat.equal(Format.XML) or not _ else RealmRoyalePlayer(**_)
    def getMatchHistory(self, playerId, startDatetime=None):
        """
        /getplayermatchhistory[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            |DailyExceptionDescrip|
        TypeError
            |TypeErrorB|
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        methodName = "getplayermatchhistory" if not startDatetime else "getplayermatchhistoryafterdatetime"
        params = [playerId] if not startDatetime else [startDatetime.strftime("yyyyMMddHHmmss") if isinstance(startDatetime, datetime) else startDatetime, playerId]
        _ = self.makeRequest(methodName, params)
        return _ if self._responseFormat.equal(Format.XML) or not _ else RealmMatchHistory(**_)
    def getPlayerStats(self, playerId):
        """
        /getplayerstats[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            |DailyExceptionDescrip|
        TypeError
            |TypeErrorA|
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        return self.makeRequest("getplayerstats", [playerId])
    def getItems(self, language=Language.English):
        """
        Get all talents

        Parameters
        -------
        language : |LanguageParam|
            |LanguageParamDescrip|
        Raises
        -------
        pyrez.exceptions.DailyLimit
            |DailyExceptionDescrip|
        TypeError
            |TypeErrorA|
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        _ = self.makeRequest("gettalents", [language or Language.English])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ RealmRoyaleTalent(**___) for ___ in (_ or []) ]
        return __ if __ else None
