from pyrez.enumerations import *
from datetime import datetime

class BaseAPIResponse:
    def __init__(self, **kwargs):
        self.json = str(kwargs)
    def __str__(self):
        return str(self.json)
class APIResponse(BaseAPIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.retMsg = kwargs.get("ret_msg", None)
    def hasRetMsg(self):
        return self.retMsg != None
class AbstractPlayer(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerId = kwargs.get("Id", 0) or kwargs.get("id", 0)
        self.playerName = kwargs.get("Name", None) or kwargs.get("name", None)
class MergedPlayer(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mergeDatetime = kwargs.get("merge_datetime", None)
        self.playerId = kwargs.get("playerId", 0)
        self.portalId = kwargs.get("portalId", 0)
class Player(AbstractPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.steamId = kwargs.get("steam_id", 0)
class PlayerAcheviements(AbstractPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.assistedKills = kwargs.get("AssistedKills", 0)
        self.campsCleared = kwargs.get("CampsCleared", 0)
        self.deaths = kwargs.get("Deaths", 0)
        self.divineSpree = kwargs.get("DivineSpree", 0)
        self.doubleKills = kwargs.get("DoubleKills", 0)
        self.fireGiantKills = kwargs.get("FireGiantKills", 0)
        self.firstBloods = kwargs.get("FirstBloods", 0)
        self.godLikeSpree = kwargs.get("GodLikeSpree", 0)
        self.goldFuryKills = kwargs.get("GoldFuryKills", 0)
        self.immortalSpree = kwargs.get("ImmortalSpree", 0)
        self.killingSpree = kwargs.get("KillingSpree", 0)
        self.minionKills = kwargs.get("MinionKills", 0)
        self.pentaKills = kwargs.get("PentaKills", 0)
        self.phoenixKills = kwargs.get("PhoenixKills", 0)
        self.playerKills = kwargs.get("PlayerKills", 0)
        self.quadraKills = kwargs.get("QuadraKills", 0)
        self.rampageSpree = kwargs.get("RampageSpree", 0)
        self.shutdownSpree = kwargs.get("ShutdownSpree", 0)
        self.siegeJuggernautKills = kwargs.get("SiegeJuggernautKills", 0)
        self.towerKills = kwargs.get("TowerKills", 0)
        self.tripleKills = kwargs.get("TripleKills", 0)
        self.unstoppableSpree = kwargs.get("UnstoppableSpree", 0)
        self.wildJuggernautKills = kwargs.get("WildJuggernautKills", 0)
class BasePlayer(AbstractPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.createdDatetime = kwargs.get("Created_Datetime", None) or kwargs.get("created_datetime", None)
        if self.createdDatetime and self.createdDatetime != None:
            self.createdDatetime = datetime.strptime(self.createdDatetime, "%m/%d/%Y %H:%M:%S %p")
        self.lastLoginDatetime = kwargs.get("Last_Login_Datetime", None) or kwargs.get("last_login_datetime", None)
        if self.lastLoginDatetime and self.lastLoginDatetime != None:
            self.lastLoginDatetime = datetime.strptime(self.lastLoginDatetime, "%m/%d/%Y %H:%M:%S %p")
        self.accountLevel = wargs.get("Level", 0) or kwargs.get("level", 0)
        self.playerRegion = kwargs.get("Region", None) or kwargs.get("region", None)
class PlayerRealmRoyale(BasePlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.steamId = kwargs.get("steam_id", 0)
        self.portal = kwargs.get("portal", None)
        self.portalId = kwargs.get("portal_id", 0)
        self.portalUserId = kwargs.get("portal_userid", 0)
class BasePSPlayer(BasePlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.activePlayerId = kwargs.get("ActivePlayerId", 0)
        self.hzGamerTag = kwargs.get("hz_gamer_tag", None)
        self.hzPlayerName = kwargs.get("hz_player_name", None)
        self.hoursPlayed = kwargs.get("HoursPlayed", 0)
        self.leaves = kwargs.get("Leaves", 0)
        self.losses = kwargs.get("Losses", 0)
        self.mergedPlayers = kwargs.get("MergedPlayers", None)
        if self.mergedPlayers and self.mergedPlayers != None:
            players = []
            for player in self.mergedPlayers:
                obj = MergedPlayer(**player)
                players.append(obj)
            self.mergedPlayers = players
        self.playedGods = kwargs.get("MasteryLevel", 0)
        self.playerStatusMessage = kwargs.get("Personal_Status_Message", None)
        self.rankedConquest = BaseRanked(**kwargs.get("RankedConquest", None))
        self.teamId = kwargs.get("TeamId", 0)
        self.teamName = kwargs.get("Team_Name", None)
        self.playerRank = Tier(int(kwargs.get("Tier_Conquest", 0)))
        self.totalAchievements = kwargs.get("Total_Achievements", 0)
        self.totalXP = kwargs.get("Total_Worshippers", 0)
        self.wins = kwargs.get("Wins", 0)
    def getWinratio(self, decimals = 2):
        winratio = self.wins /((self.wins + self.losses) if self.wins + self.losses > 1 else 1) * 100.0
        return int(winratio) if winratio % 2 == 0 else round(winratio, decimals)
class PlayerPaladins(BasePSPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.platform = kwargs.get("Platform", None)
        self.rankedController = BaseRanked(**kwargs.get("RankedController", None))
        self.rankedKeyboard = BaseRanked(**kwargs.get("RankedKBM", None))
        self.playerRankController = Tier(int(kwargs.get("Tier_RankedController", 0)))
        self.playerRankKeyboard = Tier(int(kwargs.get("Tier_RankedKBM", 0)))
class PlayerSmite(BasePSPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.avatarURL = kwargs.get("Avatar_URL", None)
        self.rankStatConquest = kwargs.get("Rank_Stat_Conquest", None)
        self.rankStatDuel = kwargs.get("Rank_Stat_Duel", None)
        self.rankStatJoust = kwargs.get("Rank_Stat_Joust", None)
        self.rankedDuel = BaseRanked(**kwargs.get("RankedDuel", None))
        self.rankedJoust = BaseRanked(**kwargs.get("RankedJoust", None))
        self.tierJoust = kwargs.get("Tier_Joust", None)
        self.tierDuel = kwargs.get("Tier_Duel", None)
class BaseAbility:#class Ability
    def __init__(self, **kwargs):
        self.id = kwargs.get("Id", 0)
        self.summary = kwargs.get("Summary", None)
        self.url = kwargs.get("URL", None)
    def __str__(self):
        return "ID: {0} Description: {1} Summary: {2} Url: {3}".format(self.id, self.description, self.summary, self.url)
class ChampionAbility(BaseAbility):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description = kwargs.get("Description", None)
class BaseCharacter(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.abilitys = []
        self.cons = kwargs.get("Cons", None)
        self.health = kwargs.get("Health", 0)
        self.lore = kwargs.get("Lore", None)
        self.onFreeRotation = str(kwargs.get("OnFreeRotation", None)).lower() == 'y'
        self.pantheon = kwargs.get("Pantheon", None)
        self.pros = kwargs.get("Pros", None)
        self.roles = kwargs.get("Roles", None)
        self.speed = kwargs.get("Speed", 0)
        self.title = kwargs.get("Title", None)
        self.type = kwargs.get("Type", None)
class Champion(BaseCharacter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Champions(int(kwargs.get("id")))
            self.godName = str(self.championId)
        except:
            self.godId = kwargs.get("id", 0)
            self.godName = kwargs.get("Name", None)
        for i in range(0, 5):
            obj = ChampionAbility(**kwargs.get("Ability_" + str(i + 1), None))
            self.abilitys.append(obj)
        self.godCardURL = kwargs.get("ChampionCard_URL", None)
        self.godIconURL = kwargs.get("ChampionIcon_URL", None)
        self.latestGod = str(kwargs.get("latestChampion", None)).lower() == 'y'
    def __str__(self):
        st = "Name: {0} ID: {1} Health: {2} Roles: {3} Title: {4}".format(self.godName, self.godId.getId() if isinstance(self.godId, Champions) else self.godId, self.health, self.roles, self.title)
        for i in range(0, len(self.abilitys)):
            st +=(" Ability {0}: {1}").format(i + 1, self.abilitys [i])
        st += "CardUrl: {0} IconUrl: {1} ".format(self.godCardURL, self.godIconURL)
        return st;
class God(BaseCharacter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Gods(int(kwargs.get("id")))
            self.godName = str(self.godId)
        except:
            self.godId = kwargs.get("id", 0)
            self.godName = kwargs.get("Name", None)
        self.latestGod = str(kwargs.get("latestGod", None)).lower() == 'y'
class GodRank(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.assists = kwargs.get("Assists", 0)
        self.deaths = kwargs.get("Deaths", 0)
        try:
            self.godId = Gods(int(kwargs.get("god_id"))) if kwargs.get("god_id") else Champions(int(kwargs.get("champion_id"))) if kwargs.get("champion_id") else 0
            self.godName = str(self.godId)
        except:
            self.godId = kwargs.get("god_id") if kwargs.get("god_id") else kwargs.get("champion_id") if kwargs.get("champion_id") else 0
            self.godName = kwargs.get("god", None) if kwargs.get("god") else kwargs.get("champion", None)
        self.godLevel = kwargs.get("Rank", 0)
        self.gold = kwargs.get("Gold", 0)
        self.kills = kwargs.get("Kills", None)
        self.lastPlayed = kwargs.get("LastPlayed", None)
        self.losses = kwargs.get("Losses", 0)
        self.minionKills = kwargs.get("MinionKills", 0)
        self.minutes = kwargs.get("Minutes", 0)
        self.wins = kwargs.get("Wins", 0)
        self.totalXP = kwargs.get("Worshippers", 0)
        self.playerId = kwargs.get("player_id", 0)
    def getWinratio(self, decimals = 2):
        aux = self.wins + self.losses if self.wins + self.losses > 1 else 1
        winratio = self.wins / aux * 100.0
        return int(winratio) if winratio % 2 == 0 else round(winratio, decimals)
    def getKDA(self, decimals = 2):
        deaths = self.deaths if self.deaths > 1 else 1
        kda = ((self.assists / 2) + self.kills) / deaths
        return int(kda) if kda % 2 == 0 else round(kda, decimals)# + "%";
class BaseItem(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.deviceName = kwargs.get("DeviceName", 0)
        self.iconId = kwargs.get("IconId", 0)
        self.itemId = kwargs.get("ItemId", 0)
        self.itemPrice = kwargs.get("Price", 0)
        self.shortDesc = kwargs.get("ShortDesc", None)
        self.itemIconURL = kwargs.get("itemIcon_URL", None)
    def __eq__(self, other):
        return self.ItemId == other.ItemId
class PaladinsItem(BaseItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.itemDescription = kwargs.get("Description", None)
        try:
            self.godId = Champions(int(kwargs.get("champion_id")))
        except:
            self.godId = kwargs.get("champion_id", 0)
        self.itemType = kwargs.get("item_type", None)
        self.rechargeSeconds = kwargs.get("recharge_seconds", 0)
        self.talentRewardLevel = kwargs.get("talent_reward_level", 0)
class SmiteItem(BaseItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.childItemId = kwargs.get("ChildItemId", 0)
        self.itemDescription = ItemDescription(**kwargs.get("ItemDescription", None))
        self.itemTier = kwargs.get("ItemTier", None)
        self.rootItemId = kwargs.get("RootItemId", 0)
        self.startingItem = kwargs.get("StartingItem", None)
        self.type = kwargs.get("Type", None)
        self.itemDescription = ItemDescription(**kwargs.get("ItemDescription", None)) #Need to improve
class BaseRanked(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.leaves = kwargs.get("Leaves", 0)
        self.losses = kwargs.get("Losses", 0)
        self.rankedName = kwargs.get("Name", None)
        self.currentTrumpPoints = kwargs.get("Points", 0)
        self.prevRank = kwargs.get("PrevRank", 0)
        self.leaderboardIndex = kwargs.get("Rank", 0)
        self.rankStatConquest = kwargs.get("Rank_Stat_Conquest", None)
        self.rankStatDuel = kwargs.get("Rank_Stat_Duel", None)
        self.rankStatJoust = kwargs.get("Rank_Stat_Joust", None)
        self.currentSeason = kwargs.get("Season", 0)
        self.currentRank = Tier(int(kwargs.get("Tier", 0)))
        self.trend = kwargs.get("Trend", 0)
        self.wins = kwargs.get("Wins", 0)
        self.playerId = kwargs.get("player_id", None)
    def getWinratio(self):
        winratio = self.wins /((self.wins + self.losses) if self.wins + self.losses > 1 else 1) * 100.0
        return int(winratio) if winratio % 2 == 0 else round(winratio, 2)
class BaseSkin(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.skinId1 = kwargs.get("skin_id1", 0)
        self.skinId2 = kwargs.get("skin_id2", 0)
        self.skinName = kwargs.get("skin_name", None)
        self.skinNameEnglish = kwargs.get("skin_name_english", None)
    def __eq__(self, other):
        return self.skinID1 == other.skinID1 and self.skinID2 == other.skinID2
class ChampionSkin(BaseSkin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Champions(int(kwargs.get("champion_id")))
            self.godName = str(self.championId)
        except:
            self.godId = kwargs.get("champion_id", 0)
            self.godName = kwargs.get("champion_name", None)
        self.obtainability = kwargs.get("rarity", None)
class GodSkin(BaseSkin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Champions(int(kwargs.get("god_name")))
            self.godName = str(self.godId)
        except:
            self.godId = kwargs.get("god_id", 0)
            self.godName = kwargs.get("god_name", None)
        self.godIconURL = kwargs.get("godIcon_URL", None)
        self.godSkinURL = kwargs.get("godSkin_URL", None)
        self.obtainability = kwargs.get("obtainability", None)
        self.priceFavor = kwargs.get("price_favor", 0)
        self.priceGems = kwargs.get("price_gems", 0)
class DataUsed(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.activeSessions = kwargs.get("Active_Sessions", 0) or kwargs.get("active_sessions", 0)
        self.concurrentSessions = kwargs.get("Concurrent_Sessions", 0) or kwargs.get("concurrent_sessions", 0)
        self.requestLimitDaily = kwargs.get("Request_Limit_Daily", 0) or kwargs.get("request_limit_daily", 0)
        self.sessionCap = kwargs.get("Session_Cap", 0) or kwargs.get("session_cap", 0)
        self.sessionTimeLimit = kwargs.get("Session_Time_Limit", 0) or kwargs.get("session_time_limit", 0)
        self.totalRequestsToday = kwargs.get("Total_Requests_Today", 0) or kwargs.get("total_requests_today", 0)
        self.totalSessionsToday = kwargs.get("Total_Sessions_Today", 0) or kwargs.get("total_sessions_today", 0)
    def __str__(self):
        return "Active sessions: {0} Concurrent sessions: {1} Request limit daily: {2} Session cap: {3} Session time limit: {4} Total requests today: {5} Total sessions today: {6} ".format(self.activeSessions, self.concurrentSessions, self.requestLimitDaily, self.sessionCap, self.sessionTimeLimit, self.totalRequestsToday, self.totalSessionsToday)
    def sessionsLeft(self):
        return self.sessionCap - self.totalSessionsToday if self.sessionCap - self.totalSessionsToday > 0 else 0
    def requestsLeft(self):
        return self.requestLimitDaily - self.totalRequestsToday if self.requestLimitDaily - self.totalRequestsToday > 0 else 0
    def concurrentSessionsLeft(self):
        return self.concurrentSessions - self.activeSessions if self.concurrentSessions - self.activeSessions > 0 else 0
class Friend(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accountId = kwargs.get("account_id", 0)
        self.avatarURL = kwargs.get("avatar_url", None)
        self.playerId = kwargs.get("player_id", 0)
        self.playerName = kwargs.get("name", None)
    def __str__(self):
        return "<Player {0} ({1})>".format(self.playerName, self.playerId)
    #def __hash__(self):
        #return hash(self.playerId)
    def __eq__(self, other):
        return self.playerId == other.playerId
class HiRezServerStatus(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entryDateTime = kwargs.get("entry_datetime", None)
        self.limitedAccess = kwargs.get("limited_access", False)
        self.platform = kwargs.get("platform", None)
        self.status = kwargs.get("status", None).upper()) == "UP"
        self.version = kwargs.get("version", None)
    def __str__(self):
        return "entry_datetime: {0} platform: {1} status: {2} version: {3}".format(self.entryDateTime, self.platform, "UP" if self.status else "DOWN", self.version)
class InGameItem:
    def __init__(self, itemID, itemName, itemLevel):
        self.itemId = itemID
        self.itemName = itemName
        self.itemLevel = itemLevel
    def __str__(self):
        return self.itemName
class ItemDescription:
    def __init__(self, **kwargs):
        self.description = kwargs.get("Description")
        canTry = True
        index = 0
        while canTry:
            try:
                obj = Menuitem(**self.Menuitems.get(str(index)))
                index += 1
                self.menuItems.Append(obj)
            except:
                canTry = False
        self.secondaryDescription = kwargs.get("SecondaryDescription", 0)
class RealmRoyaleLeaderboard(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lastUpdated = kwargs.get("last_updated")
        try:
            self.queueId = RealmRoyaleQueue(int(kwargs.get("queue_id")))
        except:
            self.queueId = kwargs.get("queue_id")
        self.queueName = kwargs.get("queue")
        leaderboardDetails = kwargs.get("leaderboard_details")
        self.leaderboards = []
        for i in leaderboardDetails:
            obj = LeaderboardDetails(**i)
            self.leaderboards.append(obj)
class RealmRoyaleLeaderboardDetails:
    def __init__(self, **kwargs):
        self.matches = kwargs.get("matches")
        self.playerId = kwargs.get("player_id")
        self.playerName = kwargs.get("player_name")
        self.rank = kwargs.get("rank")
        self.teamAVGPlacement = kwargs.get("team_avg_placement")
        self.teamWins = kwargs.get("team_wins")
        self.winPercentage = kwargs.get("win_percentage")
class LoadoutItem:
    def __init__(self, **kwargs):
        self.itemId = kwargs.get("ItemId", 0)
        self.itemName = kwargs.get("ItemName", None)
        self.points = kwargs.get("Points", 0)
    def __str__(self):
        return "{0}({1})".format(self.itemName, self.points)
class BaseMatch(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.matchId = kwargs.get("Match", 0)
        self.skin = kwargs.get("Skin", None)
        self.skinId = kwargs.get("SkinId", 0)
        self.taskForce = kwargs.get("taskForce", 0) or kwargs.get("TaskForce", 0)
class BaseMatchDetail(BaseMatch):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.damageBot = kwargs.get("Damage_Bot", 0)
        self.damageDoneInHand = kwargs.get("Damage_Done_In_Hand", 0)
        self.damageDoneMagical = kwargs.get("Damage_Done_Magical", 0)
        self.damageDonePhysical = kwargs.get("Damage_Done_Physical", 0)
        self.damageMitigated = kwargs.get("Damage_Mitigated", 0)
        self.damageStructure = kwargs.get("Damage_Structure", 0)
        self.damageTaken = kwargs.get("Damage_Taken", 0)
        self.damageTakenMagical = kwargs.get("Damage_Taken_Magical", 0)
        self.damageTakenPhysical = kwargs.get("Damage_Taken_Physical", 0)
        self.deaths = kwargs.get("Deaths", 0)
        self.distanceTraveled = kwargs.get("Distance_Traveled", 0)
        self.healing = kwargs.get("Healing", 0)
        self.healingBot = kwargs.get("Healing_Bot", 0)
        self.healingPlayerSelf = kwargs.get("Healing_Player_Self", 0)
        self.killingSpree = kwargs.get("Killing_Spree", 0)
        self.mapGame = kwargs.get("Map_Game", None)
        self.matchMinutes = kwargs.get("Minutes", 0)
        self.matchRegion = kwargs.get("Region", None)
        self.matchTimeSecond = kwargs.get("Time_In_Match_Seconds", 0)
        self.multiKillMax = kwargs.get("Multi_kill_Max", 0)
        self.objectiveAssists = kwargs.get("Objective_Assists", 0)
        self.playerName = kwargs.get("playerName", None)
        self.surrendered = kwargs.get("Surrendered")
        self.team1Score = kwargs.get("Team1Score", 0)
        self.team2Score = kwargs.get("Team2Score", 0)
        self.wardsPlaced = kwargs.get("Wards_Placed", 0)
        self.winStatus = kwargs.get("Win_Status", None)
        self.winningTaskForce = kwargs.get("Winning_TaskForce", 0)
class MatchHistory(BaseMatchDetail):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.items = []
        self.loadout = []
        for i in range(1, 5):
            obj = InGameItem(kwargs.get("ActiveId{0}".format(i)), kwargs.get("Active_{0}".format(i)), kwargs.get("ActiveLevel{0}".format(i)))
            self.items.append(obj)
        for i in range(1, 7):
            obj = InGameItem(kwargs.get("ItemId{0}".format(i)), kwargs.get("Item_{0}".format(i)), kwargs.get("ItemLevel{0}".format(i)))
            self.loadout.append(obj)
        self.assists = kwargs.get("Assists")
        try:
            self.godId = Champions(int(kwargs.get("ChampionId")))
            self.godName = str(self.godId)
        except:
            self.godId = kwargs.get("ChampionId", 0)
            self.godName = kwargs.get("Champion", None)
        self.creeps = kwargs.get("Creeps", 0)
        self.damage = kwargs.get("Damage", 0)
        self.credits = kwargs.get("Gold", 0)
        self.kills = kwargs.get("Kills", 0)
        self.level = kwargs.get("Level", 0)
        self.matchQueueId = kwargs.get("Match_Queue_Id", 0)
        self.matchTime = kwargs.get("Match_Time", 0)
        self.queue = kwargs.get("Queue", None)
class BasePlayerMatchDetail(BaseMatch):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accountLevel = kwargs.get("Account_Level", 0)
        self.masteryLevel = kwargs.get("Mastery_Level", 0)
class MatchPlayerDetail(BasePlayerMatchDetail):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerCreated = datetime.strptime(kwargs.get("playerCreated", None), "%m/%d/%Y %H:%M:%S %p")
        self.playerId = kwargs.get("playerId", 0)
        self.playerName = kwargs.get("playerName", None)
        self.tier = kwargs.get("Tier", 0)
        self.tierLosses = kwargs.get("tierLosses", 0)
        self.tierWins = kwargs.get("tierWins", 0)
        try:
            self.godId = Champions(int(kwargs.get("ChampionId"))) if kwargs.get("ChampionId") else Gods(int(kwargs.get("GodId")))
            self.godName = str(self.godId)
        except:
            self.godId = kwargs.get("ChampionId", 0) if kwargs.get("ChampionId") else kwargs.get("GodId", 0)
            self.godName = kwargs.get("ChampionName", None) if kwargs.get("ChampionId") else kwargs.get("GodName", None)
        try:
            self.queue = PaladinsQueue(int(kwargs.get("Queue", 0))) if kwargs.get("ChampionId") else SmiteQueue(int(kwargs.get("Queue")))
        except:
            self.queue = kwargs.get("Queue", 0)
class Menuitem:
    def __init__(self, **kwargs):
        self.description = kwargs.get("Description", None)
        self.value = kwargs.get("Value", 0)
class PatchInfo(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gameVersion = kwargs.get("version_string", None) or kwargs.get("version", None)
        if str(kwargs).lower().find("version_code"):
            self.gameVersionCode = kwargs.get("version_code", None)
        if str(kwargs).lower().find("version_id"):
            self.gameVersionId = kwargs.get("version_id", 0)
class Ping:
    def __init__(self, kwargs):
        self.textPlain = str(kwargs)
        textPlain = str(kwargs).split(' ')
        if len(textPlain) > 11:
            self.apiName = textPlain [0]
            self.apiVersion = textPlain [2].replace(')', '')
            self.gamePatch = textPlain [5].replace(']', '')
            self.ping = textPlain [8] == "successful."
            #self.date = "{0} {1} {2}".format(textPlain [10].replace("Date:", ""), textPlain [11], textPlain [12])
            self.date = datetime.strptime("{0} {1} {2}".format(textPlain [10].replace("Date:", ""), textPlain [11], textPlain [12]), "%m/%d/%Y %H:%M:%S %p")
    def __str__(self):
        return "APIName: {0} APIVersion: {1} GameVersion: {2} Ping: {3} Date: {4}".format(self.apiName, self.apiVersion, self.gamePatch, self.ping, self.date)
class PlayerLoadout(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Champions(int(kwargs.get("ChampionId")))
            self.godName = str(self.godId)
        except:
            self.godId = kwargs.get("ChampionId", 0)
            self.godName = kwargs.get("ChampionName", None)
        self.deckId = kwargs.get("DeckId", 0)
        self.deckName = kwargs.get("DeckName", None)
        self.playerId = kwargs.get("playerId", 0)
        self.playerName = kwargs.get("playerName", None)
        cards = kwargs.get("LoadoutItems", None)
        self.cards = []
        for i in cards:
            obj = LoadoutItem(**i)
            self.cards.append(obj)
class PlayerStatus(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currentMatchId = kwargs.get("Match", 0) or kwargs.get("match_id", 0)
        self.currentMatchQueueId = kwargs.get("match_queue_id", 0)
        self.playerStatusId = kwargs.get("status_id", 0) or kwargs.get("status", 0)
        self.playerStatusMessage = kwargs.get("personal_status_message", None)
        self.playerStatusString = kwargs.get("status_string", None) or kwargs.get("status", None)
class Session(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sessionId = kwargs.get("session_id", None)
        self.timeStamp = datetime.strptime(kwargs.get("timestamp", None), "%m/%d/%Y %H:%M:%S %p")
    def isApproved(self):
        return str(self.json).lower().find("approved") != -1
class TestSession:
    def __init__(self, kwargs):
        self.textPlain = str(kwargs)
        textPlain = str(kwargs).split(' ')
        if len(textPlain) > 19:
            self.successfull = self.textPlain.lower().find("this was a successful test with the following parameters added:") != -1
            self.devId = textPlain [11]
            #self.date = "{0} {1} {2}".format(textPlain [13].replace("time:", ""), textPlain [14], textPlain [15])
            self.date = datetime.strptime("{0} {1} {2}".format(textPlain [13].replace("time:", ""), textPlain [14], textPlain [15]), "%m/%d/%Y %H:%M:%S %p")
            self.signature = textPlain [17]
            self.session = textPlain [19]
    def __str__(self):
        return "Successful: {0} devId: {1} Date: {2} Signature: {3} Session: {4}".format(self.successfull, self.devId, self.date, self.signature, self.session)
class EsportProLeagueDetail(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.awayTeamClanId = kwargs.get("away_team_clan_id", 0)
        self.awayTeamName = kwargs.get("away_team_name", None)
        self.awayTeamTagName = kwargs.get("away_team_tagname", None)
        self.homeTeamClanId = kwargs.get("home_team_clan_id", 0)
        self.homeTeamName = kwargs.get("home_team_name", None)
        self.homeTeamTagName = kwargs.get("home_team_tagname", None)
        self.mapInstanceId = kwargs.get("map_instance_id", 0)
        self.matchDate = kwargs.get("match_date", None) # Datetime
        self.matchNumber = kwargs.get("match_number", 0)
        self.matchStatus = kwargs.get("match_status", None)
        self.matchupId = kwargs.get("matchup_id", 0)
        self.region = kwargs.get("region", None)
        self.tournamentName = kwargs.get("tournament_name", None)
        self.winningTeamClanId = kwargs.get("winning_team_clan_id", 0)
class MOTD(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description = kwargs.get("description", None)
        self.gameMode = kwargs.get("gameMode", None)
        self.maxPlayers = kwargs.get("maxPlayers", 0)
        self.name = kwargs.get("name", None)
        self.startDateTime = kwargs.get("startDateTime", None)
        self.team1GodsCSV = kwargs.get("team1GodsCSV", None)
        self.team2GodsCSV = kwargs.get("team2GodsCSV", None)
        self.title = kwargs.get("title", None)
class TeamPlayer(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accountLevel = kwargs.get("AccountLevel", 0)
        self.joinedDatetime = kwargs.get("JoinedDatetime", None)
        self.lastLoginDatetime = kwargs.get("LastLoginDatetime", None)
        self.name = kwargs.get("Name", None)
class TeamSearch(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.teamFounder = kwargs.get("Founder", None)
        self.teamName = kwargs.get("Name", None)
        self.players = kwargs.get("Players", 0)
        self.teamTag = kwargs.get("Tag", None)
        self.teamId = kwargs.get("TeamId", 0)
class TeamDetail(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.teamFounder = kwargs.get("Founder", None)
        self.teamFounderId = kwargs.get("FounderId", 0)
        self.losses = kwargs.get("Losses", 0)
        self.teamName = kwargs.get("Name", None)
        self.players = kwargs.get("Players", 0)
        self.rating = kwargs.get("Rating", 0)
        self.teamTag = kwargs.get("Tag", None)
        self.teamId = kwargs.get("TeamId", 0)
        self.wins = kwargs.get("Wins", 0)
class QueueStats(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.assists = kwargs.get("Assists", 0)
        try:
            self.godId = Gods(int(kwargs.get("GodId"))) or Champions(int(kwargs.get("ChampionId")))
            self.godName = str(self.godId)
        except:
            self.godId = kwargs.get("GodId", 0) or kwargs.get("ChampionId", 0)
            self.godName = kwargs.get("God", None) or kwargs.get("Champion", None)
        self.deaths = kwargs.get("Deaths", 0)
        self.gold = kwargs.get("Gold", 0)
        self.kills = kwargs.get("Kills", 0)
        self.lastPlayed = kwargs.get("LastPlayed", None)
        if self.lastPlayed:
            self.lastPlayed = datetime.strptime(self.lastPlayed, "%m/%d/%Y %H:%M:%S %p")
        self.losses = kwargs.get("Losses", 0)
        self.matches = kwargs.get("Matches", 0)
        self.minutes = kwargs.get("Minutes", 0)
        self.queue = kwargs.get("Queue", None)
        self.wins = kwargs.get("Wins", 0)
        self.playerId = kwargs.get("player_id", 0)

class ChampionCard(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.activeFlagActivationSchedule = str(kwargs.get("active_flag_activation_schedule", None)).lower() == 'y'
        self.activeFlagLti = str(kwargs.get("active_flag_lti", None)).lower() == 'y'
        self.cardDescription = kwargs.get("card_description", None)
        self.cardId1 = kwargs.get("card_id1", 0)
        self.cardId2 = kwargs.get("card_id2", 0)
        self.cardName = kwargs.get("card_name", None)
        self.cardNameEnglish = kwargs.get("card_name_english", None)
        self.godCardURL =  kwargs.get("championCard_URL", None)
        self.godIconURL = kwargs.get("championIcon_URL", None)
        try:
            self.godId = Champions(int(kwargs.get("champion_id")))
            self.godName = str(self.godId)
        except:
            self.godId = kwargs.get("champion_id", 0)
            self.godName = kwargs.get("champion_name", None)
        self.exclusive = str(kwargs.get("exclusive", None)).lower() == 'y'
        self.rank = kwargs.get("rank", 0)
        self.rarity = kwargs.get("rarity", None)
        self.rechargeSeconds = int(kwargs.get("recharge_seconds", 0))
    def getIconURL(self):
        return "https://web2.hirez.com/paladins/champion-icons/{0}.jpg".format(self.godName)
    def getCardURL(self):
        return "https://web2.hirez.com/paladins/champion-cards/{0}.jpg".format(self.cardNameEnglish)
class RealmRoyaleTalent(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.categoryName = kwargs.get("category_name", None)
        self.itemId = kwargs.get("item_id", 0)
        self.lootTableItemId = kwargs.get("loot_table_item_id", 0)
        self.talentDescription = kwargs.get("talent_description", None)
        self.talentName = kwargs.get("talent_name", None)
class MatchDetail(BaseMatchDetail):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.activePlayerId = kwargs.get("ActivePlayerId", 0)
        self.accountLevel = kwargs.get("Account_Level", 0)
        self.masteryLevel = kwargs.get("Mastery_Level", 0)
        self.activeId1 = kwargs.get("ActiveId1", 0)
        self.activeId2 = kwargs.get("ActiveId2", 0)
        self.activeId3 = kwargs.get("ActiveId3", 0)
        self.activeId4 = kwargs.get("ActiveId4", 0)
        self.activeLevel1 = kwargs.get("ActiveLevel1", 0)
        self.activeLevel2 = kwargs.get("ActiveLevel2", 0)
        self.activeLevel3 = kwargs.get("ActiveLevel3", 0)
        self.activeLevel4 = kwargs.get("ActiveLevel4", 0)
        self.assists = kwargs.get("Assists", 0)
        self.banId1 = kwargs.get("BanId1", 0)
        self.banId2 = kwargs.get("BanId2", 0)
        self.banId3 = kwargs.get("BanId3", 0)
        self.banId4 = kwargs.get("BanId4", 0)
        self.banName1 = kwargs.get("Ban_1", None)
        self.banName2 = kwargs.get("Ban_2", None)
        self.banName3 = kwargs.get("Ban_3", None)
        self.banName4 = kwargs.get("Ban_4", None)
        self.campsCleared = kwargs.get("Camps_Cleared", 0)
        self.godId = kwargs.get("ChampionId", 0)
        self.damagePlayer = kwargs.get("Damage_Player", 0)
        self.entryDatetime = kwargs.get("Entry_Datetime", None)
        self.finalMatchLevel = kwargs.get("Final_Match_Level", 0)
        self.goldEarned = kwargs.get("Gold_Earned", 0)
        self.goldPerMinute = kwargs.get("Gold_Per_Minute", 0)
        self.hzGamerTag = kwargs.get("hz_gamer_tag", None)
        self.hzPlayerName = kwargs.get("hz_player_name", None)
        self.inputType = kwargs.get("Input_Type", 0)
        self.itemId1 = kwargs.get("ItemId1", 0)
        self.itemId2 = kwargs.get("ItemId2", 0)
        self.itemId3 = kwargs.get("ItemId3", 0)
        self.itemId4 = kwargs.get("ItemId4", 0)
        self.itemId5 = kwargs.get("ItemId5", 0)
        self.itemId6 = kwargs.get("ItemId6", 0)
        self.itemLevel1 = kwargs.get("ItemLevel1", 0)
        self.itemLevel2 = kwargs.get("ItemLevel2", 0)
        self.itemLevel3 = kwargs.get("ItemLevel3", 0)
        self.itemLevel4 = kwargs.get("ItemLevel4", 0)
        self.itemLevel5 = kwargs.get("ItemLevel5", 0)
        self.itemLevel6 = kwargs.get("ItemLevel6", 0)
        self.itemActive1 = kwargs.get("Item_Active_1", None)
        self.itemActive2 = kwargs.get("Item_Active_2", None)
        self.itemActive3 = kwargs.get("Item_Active_3", None)
        self.itemActive4 = kwargs.get("Item_Active_4", None)
        self.itemPurch1 = kwargs.get("Item_Purch_1", None)
        self.itemPurch2 = kwargs.get("Item_Purch_2", None)
        self.itemPurch3 = kwargs.get("Item_Purch_3", None)
        self.itemPurch4 = kwargs.get("Item_Purch_4", None)
        self.itemPurch5 = kwargs.get("Item_Purch_5", None)
        self.itemPurch6 = kwargs.get("Item_Purch_6", None)#lendaria
        self.killsBot = kwargs.get("Kills_Bot", 0)
        self.killsDouble = kwargs.get("Kills_Double", 0)
        self.killsFireGiant = kwargs.get("Kills_Fire_Giant", 0)
        self.killsFirstBlood = kwargs.get("Kills_First_Blood", 0)
        self.killsGoldFury = kwargs.get("Kills_Gold_Fury", 0)
        self.killsPenta = kwargs.get("Kills_Penta", 0)
        self.killsPhoenix = kwargs.get("Kills_Phoenix", 0)
        self.killsPlayer = kwargs.get("Kills_Player", 0)
        self.killsQuadra = kwargs.get("Kills_Quadra", 0)
        self.killsSiegeJuggernaut = kwargs.get("Kills_Siege_Juggernaut", 0)
        self.killsSingle = kwargs.get("Kills_Single", 0)
        self.killsTriple = kwargs.get("Kills_Triple", 0)
        self.killsWildJuggernaut = kwargs.get("Kills_Wild_Juggernaut", 0)
        self.leagueLosses = kwargs.get("League_Losses", 0)
        self.leaguePoints = kwargs.get("League_Points", 0)
        self.leagueTier = kwargs.get("League_Tier", 0)
        self.leagueWins = kwargs.get("League_Wins", 0)
        self.matchDuration = kwargs.get("Match_Duration", 0)
        self.mergedPlayers = kwargs.get("MergedPlayers", None)
        if self.mergedPlayers and self.mergedPlayers != None:
            players = []
            for player in self.mergedPlayers:
                obj = MergedPlayer(**player)
                players.append(obj)
            self.mergedPlayers = players
        self.objectiveAssists = kwargs.get("Objective_Assists", 0)
        self.partyId = kwargs.get("PartyId", 0)
        self.platform = kwargs.get("Platform", None)
        self.platformType = kwargs.get("Platform_Type", 0)
        self.rankStatLeague = kwargs.get("Rank_Stat_League", 0)
        self.referenceName = kwargs.get("Reference_Name", None)
        self.skin = kwargs.get("Skin", None)
        self.skinId = kwargs.get("SkinId", 0)
        self.structureDamage = kwargs.get("Structure_Damage", 0)
        self.taskForce = kwargs.get("TaskForce", 0)
        self.teamId = kwargs.get("TeamId", 0)
        self.teamName = kwargs.get("Team_Name", None)
        self.towersDestroyed = kwargs.get("Towers_Destroyed", 0)
        self.hasReplay = str(kwargs.get("hasReplay", None)).lower() == 'y'
        self.matchQueueId = kwargs.get("match_queue_id", 0)
        self.mapName = kwargs.get("name", None)
        self.playerName = kwargs.get("playerName", None)
        self.playerId = kwargs.get("playerId", 0)
        self.playerPortalId = kwargs.get("playerPortalId", 0)
        self.playerPortalUserId = kwargs.get("playerPortalUserId", 0)
class DemoDetail(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entryDatetime = kwargs.get("Entry_Datetime", None)
        self.matchId = kwargs.get("Match", 0)
        self.matchTime = kwargs.get("Match_Time", 0)
        self.offlineSpectators = kwargs.get("Offline_Spectators", 0)
        self.realtimeSpectators = kwargs.get("Realtime_Spectators", 0)
        self.recordingEnded = kwargs.get("Recording_Ended", None)
        self.recordingStarted = kwargs.get("Recording_Started", None)
        self.team1AvgLevel = kwargs.get("Team1_AvgLevel", 0)
        self.team1Gold = kwargs.get("Team1_Gold", 0)
        self.team1Kills = kwargs.get("Team1_Kills", 0)
        self.team1Score = kwargs.get("Team1_Score", 0)
        self.team2AvgLevel = kwargs.get("Team2_AvgLevel", 0)
        self.team2Gold = kwargs.get("Team2_Gold", 0)
        self.team2Kills = kwargs.get("Team2_Kills", 0)
        self.team2Score = kwargs.get("Team2_Score", 0)
        self.winningTeam = kwargs.get("Winning_Team", 0)
class SmiteDemoDetail(DemoDetail):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.banId1 = kwargs.get("Ban1", 0)
        self.banId2 = kwargs.get("Ban2", 0)
class PaladinsDemoDetail(DemoDetail):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.banId1 = kwargs.get("BanId1", 0)
        self.banId2 = kwargs.get("BanId2", 0)
        self.banId3 = kwargs.get("BanId3", 0)
        self.banId4 = kwargs.get("BanId4", 0)
        self.banId4 = kwargs.get("Queue", 0)

class BaseCharacterLeaderboard(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.losses = kwargs.get("losses", 0)
        self.playerId = kwargs.get("player_id", 0)
        self.playerName = kwargs.get("player_name", None)
        self.playerRanking = kwargs.get("player_ranking", None)
        self.rank = kwargs.get("rank", 0)
        self.wins = kwargs.get("wins", 0)
    def getWinratio(self):
        winratio = self.wins /((self.wins + self.losses) if self.wins + self.losses > 1 else 1) * 100.0
        return int(winratio) if winratio % 2 == 0 else round(winratio, 2)
class ChampionLeaderboard(BaseCharacterLeaderboard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Champions(int(kwargs.get("champion_id")))
        except:
            self.godId = kwargs.get("champion_id", 0)
class GodLeaderboard(BaseCharacterLeaderboard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Gods(int(kwargs.get("god_id")))
        except:
            self.godId = kwargs.get("god_id", 0)
class PlayerIdInfoForXboxOrSwitch(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerName = kwargs.get("Name", None)
        self.gamerTag = kwargs.get("gamer_tag", None)
        self.platform = kwargs.get("platform", None)#"unknown", "xbox" or "switch"
        self.playerId = kwargs.get("player_id", 0)
        self.portalUserId = kwargs.get("portal_userid", 0)
class PlayerIdByX(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerId = kwargs.get("player_id", 0)
        self.portalUserId = kwargs.get("portal_userid", 0)
        self.portalName = kwargs.get("portal", None)
        self.portalId = kwargs.get("portal_id", 0)
class MatchIdByQueue(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.matchId = kwargs.get("Match", 0) or intkwargs.get("match", 0)
        self.activeFlag = str(kwargs.get("Active_Flag", None)).lower() == 'y' or str(kwargs.get("active_flag", None)).lower() == 'y'
class GodRecommendedItem(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Gods(int(kwargs.get("god_id")))
            self.godName = str(self.godId)
        except:
            self.godId = kwargs.get("god_id", 0)
            self.godName = kwargs.get("god_name", None)
        self.category = kwargs.get("Category", None)
        self.item = kwargs.get("Item", None)
        self.role = kwargs.get("Role", None)
        self.categoryValueId = kwargs.get("category_value_id", 0)
        self.iconId = kwargs.get("icon_id", 0)
        self.itemId = kwargs.get("item_id", 0)
        self.roleValueId = kwargs.get("role_value_id", 0)
class LeagueSeason(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.leagueCompleted = kwargs.get("complete", False)
        self.leagueId = kwargs.get("id", 0)
        self.leagueDescription = kwargs.get("league_description", None)
        self.leagueName = kwargs.get("name", None)
        self.leagueSplit = kwargs.get("round", 0)
        self.leagueSeason = kwargs.get("season", 0)
class LeagueLeaderboard(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.leaves = kwargs.get("Leaves", 0)
        self.losses = kwargs.get("Losses", 0)
        self.playerName = kwargs.get("Name", None)
        self.points = kwargs.get("Points", 0)
        self.prevRank = kwargs.get("PrevRank", 0)
        self.rank = kwargs.get("Rank", 0)
        self.rankStatConquest = kwargs.get("Rank_Stat_Conquest", 0)
        self.rankStatDuel = kwargs.get("Rank_Stat_Duel", 0)
        self.rankStatJoust = kwargs.get("Rank_Stat_Joust", 0)
        self.leagueSeason = kwargs.get("Season", 0)
        self.tier = kwargs.get("Tier", 0)
        self.trend = kwargs.get("Trend", 0)
        self.wins = kwargs.get("Wins", 0)
        self.playerId = kwargs.get("player_id", 0)
class RealmMatch:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.assists = kwargs.get("assists", 0)
        try:
            self.godId = Classes(int(kwargs.get("class_id")))
            self.godName = str(self.godId)
        except:
            self.godId = kwargs.get("class_id", 0)
            self.godName = wargs.get("class_name", None)
        self.creeps = kwargs.get("creeps", 0)
        self.damage = kwargs.get("damage", 0)
        self.damageDoneInHand = kwargs.get("damage_done_in_hand", 0)
        self.damageMitigated = kwargs.get("damage_mitigated", 0)
        self.damageTaken = kwargs.get("damage_taken", 0)
        self.deaths = kwargs.get("deaths", 0)
        self.gold = kwargs.get("gold", 0)
        self.healingBot = kwargs.get("healing_bot", 0)
        self.healingPlayer = kwargs.get("healing_player", 0)
        self.healingPlayerSelf = kwargs.get("healing_player_self", 0)
        self.killingSpreeMax = kwargs.get("killing_spree_max", 0)
        self.kills = kwargs.get("kills", 0)
        self.mapGame = kwargs.get("map_game", None)
        self.matchDatetime = kwargs.get("match_datetime", None)
        self.matchDurationSecs = kwargs.get("match_duration_secs", 0)
        self.matchId = kwargs.get("match_id", 0)
        try:
            self.matchQueueId = RealmRoyaleQueue(int(kwargs.get("match_queue_id")))
        except:
            self.matchQueueId = kwargs.get("match_queue_id", 0)
        self.matchQueueName = kwargs.get("match_queue_name", None)
        self.placement = kwargs.get("placement", 0)
        self.playerId = kwargs.get("player_id", 0)
        self.region = kwargs.get("region", None)
        self.teamId = kwargs.get("team_id", 0)
        self.timeInMatchMinutes = kwargs.get("time_in_match_minutes", 0)
        self.timeInMatchSecs = kwargs.get("time_in_match_secs", 0)
        self.wardsMinesPlaced = kwargs.get("wards_mines_placed", 0)
class RealmMatchHistory(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerId = kwargs.get("id", 0)
        self.playerName = kwargs.get("name", None)
        mats = kwargs.get("matches", None)
        self.matches = []
        for i in mats:
            obj = RealmMatch(**i)
            self.matches.append(obj)
        self.matches = mats
class SmiteTopMatch(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ban1Id = kwargs.get("Ban1Id", 0)
        self.ban1Name = kwargs.get("Ban1", None)
        self.ban2Id = kwargs.get("Ban2Id", 0)
        self.ban2Name = kwargs.get("Ban2", None)
        self.entryDatetime = kwargs.get("Entry_Datetime", None)
        self.liveSpectators = kwargs.get("LiveSpectators", 0)
        self.matchId = kwargs.get("Match", 0)
        self.matchTime = kwargs.get("Match_Time", 0)
        self.offlineSpectators = kwargs.get("OfflineSpectators", 0)
        self.queueName = kwargs.get("Queue", None)
        self.recordingFinished = kwargs.get("RecordingFinished", None)
        self.recordingStarted = kwargs.get("RecordingStarted", None)
        self.team1AvgLevel = kwargs.get("Team1_AvgLevel", 0)
        self.team1Gold = kwargs.get("Team1_Gold", 0)
        self.team1Kills = kwargs.get("Team1_Kills", 0)
        self.team1Score = kwargs.get("Team1_Score", 0)
        self.team2AvgLevel = kwargs.get("Team2_AvgLevel", 0)
        self.team2Gold = kwargs.get("Team2_Gold", 0)
        self.team2Kills = kwargs.get("Team2_Kills", 0)
        self.team2Score = kwargs.get("Team2_Score", 0)
        self.winningTeam = kwargs.get("WinningTeam", 0)

class PaladinsWebsitePost(BaseAPIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.content = kwargs.get("content", None)
        self.featuredImage = kwargs.get("featured_image", None)
        self.postAuthor = kwargs.get("author", None)
        self.postCategories = kwargs.get("real_categories", None)
        self.postId = kwargs.get("id", 0)
        self.postTimestamp = kwargs.get("timestamp", None)
        self.postTitle = kwargs.get("title", None)
        self.slug = kwargs.get("slug", None)
