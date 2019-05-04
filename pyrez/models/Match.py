from .MergedPlayer import MergedPlayer
from .BaseMatchDetail import BaseMatchDetail
class Match(BaseMatchDetail):
    def __init__(self, **kwargs):
        BaseMatchDetail.__init__(self, **kwargs)
        self.activePlayerId = kwargs.get("ActivePlayerId", 0) if kwargs else 0
        self.accountLevel = kwargs.get("Account_Level", 0) if kwargs else 0
        self.masteryLevel = kwargs.get("Mastery_Level", 0) if kwargs else 0
        self.activeId1 = kwargs.get("ActiveId1", 0) if kwargs else 0
        self.activeId2 = kwargs.get("ActiveId2", 0) if kwargs else 0
        self.activeId3 = kwargs.get("ActiveId3", 0) if kwargs else 0
        self.activeId4 = kwargs.get("ActiveId4", 0) if kwargs else 0
        self.activeLevel1 = kwargs.get("ActiveLevel1", 0) if kwargs else 0
        self.activeLevel2 = kwargs.get("ActiveLevel2", 0) if kwargs else 0
        self.activeLevel3 = kwargs.get("ActiveLevel3", 0) if kwargs else 0
        self.activeLevel4 = kwargs.get("ActiveLevel4", 0) if kwargs else 0
        self.assists = kwargs.get("Assists", 0) if kwargs else 0
        self.banId1 = kwargs.get("BanId1", 0) if kwargs else 0
        self.banId2 = kwargs.get("BanId2", 0) if kwargs else 0
        self.banId3 = kwargs.get("BanId3", 0) if kwargs else 0
        self.banId4 = kwargs.get("BanId4", 0) if kwargs else 0
        self.banName1 = kwargs.get("Ban_1", None) if kwargs else None
        self.banName2 = kwargs.get("Ban_2", None) if kwargs else None
        self.banName3 = kwargs.get("Ban_3", None) if kwargs else None
        self.banName4 = kwargs.get("Ban_4", None) if kwargs else None
        self.campsCleared = kwargs.get("Camps_Cleared", 0) if kwargs else 0
        self.godId = kwargs.get("ChampionId", 0) if kwargs else 0
        self.damagePlayer = kwargs.get("Damage_Player", 0) if kwargs else 0
        self.entryDatetime = kwargs.get("Entry_Datetime", None) if kwargs else None
        self.finalMatchLevel = kwargs.get("Final_Match_Level", 0) if kwargs else 0
        self.goldEarned = kwargs.get("Gold_Earned", 0) if kwargs else 0
        self.goldPerMinute = kwargs.get("Gold_Per_Minute", 0) if kwargs else 0
        self.hzGamerTag = kwargs.get("hz_gamer_tag", None) if kwargs else None
        self.hzPlayerName = kwargs.get("hz_player_name", None) if kwargs else None
        self.inputType = kwargs.get("Input_Type", 0) if kwargs else 0
        self.itemId1 = kwargs.get("ItemId1", 0) if kwargs else 0
        self.itemId2 = kwargs.get("ItemId2", 0) if kwargs else 0
        self.itemId3 = kwargs.get("ItemId3", 0) if kwargs else 0
        self.itemId4 = kwargs.get("ItemId4", 0) if kwargs else 0
        self.itemId5 = kwargs.get("ItemId5", 0) if kwargs else 0
        self.itemId6 = kwargs.get("ItemId6", 0) if kwargs else 0
        self.itemLevel1 = kwargs.get("ItemLevel1", 0) if kwargs else 0
        self.itemLevel2 = kwargs.get("ItemLevel2", 0) if kwargs else 0
        self.itemLevel3 = kwargs.get("ItemLevel3", 0) if kwargs else 0
        self.itemLevel4 = kwargs.get("ItemLevel4", 0) if kwargs else 0
        self.itemLevel5 = kwargs.get("ItemLevel5", 0) if kwargs else 0
        self.itemLevel6 = kwargs.get("ItemLevel6", 0) if kwargs else 0
        self.itemActive1 = kwargs.get("Item_Active_1", None) if kwargs else None
        self.itemActive2 = kwargs.get("Item_Active_2", None) if kwargs else None
        self.itemActive3 = kwargs.get("Item_Active_3", None) if kwargs else None
        self.itemActive4 = kwargs.get("Item_Active_4", None) if kwargs else None
        self.itemPurch1 = kwargs.get("Item_Purch_1", None) if kwargs else None
        self.itemPurch2 = kwargs.get("Item_Purch_2", None) if kwargs else None
        self.itemPurch3 = kwargs.get("Item_Purch_3", None) if kwargs else None
        self.itemPurch4 = kwargs.get("Item_Purch_4", None) if kwargs else None
        self.itemPurch5 = kwargs.get("Item_Purch_5", None) if kwargs else None
        self.itemPurch6 = kwargs.get("Item_Purch_6", None) if kwargs else None#lendaria
        self.killsBot = kwargs.get("Kills_Bot", 0) if kwargs else 0
        self.killsDouble = kwargs.get("Kills_Double", 0) if kwargs else 0
        self.killsFireGiant = kwargs.get("Kills_Fire_Giant", 0) if kwargs else 0
        self.killsFirstBlood = kwargs.get("Kills_First_Blood", 0) if kwargs else 0
        self.killsGoldFury = kwargs.get("Kills_Gold_Fury", 0) if kwargs else 0
        self.killsPenta = kwargs.get("Kills_Penta", 0) if kwargs else 0
        self.killsPhoenix = kwargs.get("Kills_Phoenix", 0) if kwargs else 0
        self.killsPlayer = kwargs.get("Kills_Player", 0) if kwargs else 0
        self.killsQuadra = kwargs.get("Kills_Quadra", 0) if kwargs else 0
        self.killsSiegeJuggernaut = kwargs.get("Kills_Siege_Juggernaut", 0) if kwargs else 0
        self.killsSingle = kwargs.get("Kills_Single", 0) if kwargs else 0
        self.killsTriple = kwargs.get("Kills_Triple", 0) if kwargs else 0
        self.killsWildJuggernaut = kwargs.get("Kills_Wild_Juggernaut", 0) if kwargs else 0
        self.leagueLosses = kwargs.get("League_Losses", 0) if kwargs else 0
        self.leaguePoints = kwargs.get("League_Points", 0) if kwargs else 0
        self.leagueTier = kwargs.get("League_Tier", 0) if kwargs else 0
        self.leagueWins = kwargs.get("League_Wins", 0) if kwargs else 0
        self.matchDuration = kwargs.get("Match_Duration", 0) if kwargs else 0
        self.mergedPlayers = [ MergedPlayer(**_) for _ in (kwargs.get("MergedPlayers") if kwargs.get("MergedPlayers", None) else []) ]
        self.objectiveAssists = kwargs.get("Objective_Assists", 0) if kwargs else 0
        self.partyId = kwargs.get("PartyId", 0) if kwargs else 0
        self.platform = kwargs.get("Platform", None) if kwargs else None
        self.platformType = kwargs.get("Platform_Type", 0) if kwargs else 0
        self.rankStatLeague = kwargs.get("Rank_Stat_League", 0) if kwargs else 0
        self.referenceName = kwargs.get("Reference_Name", None) if kwargs else None
        self.skin = kwargs.get("Skin", None) if kwargs else None
        self.skinId = kwargs.get("SkinId", 0) if kwargs else 0
        self.structureDamage = kwargs.get("Structure_Damage", 0) if kwargs else 0
        self.taskForce = kwargs.get("TaskForce", 0) if kwargs else 0
        self.teamId = kwargs.get("TeamId", 0) if kwargs else 0
        self.teamName = kwargs.get("Team_Name", None) if kwargs else None
        self.towersDestroyed = kwargs.get("Towers_Destroyed", 0) if kwargs else 0
        self.hasReplay = str(kwargs.get("hasReplay", None)).lower() == 'y' if kwargs else False
        self.matchQueueId = kwargs.get("match_queue_id", 0) if kwargs else 0
        self.mapName = kwargs.get("name", None) if kwargs else None
        self.playerName = kwargs.get("playerName", None) if kwargs else None
        self.playerId = kwargs.get("playerId", 0) if kwargs else 0
        self.playerPortalId = kwargs.get("playerPortalId", 0) if kwargs else 0
        self.playerPortalUserId = kwargs.get("playerPortalUserId", 0) if kwargs else 0
