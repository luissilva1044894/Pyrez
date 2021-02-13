from datetime import datetime

from pyrez.enumerations import (
    Format,
    Endpoint,
    Language,
)
from pyrez.models.RealmRoyale import (
    Leaderboard as RealmRoyaleLeaderboard,
    MatchHistory as RealmMatchHistory,
    Player as RealmRoyalePlayer,
    Talent as RealmRoyaleTalent,
)

from .API import API
class RealmRoyaleAPI(API):
    """Represents a client that connects to |REALMROYALEGAME| API.

    NOTE
    ----
        |PrivacyMode|

    Keyword Arguments
    -----------------
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
    ------
    pyrez.exceptions.IdOrAuthEmpty
        Raised when the ``Developer ID`` or ``Authentication Key`` is not specified.
    pyrez.exceptions.InvalidArgument
        Raised when an invalid ``Credentials`` is passed.

    Attributes
    ----------
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
        :class:`.StatusPageAPI` – An object that represents :class:`.StatusPageAPI` client.
    storeSession
        |BOOL| – Allows Pyrez to read and store sessionId in a .json file.
    """
    def __init__(self, devId, authKey, responseFormat=Format.JSON, sessionId=None, storeSession=True):
        super().__init__(devId, authKey, Endpoint.REALM_ROYALE, responseFormat, sessionId, storeSession)

    # GET /getleaderboard[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{queueId}/{rankingCriteria}
    def getLeaderboard(self, queueId, rankingCriteria):
        """
        Parameters
        ----------
        rankingCriteria : |INT|
            Can be:
            - 1: team_wins,
            - 2: team_average_placement (shown below),
            - 3: individual_average_kills,
            - 4. win_rate, possibly/probably others as desired

        NOTE
        ----
            - for duo and quad queues/modes the individual's placement results reflect their team/grouping; solo is self-explanatory
            - will limit results to the top 500 players (minimum 50 matches played per queue); we never like to expose weak/beginner players
            - players that select to be "private" will have their player_name and player_id values hidden

        Warning
        -------
        Expect this data to be cached on an hourly basis because the query to acquire the data will be expensive; don't spam the calls

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        _ = self.makeRequest("getleaderboard", [queueId, rankingCriteria])
        return _ if self._responseFormat.equal(Format.XML) or not _ else RealmRoyaleLeaderboard(**_)

    # GET /getplayer[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerIdOrName}/{"hirez"}] | {steamId}/{"steam"}
    def getPlayer(self, player, platform=None):
        """Returns league and other high level data for a particular player.

        Parameters
        ----------
        player : |INT| or |STR|

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        plat = platform if platform else "hirez" if not str(player).isdigit() or str(player).isdigit() and len(str(player)) <= 8 else "steam"
        _ = self.makeRequest("getplayer", [player, plat])
        #raise PlayerNotFound("Player don't exist or it's hidden")
        return _ if self._responseFormat.equal(Format.XML) or not _ else RealmRoyalePlayer(**_)

    # GET /getplayermatchhistory[ResponseFormat]/{devId}/{signature}/{sessionId}/{playerId}
    # GET /getplayermatchhistoryafterdatetime[ResponseFormat]/{devId}/{signature}/{sessionId}/{playerId}
    def getMatchHistory(self, playerId, startDatetime=None):
        """Gets recent matches and high level match statistics for a particular player.

        Parameters
        ----------
        playerId : |INT|

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        methodName = "getplayermatchhistory" if not startDatetime else "getplayermatchhistoryafterdatetime"
        params = [playerId] if not startDatetime else [startDatetime.strftime("yyyyMMddHHmmss") if isinstance(startDatetime, datetime) else startDatetime, playerId]
        _ = self.makeRequest(methodName, params)
        return _ if self._responseFormat.equal(Format.XML) or not _ else RealmMatchHistory(**_)

    # GET /getplayerstats[ResponseFormat]/{devId}/{signature}/{sessionId}/{playerId}
    def getPlayerStats(self, playerId):
        """
        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.makeRequest("getplayerstats", [playerId])

    # GET /getTalents[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{languageCode}
    def getItems(self, language=Language.English):
        """Get all talents

        Parameters
        ----------
        language : |LanguageParam|
            |LanguageParamDescrip|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        _ = self.makeRequest("gettalents", [language or Language.English])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ RealmRoyaleTalent(**___) for ___ in (_ or []) ]
        return __ or None
