from pyrez.enumerations import Endpoint, Format, Language, QueuePaladins
from pyrez.exceptions import PlayerNotFound
from pyrez.models import PlayerId
from pyrez.models.Paladins import Champion, ChampionCard, ChampionSkin, Item as PaladinsItem, Player as PaladinsPlayer, Post as PaladinsWebsitePost, Loadout as PlayerLoadout
from pyrez.models.Smite import GodLeaderboard, GodRank

from .BaseSmitePaladins import BaseSmitePaladins
#https://pythonhosted.org/an_example_pypi_project/sphinx.html#includes
class PaladinsAPI(BaseSmitePaladins):
    """
    Represents a client that connects to `Paladins <https://www.paladins.com/>`_ API.
    
    NOTE
    -------
        Any player with ``Privacy Mode`` enabled in-game will return a null dataset from methods that require a playerId or playerName.
    Keyword arguments
    -------
    devId : :class:`int`
        Used for authentication. This is the Developer ID that you receive from Hi-Rez Studios.
    authKey : :class:`str`
        Used for authentication. This is the Authentication Key that you receive from Hi-Rez Studios.
    responseFormat : Optional :class:`.Format`
        The response format that will be used by default when making requests. Passing in ``None`` or an invalid value will use the default instead of the passed in value.
    sessionId : Optional :class:`str`
        Manually sets an active sessionId. Passing in ``None`` or an invalid sessionId will use the default instead of the passed in value.
    storeSession : Optional :class:`bool`
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
        super().__init__(devId, authKey, Endpoint.PALADINS, responseFormat, sessionId, storeSession)
    def getLatestPatchNotes(self, language=Language.English):
        """
        Parameters
        -------
        language : Optional :class:`int` or :class:`.Language`
            Passing in ``None`` will use :class:`Language.English` instead of the passed in value.
        Raises
        -------
        TypeError
            Raised when more (or less) than 1 parameter is passed.
        """
        _ = self.makeRequest("https://cms.paladins.com/wp-json/api/get-posts/{}?tag=update-notes".format(language or Language.English))
        if not _:
            return None
        __ = self.getWebsitePost(language=language or Language.English, slug=PaladinsWebsitePost(**_[0]).slug)
        return __[0] if __ else None
    def getWebsitePost(self, language=Language.English, slug=None, query=None):
        """
        Parameters
        -------
        language : Optional :class:`int` or :class:`.Language`
            Passing in ``None`` will use :class:`Language.English` instead of the passed in value.
        Raises
        -------
        TypeError
            Raised when more than 3 parameters is passed.
        """
        _ = self.makeRequest("https://cms.paladins.com/wp-json/api/get-post/{}?slug={}&search={}".format(language or Language.English, slug, query))
        if not _:
            return None
        __ = [ PaladinsWebsitePost(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getChampions(self, language=Language.English):
        """
        Returns all Champions and their various attributes.

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
        _ = self.makeRequest("getchampions", [language or Language.English])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ Champion(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getChampionCards(self, godId, language=Language.English):
        """
        Returns all Champion cards.

        More than 2 parameters or less than 1 parameter raises a :class:`TypeError`.

        Parameters
        -------
        godId: :class:`int` or :class:`.Champions`
            The god ID to get their cards.
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
        Returns
        -------
        :class:`list` of :class:`pyrez.models.Paladins.ChampionCard`
            Returns a :class:`list` of :class:`.ChampionCard` objects or ``None``
        """
        _ = self.makeRequest("getchampioncards", [godId, language or Language.English])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ ChampionCard(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getChampionLeaderboard(self, godId, queueId=QueuePaladins.Live_Competitive_Keyboard):
        """
        Returns the current season’s leaderboard for a champion/queue combination.

        More than 2 parameters or less than 1 parameter raises a :class:`TypeError`.
        
        Parameters
        -------
        godId: :class:`int` or :class:`.Champions`
            The god ID.
        queueId: Optional [:class:`int` or :class:`.QueuePaladins`]
            Passing in ``None`` will use :class:`pyrez.enumerations.QueuePaladins.Live_Competitive_Keyboard` instead of the passed in value.
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when more than 2 parameters or less than 1 parameter is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        Returns
        -------
        :class:`list` of :class:`pyrez.models.Smite.GodLeaderboard`
            Returns a :class:`list` of :class:`pyrez.models.Smite.GodLeaderboard` objects or ``None``
        """
        _ = self.makeRequest("getchampionleaderboard", [godId, queueId or QueuePaladins.Live_Competitive_Keyboard])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ GodLeaderboard(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getChampionRanks(self, playerId):
        """
        /getchampionranks[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
            Returns the Rank and Worshippers value for each Champion a player has played. [PaladinsAPI only]
        Parameters
        -------
        playerId [int]:
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when more (or less) than 1 parameter is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        _ = self.makeRequest("getchampionranks", [playerId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ GodRank(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getChampionSkins(self, godId, language=Language.English):
        """
        /getchampionskins[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{language}
            Returns all available skins for a particular Champion. [PaladinsAPI only]
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
        _ = self.makeRequest("getchampionskins", [godId, language or Language.English])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ ChampionSkin(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getGods(self, language=Language.English):
        """
        /getgods[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{language}
            Returns all Gods and their various attributes.
        Parameters
        -------
        language : Optional :class:`int` or :class:`.Language`
            Passing in ``None`` will use :class:`.Language.English` instead of the passed in value.
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when more (or less) than 1 parameter is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        Returns
        -------
            Returns a :class:`list` of :class:`pyrez.models.Paladins.Champion` objects
        """
        #_ = self.makeRequest("getgods", [language])
        #if self._responseFormat.equal(Format.XML) or not _:
        #    return _
        #__ = [ Champion(**___) for ___ in (_ if _ else []) ]
        #return __ if __ else None
        return self.getChampions(language or Language.English)
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
        #_ = self.makeRequest("getgodskins", [godId, language])
        #if self._responseFormat.equal(Format.XML) or not _:
        #    return _
        #__ = [ ChampionSkin(**___) for ___ in (_ if _ else []) ]
        #return __ if __ else None
        return self.getChampionSkins(godId, language or Language.English)
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
        __ = [ PaladinsItem(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getPlayer(self, player, portalId=None):
        """
        Returns league and other high level data for a particular player.

        This method can be used in two different ways:
            getPlayer(player)
            getPlayer(player, portalId)

        Parameters
        -------
        player: [:class:`str`] or [:class:`int`]
            playerName or playerId of the player you want to get info on
        portalId: Optional[:class:`int`] or [:class:`pyrez.enumerations.PortalId`]
            The portalId that you want to looking for (Defaults to ``None``)
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        pyrez.exceptions.PlayerNotFound
             Raised when the player does not exist or it's hidden.
        TypeError
            Raised when more than 2 parameters or less than 1 parameter is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        Returns
        -------
        :class:`list` of pyrez.models.Paladins.Player
            :class:`list` of pyrez.models.Paladins.Player objects with league and other high level data for a particular player.
        """
        _ = BaseSmitePaladins.getPlayer(self, player, portalId)
        if not _:
            raise PlayerNotFound("Player don't exist or it's hidden")
        return PaladinsPlayer(**_[0])#TypeError: type object argument after ** must be a mapping, not NoneType
    def getPlayerId(self, playerName, portalId=None, xboxOrSwitch=False):
        """
        /getplayeridinfoforxboxandswitch[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerName}
            Meaningful only for the Paladins Xbox API. Paladins Xbox data and Paladins Switch data is stored in the same DB.
            Therefore a Paladins Gamer Tag value could be the same as a Paladins Switch Gamer Tag value.
            Additionally, there could be multiple identical Paladins Switch Gamer Tag values.
            The purpose of this method is to return all Player ID data associated with the playerName (gamer tag) parameter.
            The expectation is that the unique player_id returned could then be used in subsequent method calls. [PaladinsAPI only]
        
        Raises
        -------
        pyrez.exceptions.DailyLimit
            Raised when the daily request limit is reached.
        TypeError
            Raised when more than 3 parameters or less than 1 parameter is passed.
        pyrez.exceptions.WrongCredentials
            Raised when a wrong ``Credentials`` is passed.
        """
        if xboxOrSwitch:
            _ = self.makeRequest("getplayeridinfoforxboxandswitch", [playerName])
            if self._responseFormat.equal(Format.XML) or not _:
                return _
            __ = [ PlayerId(**___) for ___ in (_ or []) ]
            return __ if __ else None
        return BaseSmitePaladins.getPlayerId(self, playerName, portalId)
    def getPlayerLoadouts(self, playerId, language=Language.English):
        """
        /getplayerloadouts[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/playerId}/{language}
            Returns deck loadouts per Champion. [PaladinsAPI only]
        Parameters
        -------
        playerId [int]:
        language: Optional [:class:`int` or :class:`.Language`]
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
        _ = self.makeRequest("getplayerloadouts", [playerId, language or Language.English])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ PlayerLoadout(**___) for ___ in (_ or []) ]
        return __ if __ else None
