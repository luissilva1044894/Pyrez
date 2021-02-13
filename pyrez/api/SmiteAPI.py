from pyrez.enumerations import (
    Format,
    Endpoint,
    Language,
)
from pyrez.exceptions import PlayerNotFound
from pyrez.models import MOTD
from pyrez.models.Smite import (
    God,
    GodSkin,
    Item as SmiteItem,
    Player as SmitePlayer,
    TopMatch as SmiteTopMatch,
    GodRecommendedItem,
)
from pyrez.models.Smite.Team import (
    Player as TeamPlayer,
    Search as TeamSearch,
    Info as TeamDetail,
)

from .BaseSmitePaladins import BaseSmitePaladins
class SmiteAPI(BaseSmitePaladins):
    """Represents a client that connects to |SMITEGAME| API.

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
        super().__init__(devId, authKey, Endpoint.SMITE, responseFormat, sessionId, storeSession)

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

        Returns:
            List of pyrez.models.God or pyrez.models.Champion objects
        """
        _ = self.makeRequest("getgods", [language or Language.English])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ God(**___) for ___ in (_ or []) ]
        return __ or None

    # GET /getgodrecommendeditems[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{godId}/{languageCode}
    def getGodRecommendedItems(self, godId, language=Language.English):
        """Returns the Recommended Items for a particular God.

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
        _ = self.makeRequest("getgodrecommendeditems", [godId, language or Language.English])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ GodRecommendedItem(**___) for ___ in (_ or []) ]
        return __ or None

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
        _ = self.makeRequest("getgodskins", [godId, language or Language.English])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ GodSkin(**___) for ___ in (_ or []) ]
        return __ or None

    # GET /getitems[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{languageCode}
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
        _ = BaseSmitePaladins.getItems(self, language or Language.English)
        __ = [ SmiteItem(**___) for ___ in (_ or []) ]
        return __ or None

    # GET /getmotd[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}
    def getMotd(self):
        """Returns information about the 20 most recent Match-of-the-Days.

        Raises
        ------
        TypeError
            |TypeError|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        _ = self.makeRequest("getmotd")
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ MOTD(**___) for ___ in (_ or []) ]
        return __ or None

    # GET /getplayer[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerIdOrName}
    # GET /getplayer[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerIdOrName}/{portalId}
    def getPlayer(self, player, portalId=None):
        _ = BaseSmitePaladins.getPlayer(self, player, portalId)
        if not _:
            raise PlayerNotFound("Player don't exist or it's hidden")
        return SmitePlayer(**_[0])#TypeError: type object argument after ** must be a mapping, not NoneType

    # GET /getteamdetails[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{clanId}
    def getTeamDetails(self, clanId):
        """Lists the number of players and other high level details for a particular clan.

        Parameters
        ----------
        clanId : |INT|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        _ = self.makeRequest("getteamdetails", [clanId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ TeamDetail(**___) for ___ in (_ or []) ]
        return __ or None

    # GET /getteamplayers[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{clanId}
    def getTeamPlayers(self, clanId):
        """Lists the players for a particular clan.

        Parameters
        ----------
        clanId : |INT|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        _ = self.makeRequest("getteamplayers", [clanId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ TeamPlayer(**___) for ___ in (_ or []) ]
        return __ or None

    # GET /gettopmatches[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}
    def getTopMatches(self):
        """Lists the 50 most watched / most recent recorded matches.

        Raises
        ------
        TypeError
            |TypeError|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        _ = self.makeRequest("gettopmatches")
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ SmiteTopMatch(**___) for ___ in (_ or []) ]
        return __ or None

    # GET /searchteams[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{searchTeam}
    def searchTeams(self, searchTeam):
        """Returns high level information for Clan names containing the ``searchTeam`` string.

        Parameters
        ----------
        searchTeam : |STR|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        _ = self.makeRequest("searchteams", [searchTeam])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ TeamSearch(**___) for ___ in (_ or []) ]
        return __ or None
