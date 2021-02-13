from pyrez.enumerations import Format
from pyrez.models import (
    DemoDetails,
    EsportProLeague,
    LeagueSeason,
    LeagueLeaderboard,
)
from pyrez.models.Smite import (
    GodLeaderboard,
    GodRank,
)

from .API import API
class BaseSmitePaladins(API):
    def __init__(self, devId, authKey, endpoint, responseFormat=Format.JSON, sessionId=None, storeSession=True):
        super().__init__(devId, authKey, endpoint, responseFormat, sessionId, storeSession)

    # GET /getdemodetails[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{matchId}
    def getDemoDetails(self, matchId):
        """Returns information regarding a particular match.

        NOTE
        ----
            Rarely used in lieu of :meth:`getMatch`.

        Parameters
        ----------
        matchId : |INT|
            |MatchIdDescrip|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        _ = self.makeRequest("getdemodetails", [matchId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ DemoDetails(**___) for ___ in (_ or []) ]
        return __ or None

    # GET /getesportsproleaguedetails[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}
    def getEsportsProLeague(self):
        """Returns the matchup information for each matchup for the current eSports Pro League season.

        Raises
        ------
        TypeError
            |TypeError|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        _ = self.makeRequest("getesportsproleaguedetails")
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ EsportProLeague(**___) for ___ in (_ or []) ]
        return __ or None

    # GET /getgodleaderboard[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{godId}/{queueId}
    def getGodLeaderboard(self, godId, queueId):
        """Returns the current season’s leaderboard for a god/queue combination.

        Parameters
        ----------
        godId : |INT|
        queueId : |INT|
            The id of the game mode

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        _ = self.makeRequest("getgodleaderboard", [godId, queueId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ GodLeaderboard(**___) for ___ in (_ or []) ]
        return __ or None

    # GET /getgodranks[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerId}
    def getGodRanks(self, playerId):
        """Returns the Rank and Worshippers value for each God a player has played.

        Parameters
        ----------
        playerId : |INT|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
            List of pyrez.models.GodRank objects
        """
        _ = self.makeRequest("getgodranks", [playerId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ GodRank(**___) for ___ in (_ or []) ]
        return __ or None

    # GET /getleagueleaderboard[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{queueId}/{tier}/{split}
    def getLeagueLeaderboard(self, queueId, tier, split):
        """Returns the top players for a particular league (as indicated by the queue/tier/split parameters).

        Parameters
        ----------
        queueId : |INT|
            The id of the game mode
        tier : |INT|
        split : |INT|

        Raises
        -------
        TypeError
            |TypeErrorC|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        _ = self.makeRequest("getleagueleaderboard", [queueId, tier, split])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ LeagueLeaderboard(**___) for ___ in (_ or []) ]
        return __ or None

    # GET /getleagueseasons[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{queueId}
    def getLeagueSeasons(self, queueId):
        """Provides a list of seasons (including the single active season) for a match queue.

        Parameters
        ----------
        queueId : |INT|
            The id of the game mode

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        _ = self.makeRequest("getleagueseasons", [queueId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ LeagueSeason(**___) for ___ in (_ or []) ]
        return __ or None
