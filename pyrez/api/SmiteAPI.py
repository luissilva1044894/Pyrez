from pyrez.enumerations import Format, Endpoint, Language
from pyrez.exceptions import PlayerNotFound
from pyrez.models import MOTD
from pyrez.models.Smite import God, Item as SmiteItem, Player as SmitePlayer, TopMatch as SmiteTopMatch, GodRecommendedItem
from pyrez.models.Smite.Team import Player as TeamPlayer, Search as TeamSearch, Info as TeamDetail

from .BaseSmitePaladinsAPI import BaseSmitePaladinsAPI
class SmiteAPI(BaseSmitePaladinsAPI):
    """
    Class for handling connections and requests to Smite API.
    """
    def __init__(self, devId, authKey, responseFormat=Format.JSON, sessionId=None, storeSession=True):
        """
        The constructor for SmiteAPI class.
        Keyword arguments/Parameters:
            devId [int]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            authKey [str]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            responseFormat [pyrez.enumerations.Format]: The response format that will be used by default when making requests (default pyrez.enumerations.Format.JSON)
            sessionId [str]: An active sessionId (default None)
            storeSession [bool]: (default True)
        """
        super().__init__(devId, authKey, Endpoint.SMITE, responseFormat, sessionId, storeSession)
    def getGods(self, language=Language.English):
        """
        /getgods[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{language}
            Returns all Gods and their various attributes.
        Keyword arguments/Parameters:
            language [int] or [pyrez.enumerations.Language]: (default pyrez.enumerations.Language.English)
        Returns:
            List of pyrez.models.God or pyrez.models.Champion objects
        """
        _ = self.makeRequest("getgods", [language])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ God(**___) if isinstance(self, SmiteAPI) else Champion(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getGodRecommendedItems(self, godId, language=Language.English):
        """
        /getgodrecommendeditems[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{language}
            Returns the Recommended Items for a particular God. [SmiteAPI only]
        Keyword arguments/Parameters:
            godId [int]:
            language [int] or [pyrez.enumerations.Language]: (default pyrez.enumerations.Language.English)
        """
        _ = self.makeRequest("getgodrecommendeditems", [godId, language])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ GodRecommendedItem(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getGodSkins(self, godId, language=Language.English):
        """
        /getgodskins[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{language}
            Returns all available skins for a particular God.
        Keyword arguments/Parameters:
            godId [int]:
            language [int] or [pyrez.enumerations.Language]: (default pyrez.enumerations.Language.English)
        """
        _ = self.makeRequest("getgodskins", [godId, language])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ ChampionSkin(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getItems(self, language=Language.English):
        """
        /getitems[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{language}
            Returns all Items and their various attributes.
        Keyword arguments/Parameters:
            language [int] or [pyrez.enumerations.Language]: (default pyrez.enumerations.Language.English)
        """
        _ = BaseSmitePaladinsAPI.getItems(self, language)
        __ = [ SmiteItem(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getMotd(self):
        """
        /getmotd[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Returns information about the 20 most recent Match-of-the-Days.
        """
        _ = self.makeRequest("getmotd")
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ MOTD(**___) for ___ in (_ if _ else []) ]
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
        _ = BaseSmitePaladinsAPI.getPlayer(self, player, portalId)
        if not _:
            raise PlayerNotFound("Player don't exist or it's hidden")
        return SmitePlayer(**_[0])#TypeError: type object argument after ** must be a mapping, not NoneType
    def getTeamDetails(self, clanId):
        """
        /getteamdetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{clanId}
            Lists the number of players and other high level details for a particular clan.
        Keyword arguments/Parameters:
            clanId [int]:
        """
        _ = self.makeRequest("getteamdetails", [clanId])
        if self._responseFormat.equal(Format.XML) or not _:
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
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ TeamPlayer(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
    def getTopMatches(self):
        """
        /gettopmatches[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Lists the 50 most watched / most recent recorded matches.
        """
        _ = self.makeRequest("gettopmatches")
        if self._responseFormat.equal(Format.XML) or not _:
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
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ TeamSearch(**___) for ___ in (_ if _ else []) ]
        return __ if __ else None
