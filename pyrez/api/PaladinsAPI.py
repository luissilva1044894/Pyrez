from pyrez.enumerations import Endpoint, Format, Language, QueuePaladins
from pyrez.exceptions import PlayerNotFound
from pyrez.models import PlayerId
from pyrez.models.Paladins import Champion, ChampionCard, ChampionSkin, Item as PaladinsItem, Player as PaladinsPlayer, Post as PaladinsWebsitePost, Loadout as PlayerLoadout
from pyrez.models.Smite import GodLeaderboard, GodRank

from .BaseSmitePaladins import BaseSmitePaladins
from .APIBase import ASYNC
#https://pythonhosted.org/an_example_pypi_project/sphinx.html#includes
class PaladinsAPI(BaseSmitePaladins):
    """Represents a client that connects to |PALADINSGAME| API.

    NOTE
    ----
        |PrivacyMode|

    Keyword Arguments
    -----------------
    devId : |INT|
        |DevIdConstruct|
    authKey : |STR|
        |AuthKeyConstruct|
    response_format : Optional :class:`.Format`
        |FormatConstruct|
    sessionId : Optional |STR|
        Manually sets an active sessionId. Passing in ``None`` or an invalid sessionId will use the default instead of the passed in value.
    storeSession : Optional |BOOL|
        Allows Pyrez to read and store sessionId in a .json file. Defaults to ``False``.

    Raises
    ------
    pyrez.exceptions.UnauthorizedError
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
    response_format:
        |FormatAtrib|
    sessionId
        |STR| – The active sessionId.
    statusPage
        :class:`.StatusPageAPI` – An object that represents :class:`.StatusPageAPI` client.
    storeSession
        |BOOL| – Allows Pyrez to read and store sessionId in a .json file.
    """
    if ASYNC:
        @classmethod
        def Async(cls, devId, authKey, *, response_format=Format.JSON, sessionId=None, storeSession=True, headers=None, cookies=None, raise_for_status=True, logger_name=None, debug_mode=True, loop=None):
            """An asynchronous PaladinsAPI.

            Basic Usage:
                >>> import pyrez
                >>> paladins = pyrez.PaladinsAPI.Async(devId, authKey)
                >>> player = await paladins.getPlayer('feyrazzle')
            Or as a context manager:
                >>> import pyrez
                >>> async with pyrez.PaladinsAPI.Async(devId, authKey) as paladins:
                >>>    return await paladins.getPlayer('feyrazzle')
            """
            return cls(devId=devId, authKey=authKey, response_format=response_format, sessionId=sessionId, storeSession=storeSession, headers=headers, cookies=cookies, raise_for_status=raise_for_status, logger_name=logger_name, debug_mode=debug_mode, is_async=True, loop=loop)
    def __init__(self, devId, authKey, *, response_format=Format.JSON, sessionId=None, storeSession=True, headers=None, cookies=None, raise_for_status=True, logger_name=None, debug_mode=True, is_async=False, loop=None):
        super().__init__(devId=devId, authKey=authKey, endpoint=Endpoint.PALADINS, response_format=response_format, sessionId=sessionId, storeSession=storeSession, headers=headers, cookies=cookies, raise_for_status=raise_for_status, logger_name=logger_name, debug_mode=debug_mode, is_async=is_async, loop=loop)
    def getLatestPatchNotes(self, language=Language.English):
        """
        Parameters
        ----------
        language : |LanguageParam|
            |LanguageParamDescrip|

        Raises
        ------
        TypeError
            |TypeErrorA|
        """
        _ = self.__request_method__('https://cms.paladins.com/wp-json/api/get-posts/{}?tag=update-notes'.format(language or Language.English), PaladinsWebsitePost, 1)
        if not _:
            return None
        __ = self.getWebsitePost(language=language or Language.English, slug=PaladinsWebsitePost(**_[0]).slug)
        return __[0] if __ else None

    def getWebsitePost(self, language=Language.English, slug=None, query=None):
        """
        Parameters
        ----------
        language : |LanguageParam|
            |LanguageParamDescrip|

        Raises
        ------
        TypeError
            |TypeErrorC|
        """
        return self.__request_method__('https://cms.paladins.com/wp-json/api/get-post/{}?slug={}&search={}'.format(language or Language.English, slug, query), PaladinsWebsitePost, 1)

    # GET /getchampions[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{languageCode}
    def getChampions(self, language=Language.English):
        """Returns all Champions and their various attributes.

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
        return self.__request_method__('getchampions', Champion, 1, params=[language or Language.English])

    # GET /getchampioncards[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{godId}/{languageCode}
    def getChampionCards(self, godId, language=Language.English):
        """Returns all Champion cards.

        Parameters
        ----------
        godId : |INT| or :class:`.Champions`
            The god ID to get their cards.
        language : |LanguageParam|
            |LanguageParamDescrip|

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
        :class:`list` of :class:`pyrez.models.Paladins.ChampionCard`
            Returns a :class:`list` of :class:`.ChampionCard` objects or ``None``
        """
        return self.__request_method__('getchampioncards', ChampionCard, 1, params=[godId, language or Language.English])

    # GET /getchampionleaderboard[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{godId}/{queueId}
    def getChampionLeaderboard(self, godId, queueId=QueuePaladins.Live_Competitive_Keyboard):
        """Returns the current season’s leaderboard for a champion/queue combination.

        Parameters
        ----------
        godId : |INT| or :class:`.Champions`
            The god ID.
        queueId: Optional |INT| or :class:`.QueuePaladins`
            The id of the game mode. Passing in |NONE| will use :class:`pyrez.enumerations.QueuePaladins.Live_Competitive_Keyboard` instead of the passed in value.

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
        :class:`list` of :class:`pyrez.models.Smite.GodLeaderboard`
            Returns a :class:`list` of :class:`pyrez.models.Smite.GodLeaderboard` objects or ``None``
        """
        return self.__request_method__('getchampionleaderboard', GodLeaderboard, 1, params=[godId, queueId or QueuePaladins.Live_Competitive_Keyboard])

    # GET /getchampionranks[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerId}
    def getChampionRanks(self, playerId):
        """Returns the Rank and Worshippers value for each Champion a player has played.

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
        """
        return self.__request_method__('getchampionranks', GodRank, 1, params=[playerId])

    # GET /getchampionskins[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{godId}/{languageCode}
    def getChampionSkins(self, godId, language=Language.English):
        """Returns all available skins for a particular Champion.

        Parameters
        ----------
        godId : |INT|
        language : |LanguageParam|
            |LanguageParamDescrip|

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('getchampionskins', ChampionSkin, 1, params=[godId, language or Language.English])

    # GET /getgods[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{languageCode}
    def getGods(self, language=Language.English):
        """Returns all Gods and their various attributes.

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

        Returns
        -------
            Returns a :class:`list` of :class:`pyrez.models.Paladins.Champion` objects
        """
        #_ = self.makeRequest('getgods', [language])
        #if self._responseFormat.equal(Format.XML) or not _:
        #    return _
        #__ = [ Champion(**___) for ___ in (_ if _ else []) ]
        #return __ if __ else None
        return self.getChampions(language or Language.English)

    # GET /getgodskins[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{godId}/{languageCode}
    def getGodSkins(self, godId, language=Language.English):
        """Returns all available skins for a particular God.

        Parameters
        ----------
        godId : |INT|
        language : |LanguageParam|
            |LanguageParamDescrip|

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        #_ = self.makeRequest('getgodskins', [godId, language])
        #if self._responseFormat.equal(Format.XML) or not _:
        #    return _
        #__ = [ ChampionSkin(**___) for ___ in (_ if _ else []) ]
        #return __ if __ else None
        return self.getChampionSkins(godId, language or Language.English)

    # GET /getitems[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{languagecode}
    def getItems(self, language=Language.English):
        """Returns all Items and their various attributes.

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
        return self.__request_method__('getitems', PaladinsItem, 1, params=[language or Language.English])

    # GET /getplayer[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerIdOrName}
    # GET /getplayer[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerIdOrName}/{portalId}
    def getPlayer(self, player, portalId=None):
        """Returns league and other high level data for a particular player.

        Parameters
        ----------
        player : |STR| or  |INT|
            playerName or playerId of the player you want to get info on
        portalId : Optional |INT| or :class:`pyrez.enumerations.PortalId`
            The portalId that you want to looking for (Defaults to |NONE|)

        Raises
        ------
        pyrez.exceptions.PlayerNotFound
            Raised if the given player does not exist or it's hidden.
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
        :class:`list` of pyrez.models.Paladins.Player
            :class:`list` of pyrez.models.Paladins.Player objects with league and other high level data for a particular player.
        """
        return self.__request_method__('getplayer', PaladinsPlayer, params=[player, portalId] if portalId else [player], raises=PlayerNotFound("Player doesn't exist or it's hidden"))

    # GET /getplayeridbyportaluserid[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{portalId}/{portalUserId}
    def getPlayerId(self, playerName, portalId=None, xboxOrSwitch=False):
        """Function returns a list of Hi-Rez playerId values.

        Parameters
        ----------
        playerName : |STR| or  |INT|
        portalId : Optional |INT| or :class:`pyrez.enumerations.PortalId`
            Only returns a list of Hi-Rez playerId values for portalId provided. (Defaults to |NONE|)
        xboxOrSwitch : |BOOL|
            Meaningful only for the Paladins Xbox and Switch API.

            Therefore a Paladins Gamer Tag value could be the same as a Paladins Switch Gamer Tag value.

            Additionally, there could be multiple identical Paladins Switch Gamer Tag values.
            The purpose of this parameter is to return all Player ID data associated with the playerName (gamer tag) parameter.
            The expectation is that the unique player_id returned could then be used in subsequent method calls.

        Raises
        ------
        TypeError
            |TypeErrorC|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        if xboxOrSwitch:
            return self.__request_method__('getplayeridinfoforxboxandswitch', PlayerId, 1, params=[playerName])
        return BaseSmitePaladins.getPlayerId(self, playerName, portalId)

    # GET /getplayerloadouts[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerId}/{languageCode}
    def getPlayerLoadouts(self, playerId, language=Language.English):
        """Returns deck loadouts per Champion.

        Parameters
        ----------
        playerId : |INT|
        language : |LanguageParam|
            |LanguageParamDescrip|

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('getplayerloadouts', PlayerLoadout, 1, params=[playerId, language or Language.English])
