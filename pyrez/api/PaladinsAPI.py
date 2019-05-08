from pyrez.enumerations import Endpoint, Format, Language, QueuePaladins
from pyrez.exceptions import PlayerNotFound
from pyrez.models import PlayerId
from pyrez.models.Paladins import Champion, ChampionCard, ChampionSkin, Item as PaladinsItem, Player as PaladinsPlayer, Post as PaladinsWebsitePost, Loadout as PlayerLoadout
from pyrez.models.Smite import GodLeaderboard, GodRank

from .BaseSmitePaladins import BaseSmitePaladins
class PaladinsAPI(BaseSmitePaladins):
    """
    Class for handling connections and requests to Paladins API.
    """
    def __init__(self, devId, authKey, responseFormat=Format.JSON, sessionId=None, storeSession=True):
        """
        The constructor for PaladinsAPI class.
        Keyword arguments/Parameters:
            devId [int]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            authKey [str]: Used for authentication. This is the developer ID that you receive from Hi-Rez Studios.
            responseFormat [pyrez.enumerations.Format]: The response format that will be used by default when making requests (default pyrez.enumerations.Format.JSON)
            sessionId [str]: An active sessionId (default None)
            storeSession [bool]: (default True)
        """
        super().__init__(devId, authKey, Endpoint.PALADINS, responseFormat, sessionId, storeSession)
    def getLatestPatchNotes(self, language=Language.English):
        _ = self.makeRequest("https://cms.paladins.com/wp-json/api/get-posts/{}?tag=update-notes".format(language))
        if not _:
            return None
        __ = self.getWebsitePost(language=language, slug=PaladinsWebsitePost(**_[0]).slug)
        return __[0] if __ else None
    def getWebsitePost(self, language=Language.English, slug=None, query=None):
        _ = self.makeRequest("https://cms.paladins.com/wp-json/api/get-post/{}?slug={}&search={}".format(language, slug, query))
        if not _:
            return None
        __ = [ PaladinsWebsitePost(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getChampions(self, language=Language.English):
        """
        /getchampions[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{language}
            Returns all Champions and their various attributes. [PaladinsAPI only]
        Keyword arguments/Parameters:
            language [int] or [pyrez.enumerations.Language]: (default pyrez.enumerations.Language.English)
        """
        _ = self.makeRequest("getchampions", [language])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ Champion(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getChampionCards(self, godId, language=Language.English):
        """
        /getchampioncards[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{language}
            Returns all Champion cards. [PaladinsAPI only]
        Keyword arguments/Parameters:
            language [int] or [pyrez.enumerations.Language]: (default pyrez.enumerations.Language.English)
        """
        _ = self.makeRequest("getchampioncards", [godId, language])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ ChampionCard(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getChampionLeaderboard(self, godId, queueId=QueuePaladins.Live_Competitive_Keyboard):
        """
        /getchampionleaderboard[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{queueId}
            Returns the current season’s leaderboard for a champion/queue combination. [PaladinsAPI; only queue 428]
        Keyword arguments/Parameters:
            godId [int]:
            queueId [int]:
        """
        _ = self.makeRequest("getchampionleaderboard", [godId, queueId])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ GodLeaderboard(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getChampionRanks(self, playerId):
        """
        /getchampionranks[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{playerId}
            Returns the Rank and Worshippers value for each Champion a player has played. [PaladinsAPI only]
        Keyword arguments/Parameters:
            playerId [int]:
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
        Keyword arguments/Parameters:
            godId [int]:
            language [int] or [pyrez.enumerations.Language]: (default pyrez.enumerations.Language.English)
        """
        _ = self.makeRequest("getchampionskins", [godId, language])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ ChampionSkin(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getGods(self, language=Language.English):
        """
        /getgods[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{language}
            Returns all Gods and their various attributes.
        Keyword arguments/Parameters:
            language [int] or [pyrez.enumerations.Language]: (default pyrez.enumerations.Language.English)
        Returns:
            List of pyrez.models.God or pyrez.models.Champion objects
        """
        #_ = self.makeRequest("getgods", [language])
        #if self._responseFormat.equal(Format.XML) or not _:
        #    return _
        #__ = [ God(**___) if isinstance(self, SmiteAPI) else Champion(**___) for ___ in (_ if _ else []) ]
        #return __ if __ else None
        return self.getChampions(language)
    def getGodSkins(self, godId, language=Language.English):
        """
        /getgodskins[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{godId}/{language}
            Returns all available skins for a particular God.
        Keyword arguments/Parameters:
            godId [int]:
            language [int] or [pyrez.enumerations.Language]: (default pyrez.enumerations.Language.English)
        """
        #_ = self.makeRequest("getgodskins", [godId, language])
        #if self._responseFormat.equal(Format.XML) or not _:
        #    return _
        #__ = [ GodSkin(**___) if isinstance(self, SmiteAPI) != -1 else ChampionSkin(**___) for ___ in (_ if _ else []) ]
        #return __ if __ else None
        return self.getChampionSkins(godId, language)
    def getItems(self, language=Language.English):
        """
        /getitems[ResponseFormat]/{devId}/{signature}/{session}/{timestamp}/{language}
            Returns all Items and their various attributes.
        Keyword arguments/Parameters:
            language [int] or [pyrez.enumerations.Language]: (default pyrez.enumerations.Language.English)
        """
        _ = BaseSmitePaladins.getItems(self, language)
        __ = [ PaladinsItem(**___) for ___ in (_ or []) ]
        return __ if __ else None
    def getPlayer(self, player, portalId=None):
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
        Keyword arguments/Parameters:
            playerId [int]:
            language [int] or [pyrez.enumerations.Language]: (default pyrez.enumerations.Language.English)
        """
        _ = self.makeRequest("getplayerloadouts", [playerId, language])
        if self._responseFormat.equal(Format.XML) or not _:
            return _
        __ = [ PlayerLoadout(**___) for ___ in (_ or []) ]
        return __ if __ else None
