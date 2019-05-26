from pyrez.enumerations import Format
from pyrez.models import DemoDetails, EsportProLeague, LeagueSeason, LeagueLeaderboard
from pyrez.models.Smite import GodLeaderboard, GodRank

from .API import API
class BaseSmitePaladins(API):
    def __init__(self, devId, authKey, endpoint, responseFormat=Format.JSON, sessionId=None, storeSession=True):
        super().__init__(devId, authKey, endpoint, responseFormat, sessionId, storeSession)
    def getDemoDetails(self, matchId):
        """
        Returns information regarding a particular match.

        NOTE
        -------
            Rarely used in lieu of getMatch().

        Parameters
        -------
        matchId : |INT|
            |MatchIdDescrip|
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            |DailyExceptionDescrip|
        TypeError
            |TypeErrorA|
        pyrez.exceptions.WrongCredentials
            |WrongCredentials|
        """
        _ = self.makeRequest("getdemodetails", [matchId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ DemoDetails(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getEsportsProLeague(self):
        """
        Returns the matchup information for each matchup for the current eSports Pro League season.

        Raises
        -------
        pyrez.exceptions.DailyLimit
            |DailyExceptionDescrip|
        TypeError
            |TypeError|
        pyrez.exceptions.WrongCredentials
            |WrongCredentials|
        """
        _ = self.makeRequest("getesportsproleaguedetails")
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ EsportProLeague(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getGodLeaderboard(self, godId, queueId):
        """
        Returns the current season’s leaderboard for a god/queue combination. [SmiteAPI only; queues 440, 450, 451 only]

        Parameters
        -------
        godId : |INT|
        queueId : |INT|
            The id of the game mode

        Raises
        -------
        pyrez.exceptions.DailyLimit
            |DailyExceptionDescrip|
        TypeError
            |TypeErrorB|
        pyrez.exceptions.WrongCredentials
            |WrongCredentials|
        """
        _ = self.makeRequest("getgodleaderboard", [godId, queueId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ GodLeaderboard(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getGodRanks(self, playerId):
        """
        Returns the Rank and Worshippers value for each God a player has played.

        Parameters
        -------
        playerId : |INT|
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            |DailyExceptionDescrip|
        TypeError
            |TypeErrorA|
        pyrez.exceptions.WrongCredentials
            |WrongCredentials|

        Returns
        -------
            List of pyrez.models.GodRank objects
        """
        _ = self.makeRequest("getgodranks", [playerId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ GodRank(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getLeagueLeaderboard(self, queueId, tier, split):
        """
        Returns the top players for a particular league (as indicated by the queue/tier/split parameters).

        Parameters
        -------
        queueId : |INT|
            The id of the game mode
        tier : |INT|
        split : |INT|

        Raises
        -------
        pyrez.exceptions.DailyLimit
            |DailyExceptionDescrip|
        TypeError
            |TypeErrorC|
        pyrez.exceptions.WrongCredentials
            |WrongCredentials|
        """
        _ = self.makeRequest("getleagueleaderboard", [queueId, tier, split])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ LeagueLeaderboard(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getLeagueSeasons(self, queueId):
        """
        Provides a list of seasons (including the single active season) for a match queue.

        Parameters
        -------
        queueId : |INT|
            The id of the game mode

        Raises
        -------
        pyrez.exceptions.DailyLimit
            |DailyExceptionDescrip|
        TypeError
            |TypeErrorA|
        pyrez.exceptions.WrongCredentials
            |WrongCredentials|
        """
        _ = self.makeRequest("getleagueseasons", [queueId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ LeagueSeason(**___) for ___ in (_ or []) ]
        return __ if __ else None
