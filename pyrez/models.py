from pyrez.enumerations import *
from datetime import datetime

class BaseAPIResponse:
    def __init__(self, **kwargs):
        self.json = str(kwargs)
    def __str__(self):
        return str(self.json)
    def hasRetMsg (self):
        return self.retMsg != None
class APIResponse(BaseAPIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.retMsg = str(kwargs.get("ret_msg", None))
class AbstractPlayer(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerId = int(kwargs.get("Id", 0)) or int(kwargs.get("id", 0))
        self.playerName = str(kwargs.get("Name", None)) or str(kwargs.get("name", None))
class Player(AbstractPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.steamId = int(kwargs.get("steam_id", 0))
class PlayerAcheviements(AbstractPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.assistedKills = int(kwargs.get("AssistedKills", 0))
        self.campsCleared = int(kwargs.get("CampsCleared", 0))
        self.deaths = int(kwargs.get("Deaths", 0))
        self.divineSpree = int(kwargs.get("DivineSpree", 0))
        self.doubleKills = int(kwargs.get("DoubleKills", 0))
        self.fireGiantKills = int(kwargs.get("FireGiantKills", 0))
        self.firstBloods = int(kwargs.get("FirstBloods", 0))
        self.godLikeSpree = int(kwargs.get("GodLikeSpree", 0))
        self.goldFuryKills = int(kwargs.get("GoldFuryKills", 0))
        self.immortalSpree = int(kwargs.get("ImmortalSpree", 0))
        self.killingSpree = int(kwargs.get("KillingSpree", 0))
        self.minionKills = int(kwargs.get("MinionKills", 0))
        self.pentaKills = int(kwargs.get("PentaKills", 0))
        self.phoenixKills = int(kwargs.get("PhoenixKills", 0))
        self.playerKills = int(kwargs.get("PlayerKills", 0))
        self.quadraKills = int(kwargs.get("QuadraKills", 0))
        self.rampageSpree = int(kwargs.get("RampageSpree", 0))
        self.shutdownSpree = int(kwargs.get("ShutdownSpree", 0))
        self.siegeJuggernautKills = int(kwargs.get("SiegeJuggernautKills", 0))
        self.towerKills = int(kwargs.get("TowerKills", 0))
        self.tripleKills = int(kwargs.get("TripleKills", 0))
        self.unstoppableSpree = int(kwargs.get("UnstoppableSpree", 0))
        self.wildJuggernautKills = int(kwargs.get("WildJuggernautKills", 0))
class BasePlayer(AbstractPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.createdDatetime = str(kwargs.get("Created_Datetime", None)) or str(kwargs.get("created_datetime", None))
        if self.createdDatetime:
            self.createdDatetime = datetime.strptime(self.createdDatetime, "%m/%d/%Y %H:%M:%S %p")
        self.lastLoginDatetime = str(kwargs.get("Last_Login_Datetime", None)) or str(kwargs.get("last_login_datetime", None))
        if self.lastLoginDatetime:
            self.lastLoginDatetime = datetime.strptime(self.lastLoginDatetime, "%m/%d/%Y %H:%M:%S %p")
        self.accountLevel = int(kwargs.get("Level", 0)) or int(kwargs.get("level", 0))
        self.playerRegion = str(kwargs.get("Region", None)) or str(kwargs.get("region", None))
class PlayerRealmRoyale(BasePlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.steamId = int(kwargs.get("steam_id", 0))
        self.portal = str(kwargs.get("portal", None))
        self.portalId = int(kwargs.get("portal_id", 0))
        self.portalUserId = int(kwargs.get("portal_userid", 0))
class BasePSPlayer(BasePlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hoursPlayed = int(kwargs.get("HoursPlayed", 0))
        self.leaves = int(kwargs.get("Leaves", 0))
        self.losses = int(kwargs.get("Losses", 0))
        self.playedGods = int(kwargs.get("MasteryLevel", 0))
        self.playerStatusMessage = str(kwargs.get("Personal_Status_Message", None))
        self.rankedConquest = BaseRanked(**kwargs.get("RankedConquest", None))
        self.teamId = int(kwargs.get("TeamId", 0))
        self.teamName = str(kwargs.get("Team_Name", None))
        self.playerRank = Tier(int(kwargs.get("Tier_Conquest", 0)))
        self.totalAchievements = int(kwargs.get("Total_Achievements", 0))
        self.totalworshippers = int(kwargs.get("Total_Worshippers", 0))
        self.wins = int(kwargs.get("Wins", 0))
    def getWinratio(self, decimals = 2):
        winratio = self.wins /((self.wins + self.losses) if self.wins + self.losses > 1 else 1) * 100.0
        return int(winratio) if winratio % 2 == 0 else round(winratio, decimals)
class PlayerPaladins(BasePSPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.platform = str(kwargs.get("Platform", None))
        self.rankedController = BaseRanked(**kwargs.get("RankedController", None))
        self.rankedKeyboard = BaseRanked(**kwargs.get("RankedKBM", None))
        self.playerRankController = Tier(int(kwargs.get("Tier_RankedController", 0)))
        self.playerRankKeyboard = Tier(int(kwargs.get("Tier_RankedKBM", 0)))
class PlayerSmite(BasePSPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.avatarURL = str(kwargs.get("Avatar_URL", None))
        self.rankStatConquest = str(kwargs.get("Rank_Stat_Conquest", None))
        self.rankStatDuel = str(kwargs.get("Rank_Stat_Duel", None))
        self.rankStatJoust = str(kwargs.get("Rank_Stat_Joust", None))
        self.rankedDuel = BaseRanked(**kwargs.get("RankedDuel", None))
        self.rankedJoust = BaseRanked(**kwargs.get("RankedJoust", None))
        self.tierJoust = str(kwargs.get("Tier_Joust", None))
        self.tierDuel = str(kwargs.get("Tier_Duel", None))
class BaseAbility:#class Ability
    def __init__(self, **kwargs):
        self.id = int(kwargs.get("Id", 0))
        self.summary = kwargs.get("Summary", None)
        self.url = kwargs.get("URL", None)
    def __str__(self):
        return "ID: {0} Description: {1} Summary: {2} Url: {3}".format(self.id, self.description, self.summary, self.url)
class ChampionAbility(BaseAbility):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description = str(kwargs.get("Description", None))
class BaseCharacter(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.abilitys = []
        self.cons = str(kwargs.get("Cons", None))
        self.health = int(kwargs.get("Health", 0))
        self.lore = str(kwargs.get("Lore", None))
        self.onFreeRotation = str(kwargs.get("OnFreeRotation", None)).lower() == 'y'
        self.pantheon = str(kwargs.get("Pantheon", None))
        self.pros = str(kwargs.get("Pros", None))
        self.roles = str(kwargs.get("Roles", None))
        self.speed = int(kwargs.get("Speed", 0))
        self.title = str(kwargs.get("Title", None))
        self.type = str(kwargs.get("Type", None))
class Champion(BaseCharacter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.championId = Champions(int(kwargs.get("id", 0)))
            self.championName = str(self.championId)
        except:
            self.championId = int(kwargs.get("id", 0))
            self.championName = str(kwargs.get("Name", None))
        for i in range(0, 5):
            obj = ChampionAbility(**kwargs.get("Ability_" + str(i + 1), None))
            self.abilitys.append(obj)
        self.championCardURL = str(kwargs.get("ChampionCard_URL", None))
        self.championIconURL = str(kwargs.get("ChampionIcon_URL", None))
        self.latestChampion = str(kwargs.get("latestChampion", None)).lower() == 'y'
    def __str__(self):
        st = "Name: {0} ID: {1} Health: {2} Roles: {3} Title: {4}".format(self.championName, self.championId.getId() if isinstance(self.championId, Champions) else self.championId, self.health, self.roles, self.title)
        for i in range(0, len(self.abilitys)):
            st +=(" Ability {0}: {1}").format(i + 1, self.abilitys [i])
        st += "CardUrl: {0} IconUrl: {1} ".format(self.championCardURL, self.championIconURL)
        return st;
class God(BaseCharacter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Gods(int(kwargs.get("id", 0)))
            self.godName = str(self.godId)
        except:
            self.godId = int(kwargs.get("id", 0))
            self.godName = str(kwargs.get("Name", None))
        self.latestGod = str(kwargs.get("latestGod", None)).lower() == 'y'
class BaseCharacterRank(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.assists = int(kwargs.get("Assists", 0))
        self.deaths = int(kwargs.get("Deaths", 0))
        self.kills = int(kwargs.get("Kills", None))
        self.losses = int(kwargs.get("Losses", 0))
        self.minionKills = int(kwargs.get("MinionKills", 0))
        self.godLevel = int(kwargs.get("Rank", 0))
        self.wins = int(kwargs.get("Wins", 0))
        self.worshippers = int(kwargs.get("Worshippers", 0))
        self.playerId = int(kwargs.get("player_id", 0))
    def getWinratio(self, decimals = 2):
        aux = self.wins + self.losses if self.wins + self.losses > 1 else 1
        winratio = self.wins / aux * 100.0
        return int(winratio) if winratio % 2 == 0 else round(winratio, decimals)
    def getKDA(self, decimals = 2):
        deaths = self.deaths if self.deaths > 1 else 1
        kda = ((self.assists / 2) + self.kills) / deaths
        return int(kda) if kda % 2 == 0 else round(kda, decimals)# + "%";
class GodRank(BaseCharacterRank):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Gods(int(kwargs.get("god_id"))) if kwargs.get("god_id") else Champions(int(kwargs.get("champion_id"))) if kwargs.get("champion_id") else -1
            self.godName = str(self.godId)
        except:
            self.godId = int(kwargs.get("god_id")) if kwargs.get("god_id") else int(kwargs.get("champion_id")) if kwargs.get("champion_id") else -1
            self.godName = str(kwargs.get("champion", None)) if kwargs.get("champion") else str(kwargs.get("god", None))
class BaseItem(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.deviceName = int(kwargs.get("DeviceName", 0))
        self.iconId = int(kwargs.get("IconId", 0))
        self.itemId = int(kwargs.get("ItemId", 0))
        self.price = int(kwargs.get("Price", 0))
        self.shortDesc = str(kwargs.get("ShortDesc", None))
        self.itemIconURL = str(kwargs.get("itemIcon_URL", None))
    def __eq__(self, other):
        return self.ItemId == other.ItemId
class PaladinsItem(BaseItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description = str(kwargs.get("Description", None))
        try:
            self.championId = Champions(int(kwargs.get("champion_id", 0)))
        except:
            self.championId = int(kwargs.get("champion_id", 0))
        self.itemType = str(kwargs.get("item_type", None))
        self.talentRewardLevel = int(kwargs.get("talent_reward_level", 0))
class SmiteItem(BaseItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.childItemId = int(kwargs.get("ChildItemId", 0))
        self.itemDescription = ItemDescription(**kwargs.get("ItemDescription", None))
        self.itemTier = str(kwargs.get("ItemTier", None))
        self.rootItemId = int(kwargs.get("RootItemId", 0))
        self.startingItem = str(kwargs.get("StartingItem", None))
        self.type = str(kwargs.get("Type", None))
class BaseRanked(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.leaves = int(kwargs.get("Leaves", 0))
        self.losses = int(kwargs.get("Losses", 0))
        self.rankedName = str(kwargs.get("Name", None))
        self.currentTrumpPoints = int(kwargs.get("Points", 0))
        self.prevRank = int(kwargs.get("PrevRank", 0))
        self.leaderboardIndex = int(kwargs.get("Rank", 0))
        self.rankStatConquest = kwargs.get("Rank_Stat_Conquest", None)
        self.rankStatDuel = kwargs.get("Rank_Stat_Duel", None)
        self.rankStatJoust = kwargs.get("Rank_Stat_Joust", None)
        self.currentSeason = int(kwargs.get("Season", 0))
        self.currentRank = Tier(int(kwargs.get("Tier", 0)))
        self.trend = int(kwargs.get("Trend", 0))
        self.wins = int(kwargs.get("Wins", 0))
        self.playerId = kwargs.get("player_id", None)
    def getWinratio(self):
        winratio = self.wins /((self.wins + self.losses) if self.wins + self.losses > 1 else 1) * 100.0
        return int(winratio) if winratio % 2 == 0 else round(winratio, 2)
class BaseSkin(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.skinId1 = int(kwargs.get("skin_id1", 0))
        self.skinId2 = int(kwargs.get("skin_id2", 0))
        self.skinName = str(kwargs.get("skin_name", None))
        self.skinNameEnglish = str(kwargs.get("skin_name_english", None))
    def __eq__(self, other):
        return self.skinID1 == other.skinID1 and self.skinID2 == other.skinID2
class ChampionSkin(BaseSkin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.championId = Champions(int(kwargs.get("champion_id", 0)))
            self.championName = str(self.championId)
        except:
            self.championId = int(kwargs.get("champion_id", 0))
            self.championName = str(kwargs.get("champion_name", None))
        self.rarity = str(kwargs.get("rarity", None))
class GodSkin(BaseSkin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Champions(int(kwargs.get("god_name", 0)))
            self.godName = str(self.championId)
        except:
            self.godId = int(kwargs.get("god_id", 0))
            self.godName = str(kwargs.get("god_name", None))
        self.godIconURL = str(kwargs.get("godIcon_URL", None))
        self.godSkinURL = str(kwargs.get("godSkin_URL", None))
        self.obtainability = str(kwargs.get("obtainability", None))
        self.priceFavor = int(kwargs.get("price_favor", 0))
        self.priceGems = int(kwargs.get("price_gems", 0))
class DataUsed(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.activeSessions = int(kwargs.get("Active_Sessions", 0)) or int(kwargs.get("active_sessions", 0))
        self.concurrentSessions = int(kwargs.get("Concurrent_Sessions", 0)) or int(kwargs.get("concurrent_sessions", 0))
        self.requestLimitDaily = int(kwargs.get("Request_Limit_Daily", 0)) or int(kwargs.get("request_limit_daily", 0))
        self.sessionCap = int(kwargs.get("Session_Cap", 0)) or int(kwargs.get("session_cap", 0))
        self.sessionTimeLimit = int(kwargs.get("Session_Time_Limit", 0)) or int(kwargs.get("session_time_limit", 0))
        self.totalRequestsToday = int(kwargs.get("Total_Requests_Today", 0)) or int(kwargs.get("total_requests_today", 0))
        self.totalSessionsToday = int(kwargs.get("Total_Sessions_Today", 0)) or int(kwargs.get("total_sessions_today", 0))
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
        self.accountId = int(kwargs.get("account_id", 0))
        self.avatarURL = str(kwargs.get("avatar_url", None))
        self.playerId = int(kwargs.get("player_id", 0))
        self.playerName = str(kwargs.get("name", None))
    def __str__(self):
        return "<Player {0} ({1})>".format(self.playerName, self.playerId)
    #def __hash__(self):
        #return hash(self.playerId)
    def __eq__(self, other):
        return self.playerId == other.playerId
class HiRezServerStatus(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entryDateTime = str(kwargs.get("entry_datetime", None))
        self.platform = str(kwargs.get("platform", None))
        self.status = str(kwargs.get("status", None).upper()) == "UP"
        self.version = str(kwargs.get("version", None))
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
        self.description = int(kwargs.get("Description"))
        canTry = True
        index = 0
        while canTry:
            try:
                obj = Menuitem(**self.Menuitems.get(str(index)))
                index += 1
                self.menuItems.Append(obj)
            except:
                canTry = False
        self.secondaryDescription = int(kwargs.get("SecondaryDescription", 0))
class Leaderboard(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lastUpdated = kwargs.get("last_updated")
        self.queue = kwargs.get("queue")
        self.queueId = int(kwargs.get("queue_id"))
        leaderboardDetails = kwargs.get("leaderboard_details")
        self.leaderboards = []
        for i in range(0, len(leaderboardDetails)):
            obj = LeaderboardDetails(** leaderboardDetails [i])
            self.leaderboards.append(obj)
class LeaderboardDetails:
    def __init__(self, **kwargs):
        self.matches = int(kwargs.get("matches"))
        self.playerId = kwargs.get("player_id")
        self.playerName = kwargs.get("player_name")
        self.rank = int(kwargs.get("rank"))
        self.teamAVGPlacement = float(kwargs.get("team_avg_placement"))
        self.teamWins = int(kwargs.get("team_wins"))
        self.winPercentage = float(kwargs.get("win_percentage"))
class LoadoutItem:
    def __init__(self, **kwargs):
        self.itemId = int(kwargs.get("ItemId", 0))
        self.itemName = str(kwargs.get("ItemName", None))
        self.points = int(kwargs.get("Points", 0))
    def __str__(self):
        return "{0}({1})".format(self.itemName, self.points)
class MatchHistory(APIResponse):
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
            self.championId = Champions(int(kwargs.get("ChampionId", 0)))
            self.championName = str(self.championId)
        except:
            self.championId = int(kwargs.get("ChampionId", 0))
            self.championName = str(kwargs.get("Champion", None))
        self.creeps = kwargs.get("Creeps")
        self.damage = kwargs.get("Damage")
        self.damageBot = kwargs.get("Damage_Bot")
        self.damageDoneInHand = kwargs.get("Damage_Done_In_Hand")
        self.damageMitigated = kwargs.get("Damage_Mitigated")
        self.damageStructure = kwargs.get("Damage_Structure")
        self.damageTaken = kwargs.get("Damage_Taken")
        self.damageTakenMagical = kwargs.get("Damage_Taken_Magical")
        self.damageTakenPhysical = kwargs.get("Damage_Taken_Physical")
        self.deaths = kwargs.get("Deaths")
        self.distanceTraveled = kwargs.get("Distance_Traveled")
        self.credits = kwargs.get("Gold")
        self.healing = kwargs.get("Healing")
        self.healingBot = kwargs.get("Healing_Bot")
        self.healingPlayerSelf = kwargs.get("Healing_Player_Self")
        self.killingSpree = kwargs.get("Killing_Spree")
        self.kills = kwargs.get("Kills")
        self.level = kwargs.get("Level")
        self.mapGame = kwargs.get("Map_Game")
        self.matchMinutes = kwargs.get("Minutes")
        self.matchRegion = kwargs.get("Region")
        self.matchQueueId = kwargs.get("Match_Queue_Id")
        self.matchTime = kwargs.get("Match_Time")
        self.matchTimeSecond = kwargs.get("Time_In_Match_Seconds")
        self.matchId = kwargs.get("Match")
        self.multiKillMax = kwargs.get("Multi_kill_Max")
        self.objectiveAssists = kwargs.get("Objective_Assists")
        self.queue = kwargs.get("Queue")
        self.skin = kwargs.get("Skin")
        self.skinId = kwargs.get("SkinId")
        self.surrendered = kwargs.get("Surrendered")
        self.taskForce = kwargs.get("TaskForce")
        self.team1Score = kwargs.get("Team1Score")
        self.team2Score = kwargs.get("Team2Score")
        self.wardsPlaced = kwargs.get("Wards_Placed")
        self.winStatus = kwargs.get("Win_Status")
        self.winningTaskForce = kwargs.get("Winning_TaskForce")
        self.playerName = kwargs.get("playerName")
class MatchPlayerDetail(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accountLevel = int(kwargs.get("Account_Level", 0))
        try:
            self.championId = Champions(int(kwargs.get("ChampionId", 0)))
            self.championName = str(self.championId)
        except:
            self.championId = int(kwargs.get("ChampionId", 0))
            self.championName = str(kwargs.get("ChampionName", None))
        self.masteryLevel = int(kwargs.get("Mastery_Level", 0))
        self.matchId = int(kwargs.get("Match", 0))
        try:
            self.queue = PaladinsQueue(int(kwargs.get("Queue", 0)))
        except:
            self.queue = int(kwargs.get("Queue", 0))
        self.skinId = int(kwargs.get("SkinId", 0))
        self.playerCreated = datetime.strptime(kwargs.get("playerCreated", None), "%m/%d/%Y %H:%M:%S %p")
        self.playerId = int(kwargs.get("playerId", 0))
        self.playerName = str(kwargs.get("playerName", None))
        self.taskForce = int(kwargs.get("taskForce", 0))
        self.tier = int(kwargs.get("Tier", 0))
        self.tierLosses = int(kwargs.get("tierLosses", 0))
        self.tierWins = int(kwargs.get("tierWins", 0))
class Menuitem:
    def __init__(self, **kwargs):
        self.description = int(kwargs.get("Description", 0))
        self.value = int(kwargs.get("Value", 0))
class PatchInfo(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gameVersion = str(kwargs.get("version_string", None)) or str(kwargs.get("version", None))
        if str(kwargs).lower().find("version_code"):
            self.gameVersionCode = str(kwargs.get("version_code", None))
        if str(kwargs).lower().find("version_id"):
            self.gameVersionId = int(kwargs.get("version_id", 0))
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
            self.championId = Champions(int(kwargs.get("ChampionId", 0)))
            self.championName = str(self.championId)
        except:
            self.championId = int(kwargs.get("ChampionId", 0))
            self.championName = str(kwargs.get("ChampionName", None))
        self.deckId = int(kwargs.get("DeckId", 0))
        self.deckName = str(kwargs.get("DeckName", None))
        self.playerId = int(kwargs.get("playerId", 0))
        self.playerName = str(kwargs.get("playerName", None))
        cards = kwargs.get("LoadoutItems")
        self.cards = []
        for i in cards:
            obj = LoadoutItem(**i)
            self.cards.append(obj)
class PlayerStatus(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currentMatchId = int(kwargs.get("match_id", 0)) or int(kwargs.get("Match", 0))
        self.currentMatchQueueId = int(kwargs.get("match_queue_id", 0))
        self.playerStatus = int(kwargs.get("status_id", 0)) or kwargs.get("status", 0)
        self.playerStatusString = str(kwargs.get("status_string", None)) or str(kwargs.get("status", None))
        self.playerStatusMessage = str(kwargs.get("personal_status_message", None))
class Session(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sessionId = str(kwargs.get("session_id", None))
        self.timeStamp = datetime.strptime(str(kwargs.get("timestamp", None)), "%m/%d/%Y %H:%M:%S %p")
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
        self.awayTeamClanId = int(kwargs.get("away_team_clan_id", 0))
        self.awayTeamName = str(kwargs.get("away_team_name", None))
        self.awayTeamTagName = str(kwargs.get("away_team_tagname", None))
        self.homeTeamClanId = int(kwargs.get("home_team_clan_id", 0))
        self.homeTeamName = str(kwargs.get("home_team_name", None))
        self.homeTeamTagName = str(kwargs.get("home_team_tagname", None))
        self.mapInstanceId = int(kwargs.get("map_instance_id", 0))
        self.matchDate = str(kwargs.get("match_date", None)) # Datetime
        self.matchNumber = int(kwargs.get("match_number", 0))
        self.matchStatus = str(kwargs.get("match_status", None))
        self.matchupId = int(kwargs.get("matchup_id", 0))
        self.region = str(kwargs.get("region", None))
        self.tournamentName = str(kwargs.get("tournament_name", None))
        self.winningTeamClanId = int(kwargs.get("winning_team_clan_id", 0))
class GodLeaderboard(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.godId = Gods(int(kwargs.get("god_id", 0)))
        except:
            self.godId = int(kwargs.get("god_id", 0))
        self.losses = int(kwargs.get("losses", 0))
        self.playerId = int(kwargs.get("player_id", 0))
        self.playerName = str(kwargs.get("player_name", None))
        self.playerRanking = str(kwargs.get("player_ranking", None))
        self.rank = int(kwargs.get("rank", 0))
        self.wins = int(kwargs.get("wins", 0))
class MOTD(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description = str(kwargs.get("description", None))
        self.gameMode = str(kwargs.get("gameMode", None))
        self.maxPlayers = str(kwargs.get("maxPlayers", None))
        self.name = str(kwargs.get("name", None))
        self.startDateTime = str(kwargs.get("startDateTime", None))
        self.team1GodsCSV = str(kwargs.get("team1GodsCSV", None))
        self.team2GodsCSV = str(kwargs.get("team2GodsCSV", None))
        self.title = str(kwargs.get("title", None))
class TeamPlayer(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accountLevel = int(kwargs.get("AccountLevel", 0))
        self.joinedDatetime = str(kwargs.get("JoinedDatetime", None))
        self.lastLoginDatetime = str(kwargs.get("LastLoginDatetime", None))
        self.name = str(kwargs.get("Name", None))
class TeamDetail(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.founder = str(kwargs.get("Founder", None))
        self.founderId = int(kwargs.get("FounderId", 0))
        self.losses = int(kwargs.get("Losses", 0))
        self.name = str(kwargs.get("Name", None))
        self.players = int(kwargs.get("Players", 0))
        self.rating = int(kwargs.get("Rating", 0))
        self.tag = str(kwargs.get("Tag", None))
        self.teamId = int(kwargs.get("TeamId", 0))
        self.wins = int(kwargs.get("Wins", 0))
class QueueStats(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.assists = int(kwargs.get("Assists", 0))
        try:
            self.godId = Gods(int(kwargs.get("GodId", 0))) or Champions(int(kwargs.get("ChampionId", 0)))
            self.godName = str(self.godId)
        except:
            self.godId = int(kwargs.get("ChampionId", 0)) or int(kwargs.get("GodId", 0))
            self.godName = str(kwargs.get("Champion", None)) or str(kwargs.get("God", None))
        self.deaths = int(kwargs.get("Deaths", 0))
        self.gold = int(kwargs.get("Gold", 0))
        self.kills = int(kwargs.get("Kills", 0))
        self.lastPlayed = str(kwargs.get("LastPlayed", None))
        if self.lastPlayed:
            self.lastPlayed = datetime.strptime(self.lastPlayed, "%m/%d/%Y %H:%M:%S %p")
        self.losses = int(kwargs.get("Losses", 0))
        self.matches = int(kwargs.get("Matches", 0))
        self.minutes = int(kwargs.get("Minutes", 0))
        self.queue = str(kwargs.get("Queue", None))
        self.wins = int(kwargs.get("Wins", 0))
        self.playerId = int(kwargs.get("player_id", 0))

class ChampionCard(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.activeFlagActivationSchedule = str(kwargs.get("active_flag_activation_schedule", None)).lower() == 'y'
        self.activeFlagLti = str(kwargs.get("active_flag_lti", None)).lower() == 'y'
        self.cardDescription = str(kwargs.get("card_description", None))
        self.cardId1 = int(kwargs.get("card_id1", 0))
        self.cardId2 = int(kwargs.get("card_id2", 0))
        self.cardName = str(kwargs.get("card_name", None))
        self.cardNameEnglish = str(kwargs.get("card_name_english", None))
        self.championCardURL =  str(kwargs.get("championCard_URL", None))
        self.championIconURL = str(kwargs.get("championIcon_URL", None))
        try:
            self.championId = Champions(int(kwargs.get("champion_id", 0)))
            self.championName = str(self.championId)
        except:
            self.championId = int(kwargs.get("champion_id", 0))
            self.championName = str(kwargs.get("champion_name", None))
        self.exclusive = str(kwargs.get("exclusive", None)).lower() == 'y'
        self.rank = int(kwargs.get("rank", 0))
        self.rarity = str(kwargs.get("rarity", None))
        self.recharge_seconds = int(kwargs.get("recharge_seconds", 0))
    def getIconURL(self):
        return "https://web2.hirez.com/paladins/champion-icons/{0}.jpg".format(self.championName)
    def getCardURL(self):
        return "https://web2.hirez.com/paladins/champion-cards/{0}.jpg".format(self.cardNameEnglish)
