from pyrez.enumerations import Format
from pyrez.models import DemoDetails, EsportProLeague, LeagueSeason, LeagueLeaderboard
from pyrez.models.Smite import GodLeaderboard, GodRank

from .APIBase import APIBase
class BaseSmitePaladins(APIBase):
    """
    Class for handling connections and requests to Hi-Rez Studios APIs. IS BETTER DON'T INITALISE THIS YOURSELF!
    """
    def __init__(self, devId, authKey, endpoint, responseFormat=Format.JSON, sessionId=None, storeSession=True):
        """
        The constructor for BaseSmitePaladinsAPI class.
        Keyword arguments/Parameters:
            devId [int]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            authKey [str]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            endpoint [str]: The endpoint that you want to access to retrieve information from the Hi-Rez Studios' API.
            responseFormat [pyrez.enumerations.Format]: The response format that will be used by default when making requests (default pyrez.enumerations.Format.JSON)
            sessionId [str]: An active sessionId (default None)
            storeSession [bool]: (default True)
        """
        super().__init__(devId, authKey, endpoint, responseFormat, sessionId, storeSession)

    def getDemoDetails(self, matchId):
        """
        /getdemodetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{matchId}
            Returns information regarding a particular match.  Rarely used in lieu of getmatchdetails().
        Keyword arguments/Parameters:
            matchId [int]:
        """
        _ = self.makeRequest("getdemodetails", [matchId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ DemoDetails(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getEsportsProLeague(self):
        """
        /getesportsproleaguedetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Returns the matchup information for each matchup for the current eSports Pro League season.
            An important return value is “match_status” which represents a match being scheduled (1), in-progress (2), or complete (3)
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
        Keyword arguments/Parameters:
            godId [int]:
            queueId [int]:
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
        Keyword arguments/Parameters:
            playerId [int]:
        Returns:
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
        Keyword arguments/Parameters:
            queueId [int]:
            tier [int]:
            split [int]:
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
        Keyword arguments/Parameters:
            queueId [int]:
        """
        _ = self.makeRequest("getleagueseasons", [queueId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ LeagueSeason(**___) for ___ in (_ or []) ]
        return __ if __ else None
