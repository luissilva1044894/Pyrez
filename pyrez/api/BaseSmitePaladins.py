from pyrez.enumerations import Format
from pyrez.models import DemoDetails, EsportProLeague, LeagueSeason, LeagueLeaderboard
from pyrez.models.Smite import GodLeaderboard, GodRank

from .API import API
from .APIBase import ASYNC
class BaseSmitePaladins(API):
    if ASYNC:
        @classmethod
        def Async(cls, devId, authKey, endpoint, *, responseFormat=Format.JSON, sessionId=None, storeSession=True, headers=None, cookies=None, raise_for_status=True, logger_name=None, debug_mode=True, loop=None):
            return cls(devId=devId, authKey=authKey, endpoint=endpoint, responseFormat=responseFormat, sessionId=sessionId, storeSession=storeSession, headers=headers, cookies=cookies, raise_for_status=raise_for_status, logger_name=logger_name, debug_mode=debug_mode, is_async=True, loop=loop)
    def __init__(self, devId, authKey, endpoint, *, responseFormat=Format.JSON, sessionId=None, storeSession=True, headers=None, cookies=None, raise_for_status=True, logger_name=None, debug_mode=True, is_async=False, loop=None):
        super().__init__(devId=devId, authKey=authKey, endpoint=endpoint, responseFormat=responseFormat, sessionId=sessionId, storeSession=storeSession, headers=headers, cookies=cookies, raise_for_status=raise_for_status, logger_name=logger_name, debug_mode=debug_mode, is_async=is_async, loop=loop)

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
        return self.__request_method__('getdemodetails', DemoDetails, 1, params=[matchId])

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
        return self.__request_method__('getesportsproleaguedetails', EsportProLeague, 1)

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
        return self.__request_method__('getgodleaderboard', GodLeaderboard, 1, params=[godId, queueId])

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
        return self.__request_method__('getgodranks', GodRank, 1, params=[playerId])

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
        ------
        TypeError
            |TypeErrorC|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('getleagueleaderboard', LeagueLeaderboard, 1, params=[queueId, tier, split])

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
        return self.__request_method__('getleagueseasons', LeagueSeason, 1, params=[queueId])
