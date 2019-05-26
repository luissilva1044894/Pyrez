from pyrez.enumerations import Format
from pyrez.models import DemoDetails, EsportProLeague, LeagueSeason, LeagueLeaderboard
from pyrez.models.Smite import GodLeaderboard, GodRank

from .API import API
class BaseSmitePaladins(API):
    def __init__(self, devId, authKey, endpoint, responseFormat=Format.JSON, sessionId=None, storeSession=True):
        super().__init__(devId, authKey, endpoint, responseFormat, sessionId, storeSession)
    def getDemoDetails(self, matchId):
        """
        /getdemodetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{matchId}
            Returns information regarding a particular match.
        NOTE
        -------
            Rarely used in lieu of getMatch().
        Parameters
        -------
        matchId [int]:
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            |dailydesc|
        TypeError
            |TypeErrorA|
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
    
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
            |dailydesc|
        TypeError
            |TypeError|
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
    
        """
        _ = self.makeRequest("getesportsproleaguedetails")
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ EsportProLeague(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getGodLeaderboard(self, godId, queueId):
        """
        /getgodleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{queue}
            Returns the current season’s leaderboard for a god/queue combination. [SmiteAPI only; queues 440, 450, 451 only]
        Parameters
        -------
        godId [int]:
        queueId [int]:
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            |dailydesc|
        TypeError
            |TypeErrorB|
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
    
        """
        _ = self.makeRequest("getgodleaderboard", [godId, queueId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ GodLeaderboard(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getGodRanks(self, playerId):
        """
        /getgodranks[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
            Returns the Rank and Worshippers value for each God a player has played.
        Parameters
        -------
        playerId [int]:
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            |dailydesc|
        TypeError
            |TypeErrorA|
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
    
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
        /getleagueleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queue}/{tier}/{split}
            Returns the top players for a particular league (as indicated by the queue/tier/split parameters).
        Parameters
        -------
        queueId [int]:
        tier [int]:
        split [int]:
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            |dailydesc|
        TypeError
            |TypeErrorC|
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
    
        """
        _ = self.makeRequest("getleagueleaderboard", [queueId, tier, split])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ LeagueLeaderboard(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getLeagueSeasons(self, queueId):
        """
        /getleagueseasons[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{queueId}
            Provides a list of seasons (including the single active season) for a match queue.
        Parameters
        -------
        queueId [int]:
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            |dailydesc|
        TypeError
            |TypeErrorA|
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
    
        """
        _ = self.makeRequest("getleagueseasons", [queueId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ LeagueSeason(**___) for ___ in (_ or []) ]
        return __ if __ else None
