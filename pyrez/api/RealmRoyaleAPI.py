from datetime import datetime

from pyrez.enumerations import Format, Endpoint, Language
from pyrez.models.RealmRoyale import Leaderboard as RealmRoyaleLeaderboard, MatchHistory as RealmMatchHistory, Player as RealmRoyalePlayer, Talent as RealmRoyaleTalent

from .API import API
class RealmRoyaleAPI(API):
    """
    Represents a client that connects to `Realm Royale <https://www.realmroyale.com/>`_ API.

    NOTE
    -------
        Any player with ``Privacy Mode`` enabled in-game will return a null dataset from methods that require a playerId or playerName.
    Parameters
    -------
        devId: :class:`int`
            Used for authentication. This is the Developer ID that you receive from Hi-Rez Studios.
        authKey: :class:`str`
            Used for authentication. This is the Authentication Key that you receive from Hi-Rez Studios.
        responseFormat: Optional[:class:`Format`]
            The response format that will be used by default when making requests. Passing in ``None`` or an invalid value will use the default instead of the passed in value.
        sessionId: Optional[:class:`str`]
            Manually sets an active sessionId. Passing in ``None`` or an invalid sessionId will use the default instead of the passed in value.
        storeSession: Optional[:class:`bool`]
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
        :class:`str` – This is the Authentication Key that you receive from Hi-Rez Studios.
    devId
        :class:`int` – This is the Developer ID that you receive from Hi-Rez Studios.
    onSessionCreated
        :class:`pyrez.events.Event` – A decorator that registers an event to listen to.
    responseFormat
        :class:`Format` – The response format that will be used by default when making requests.
    sessionId
        :class:`str` – The active sessionId.
    statusPage
        :class:`StatusPage` – An object that represents :class:`StatusPage` client.
    storeSession
        :class:`bool` – Allows Pyrez to read and store sessionId in a .json file.
    """
    def __init__(self, devId, authKey, responseFormat=Format.JSON, sessionId=None, storeSession=True):
        """
        The constructor for RealmRoyaleAPI class.
        Keyword arguments/Parameters:
            devId [int]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            authKey [str]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            responseFormat [pyrez.enumerations.Format]: The response format that will be used by default when making requests (default pyrez.enumerations.Format.JSON)
            sessionId [str]: An active sessionId (default None)
            storeSession [bool]: (default True)
        """
        super().__init__(devId, authKey, Endpoint.REALM_ROYALE, responseFormat, sessionId, storeSession)
    def getLeaderboard(self, queueId, rankingCriteria):
        """
        /getleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queueId}/{ranking_criteria}
            - for duo and quad queues/modes the individual's placement results reflect their team/grouping; solo is self-explanatory
            - will limit results to the top 500 players (minimum 50 matches played per queue); we never like to expose weak/beginner players
            - players that select to be "private" will have their player_name and player_id values hidden
            - {ranking_criteria} can be: 1: team_wins, 2: team_average_placement (shown below), 3: individual_average_kills, 4. win_rate, possibly/probably others as desired
            - expect this data to be cached on an hourly basis because the query to acquire the data will be expensive; don't spam the calls
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when an incorrect number of parameters is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        _ = self.makeRequest("getleaderboard", [queueId, rankingCriteria])
        return _ if self._responseFormat.equal(Format.XML) or not _ else RealmRoyaleLeaderboard(**_)
    def getPlayer(self, player, platform=None):
        """
        /getplayer[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{player}/{platform}
            Returns league and other high level data for a particular player.
        Keyword arguments/Parameters:
            player [int] or [str]:
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when an incorrect number of parameters is passed.
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
            Raised when the daily request limit is reached.
        TypeError
            Raised when an incorrect number of parameters is passed.
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
            Raised when the daily request limit is reached.
        TypeError
            Raised when an incorrect number of parameters is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        return self.makeRequest("getplayerstats", [playerId])
    def getItems(self, language=Language.English):
        """
        /gettalents[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{langId}
            Get all talents
        Parameters
        -------
        language: Optional [:class:`int` or :class:`pyrez.enumerations.Language`]
            Passing in ``None`` will use :class:`pyrez.enumerations.Language.English` instead of the passed in value.
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when an incorrect number of parameters is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        _ = self.makeRequest("gettalents", [language or Language.English])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ RealmRoyaleTalent(**___) for ___ in (_ or []) ]
        return __ if __ else None
