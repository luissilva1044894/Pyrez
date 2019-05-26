from pyrez.enumerations import Format, Endpoint, Language
from pyrez.exceptions import PlayerNotFound
from pyrez.models import MOTD
from pyrez.models.Smite import God, GodSkin, Item as SmiteItem, Player as SmitePlayer, TopMatch as SmiteTopMatch, GodRecommendedItem
from pyrez.models.Smite.Team import Player as TeamPlayer, Search as TeamSearch, Info as TeamDetail

from .BaseSmitePaladins import BaseSmitePaladins
class SmiteAPI(BaseSmitePaladins):
    """
    Represents a client that connects to `Smite <https://www.smitegame.com/>`_ API.

    NOTE
    -------
        Any player with ``Privacy Mode`` enabled in-game will return a null dataset from methods that require a playerId or playerName.
    Keyword arguments
    -------
    devId: :class:`int`
        Used for authentication. This is the Developer ID that you receive from Hi-Rez Studios.
    authKey: :class:`str`
        Used for authentication. This is the Authentication Key that you receive from Hi-Rez Studios.
    responseFormat: Optional[:class:`.Format`]
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
        :class:`.Format` – The response format that will be used by default when making requests.
    sessionId
        :class:`str` – The active sessionId.
    statusPage
        :class:`pyrez.api.StatusPageAPI` – An object that represents :class:`pyrez.api.StatusPageAPI` client.
    storeSession
        :class:`bool` – Allows Pyrez to read and store sessionId in a .json file.
    """
    def __init__(self, devId, authKey, responseFormat=Format.JSON, sessionId=None, storeSession=True):
        super().__init__(devId, authKey, Endpoint.SMITE, responseFormat, sessionId, storeSession)
    def getGods(self, language=Language.English):
        """
        /getgods[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{language}
            Returns all Gods and their various attributes.
        Parameters
        -------
        language : Optional :class:`int` or :class:`.Language`
            Passing in ``None`` will use :class:`pyrez.enumerations.Language.English` instead of the passed in value.
        Returns:
            List of pyrez.models.God or pyrez.models.Champion objects
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when more (or less) than 1 parameter is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        _ = self.makeRequest("getgods", [language or Language.English])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ God(**___) if isinstance(self, SmiteAPI) else Champion(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getGodRecommendedItems(self, godId, language=Language.English):
        """
        /getgodrecommendeditems[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{language}
            Returns the Recommended Items for a particular God. [SmiteAPI only]
        Parameters
        -------
        godId [int]:
        language : Optional :class:`int` or :class:`.Language`
            Passing in ``None`` will use :class:`pyrez.enumerations.Language.English` instead of the passed in value.
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when more than 2 parameters or less than 1 parameter is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        _ = self.makeRequest("getgodrecommendeditems", [godId, language or Language.English])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ GodRecommendedItem(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getGodSkins(self, godId, language=Language.English):
        """
        /getgodskins[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{language}
            Returns all available skins for a particular God.
        Parameters
        -------
        godId [int]:
        language : Optional :class:`int` or :class:`.Language`
            Passing in ``None`` will use :class:`pyrez.enumerations.Language.English` instead of the passed in value.
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when more than 2 parameters or less than 1 parameter is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        _ = self.makeRequest("getgodskins", [godId, language or Language.English])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ GodSkin(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getItems(self, language=Language.English):
        """
        /getitems[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{language}
            Returns all Items and their various attributes.
        Parameters
        -------
        language : Optional :class:`int` or :class:`.Language`
            Passing in ``None`` will use :class:`pyrez.enumerations.Language.English` instead of the passed in value.
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when more (or less) than 1 parameter is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        _ = BaseSmitePaladins.getItems(self, language or Language.English)
        __ = [ SmiteItem(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getMotd(self):
        """
        /getmotd[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Returns information about the 20 most recent Match-of-the-Days.
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when passing any parameters.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        _ = self.makeRequest("getmotd")
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ MOTD(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getPlayer(self, player, portalId=None):
        _ = BaseSmitePaladins.getPlayer(self, player, portalId)
        if not _:
            raise PlayerNotFound("Player don't exist or it's hidden")
        return SmitePlayer(**_[0])#TypeError: type object argument after ** must be a mapping, not NoneType
    def getTeamDetails(self, clanId):
        """
        /getteamdetails[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{clanId}
            Lists the number of players and other high level details for a particular clan.
        Parameters
        -------
        clanId : int
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when more (or less) than 1 parameter is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        _ = self.makeRequest("getteamdetails", [clanId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ TeamDetail(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getTeamPlayers(self, clanId):
        """
        /getteamplayers[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{clanId}
            Lists the players for a particular clan.
        Parameters
        -------
        clanId : int
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when more (or less) than 1 parameter is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        _ = self.makeRequest("getteamplayers", [clanId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ TeamPlayer(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getTopMatches(self):
        """
        /gettopmatches[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}
            Lists the 50 most watched / most recent recorded matches.
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when passing any parameters.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        _ = self.makeRequest("gettopmatches")
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ SmiteTopMatch(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def searchTeams(self, teamId):
        """
        /searchteams[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{searchTeam}
            Returns high level information for Clan names containing the “searchTeam” string. [SmiteAPI only]
        Parameters
        -------
        teamId : int
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when more (or less) than 1 parameter is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        _ = self.makeRequest("searchteams", [teamId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ TeamSearch(**___) for ___ in (_ or []) ]
        return __ if __ else None
