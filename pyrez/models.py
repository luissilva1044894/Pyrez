from pyrez.enumerations import Tier
from datetime import datetime

class APIResponse:
    def __init__(self, **kwargs):
        self.retMsg = kwargs.get("ret_msg", None)
        self.json = str(kwargs)
    def __str__(self):
        return str(self.json)

class BaseAbility:#class Ability
    def __init__(self, **kwargs):
        self.id = int(kwargs.get("Id", 0))
        self.summary = kwargs.get("Summary", None)
        self.url = kwargs.get("URL", None)
    def __str__(self):
        return "ID: {0} Description: {1} Summary: {2} Url: {3}".format(self.id, self.description, self.summary, self.url)

class BaseCharacter(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = int(kwargs.get("id", 0))
        self.abilitys = []
        self.cons = kwargs.get("Cons", None)
        self.health = int(kwargs.get("Health", 0))
        self.lore = kwargs.get("Lore", None)
        self.name = kwargs.get("Name", None)
        self.onFreeRotation = kwargs.get("OnFreeRotation", None)
        self.pantheon = kwargs.get("Pantheon", None)
        self.pros = kwargs.get("Pros", None)
        self.roles = kwargs.get("Roles", None)
        self.speed = int(kwargs.get("Speed", 0))
        self.title = kwargs.get("Title", None)
        self.type = kwargs.get("Type", None)

class BaseCharacterRank(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.assists = kwargs.get("Assists")
        self.deaths = int(kwargs.get("Deaths", 0))
        self.kills = kwargs.get("Kills")
        self.losses = int(kwargs.get("Losses", 0))
        self.minionKills = int(kwargs.get("MinionKills", 0))
        self.godLevel = int(kwargs.get("Rank", 0))
        self.wins = int(kwargs.get("Wins", 0))
        self.worshippers = int(kwargs.get("Worshippers", 0))
        self.playerID = int(kwargs.get("player_id", 0))
    def getWinratio(self, decimals = 2):
        aux = self.wins + self.losses if self.wins + self.losses > 1 else 1
        winratio = self.wins / aux * 100.0
        return int(winratio) if winratio % 2 == 0 else round(winratio, decimals)

    def getKDA(self, decimals = 2):
        deaths = self.deaths if self.deaths > 1 else 1
        kda =((self.assists / 2) + self.kills) / deaths
        return int(kda) if kda % 2 == 0 else round(kda, decimals)# + "%";

class BaseItem(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.deviceName = int(kwargs.get("DeviceName", 0))
        self.iconId = int(kwargs.get("IconId"))
        self.itemId = int(kwargs.get("ItemId"))
        self.price = int(kwargs.get("Price"))
        self.shortDesc = str(kwargs.get("ShortDesc"))
        self.itemIcon_URL = str(kwargs.get("itemIcon_URL"))
    def __eq__(self, other):
        return self.ItemId == other.ItemId

class AbstractPlayer(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerId = int(kwargs.get("Id", 0)) or int(kwargs.get("id", 0))
        self.name = str(kwargs.get("Name")) or str(kwargs.get("name"))

class BasePlayer(AbstractPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.createdDatetime = kwargs.get("Created_Datetime") or kwargs.get("created_datetime")
        self.lastLoginDatetime = kwargs.get("Last_Login_Datetime") or kwargs.get("last_login_datetime")
        self.accountLevel = int(kwargs.get("Level", 0)) or int(kwargs.get("level", 0))
        self.playerName = kwargs.get("Name", None)
        self.playerRegion = kwargs.get("Region") or kwargs.get("region")
        
    def __str__(self):
        return str(self.json)

class BasePSPlayer(BasePlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.leaves = int(kwargs.get("Leaves", 0))
        self.losses = int(kwargs.get("Losses", 0))
        self.playedChampions = int(kwargs.get("MasteryLevel", 0))
        self.playerStatusMessage = kwargs.get("Personal_Status_Message")
        self.rankedConquest = BaseRanked(**kwargs.get("RankedConquest"))
        self.teamID = int(kwargs.get("TeamId"))
        self.teamName = kwargs.get("Team_Name")
        self.playerElo = int(kwargs.get("Tier_Conquest", 0))
        self.totalAchievements = int(kwargs.get("Total_Achievements", 0))
        self.totalworshippers = int(kwargs.get("Total_Worshippers", 0))
        self.wins = int(kwargs.get("Wins", 0))

    def getWinratio(self, decimals = 2):
        winratio = self.wins /((self.wins + self.losses) if self.wins + self.losses > 1 else 1) * 100.0
        return int(winratio) if winratio % 2 == 0 else round(winratio, decimals)

class BaseRanked(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.leaves = kwargs.get("Leaves")
        self.losses = int(kwargs.get("Losses", 0))
        self.rankedName = kwargs.get("Name")
        self.currentTrumpPoints = int(kwargs.get("Points", 0))
        self.prevRank = int(kwargs.get("PrevRank", 0))
        self.leaderboardIndex = int(kwargs.get("Rank", 0))
        self.rankStatConquest = kwargs.get("Rank_Stat_Conquest", None)
        self.rankStatDuel = kwargs.get("Rank_Stat_Duel", None)
        self.rankStatJoust = kwargs.get("Rank_Stat_Joust", None)
        self.currentSeason = int(kwargs.get("Season", 0))
        self.currentElo = Tier(int(kwargs.get("Tier", 0)))
        self.wins = int(kwargs.get("Wins", 0))
        self.playerID = kwargs.get("player_id", None)
    def getWinratio(self):
        winratio = self.wins /((self.wins + self.losses) if self.wins + self.losses > 1 else 1) * 100.0
        return int(winratio) if winratio % 2 == 0 else round(winratio, 2)

class Champion(BaseCharacter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 5):
            obj = ChampionAbility(**kwargs.get("Ability_" + str(i + 1)))
            self.abilitys.append(obj)
        self.championCardURL = kwargs.get("ChampionCard_URL", None)
        self.championIconURL = kwargs.get("ChampionIcon_URL", None)
        self.latestChampion = True if str(kwargs.get("latestChampion")).lower() == "y" else False
    def __str__(self):
        st = "Name: {0} ID: {1} Health: {1} Roles: {2} Title: {3}".format(self.name, self.id, self.health, self.roles, self.title)
        for i in range(0, len(self.abilitys)):
            st +=(" Ability {0}: {1}").format(i + 1, self.abilitys [i])
        st += "CardUrl: {0} IconUrl: {1} ".format(self.championCardURL, self.championIconURL)
        return st;

class ChampionAbility(BaseAbility):
    def __init__(self, **kwargs):
        self.description = kwargs.get("Description", None)
        return super().__init__(**kwargs)

class ChampionSkin(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.championId = int(kwargs.get("champion_id", 0))
        self.championName = str(kwargs.get("champion_name", None))
        self.rarity = str(kwargs.get("rarity", None))
        self.skinID1 = int(kwargs.get("skin_id1", 0))
        self.skinID2 = int(kwargs.get("skin_id2", 0))
        self.skinName = str(kwargs.get("skin_name", None))
        self.skinNameEnglish = str(kwargs.get("skin_name_english", None))
    
    def __eq__(self, other):
        return self.skinID1 == other.skinID1 and self.skinID2 == other.skinID2
    def __str__(self):
        return str(self.json)

class DataUsed(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.activeSessions = int(kwargs.get("Active_Sessions", 0)) or int(kwargs.get("active_Sessions", 0))
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
        self.id = int(kwargs.get("account_id"))
        self.playerID = int(kwargs.get("player_id"))
        self.avatarURL = kwargs.get("avatar_url")
        self.name = kwargs.get("name")
    def __str__(self):
        return "<Player {}>".format(self.id)
    #def __hash__(self):
        #return hash(self.id)
    def __eq__(self, other):
        return self.id == other.id

class God(BaseCharacter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.latestGod = True if str(kwargs.get("latestGod")).lower() == "y" else False

class GodRank(BaseCharacterRank):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.godName = str(kwargs.get("god")) if kwargs.get("champion") is None else str(kwargs.get("champion"))
        self.godID = Gods(int(kwargs.get("god_id"))) if kwargs.get("god_id") else Champions(int(kwargs.get("champion_id"))) if kwargs.get("champion_id") else -1
        
class HiRezServerStatus(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entryDateTime = kwargs.get("entry_datetime")
        self.status = True if str(kwargs.get("status", None).upper()) == "UP" else False
        self.version = kwargs.get("version")
    def __str__(self):
        return "entry_datetime: {0} status: {1} version: {2}".format(self.entryDateTime, "UP" if self.status else "DOWN", self.version)

class InGameItem:
    def __init__(self, itemID, itemName, itemLevel):
        self.itemID = itemID
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
        self.secondaryDescription = int(kwargs.get("SecondaryDescription"))

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
        self.championID = kwargs.get("ChampionId")
        self.championName = kwargs.get("Champion")
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
        self.matchQueueID = kwargs.get("Match_Queue_Id")
        self.matchTime = kwargs.get("Match_Time")
        self.matchTimeSecond = kwargs.get("Time_In_Match_Seconds")
        self.matchID = kwargs.get("Match")
        self.multiKillMax = kwargs.get("Multi_kill_Max")
        self.objectiveAssists = kwargs.get("Objective_Assists")
        self.queue = kwargs.get("Queue")
        self.skin = kwargs.get("Skin")
        self.skinID = kwargs.get("SkinId")
        self.surrendered = kwargs.get("Surrendered")
        self.taskForce = kwargs.get("TaskForce")
        self.team1Score = kwargs.get("Team1Score")
        self.team2Score = kwargs.get("Team2Score")
        self.wardsPlaced = kwargs.get("Wards_Placed")
        self.winStatus = kwargs.get("Win_Status")
        self.winningTaskForce = kwargs.get("Winning_TaskForce")
        self.playerName = kwargs.get("playerName")

class MatchPlayerDetails(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accountLevel = int(kwargs.get("Account_Level", 0))
        self.championId = Champions(int(kwargs.get("ChampionId", 0)))
        #self.championName = str(kwargs.get("ChampionName", None))
        self.masteryLevel = int(kwargs.get("Mastery_Level", 0))
        self.matchId = int(kwargs.get("Match", 0))
        self.queue = PaladinsQueue(int(kwargs.get("Queue", 0)))
        self.skinId = int(kwargs.get("SkinId", 0))
        self.playerCreated = kwargs.get("playerCreated", None)
        self.playerId = int(kwargs.get("playerId", 0))
        self.playerName = kwargs.get("playerName", None)
        self.taskForce = int(kwargs.get("taskForce", 0))
        self.tier = int(kwargs.get("Tier", 0))
        self.tierLosses = int(kwargs.get("tierLosses", 0))
        self.tierWins = int(kwargs.get("tierWins", 0))

class Menuitem:
    def __init__(self, **kwargs):
        self.description = int(kwargs.get("Description"))
        self.value = int(kwargs.get("Value"))

class PaladinsItem(BaseItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description = str(kwargs.get("Description"))
        self.champion_id = int(kwargs.get("champion_id"))
        self.item_type = str(kwargs.get("item_type"))
        self.talent_reward_level = int(kwargs.get("talent_reward_level"))

class PatchInfo(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gameVersion = str(kwargs.get("version_string", None))

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

class Player(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerId = kwargs.get("id")
        self.name = kwargs.get("name")
        self.steamID = kwargs.get("steam_id")

class PlayerLoadouts(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.championID = int(kwargs.get("ChampionId", 0))
        self.championName = str(kwargs.get("ChampionName", None))
        self.deckID = int(kwargs.get("DeckId", 0))
        self.deckName = str(kwargs.get("DeckName", None))
        self.playerID = int(kwargs.get("playerId", 0))
        self.playerName = str(kwargs.get("playerName", None))
        cards = kwargs.get("LoadoutItems")
        self.cards = []
        for i in cards:
            obj = LoadoutItem(**i)
            self.cards.append(obj)
    def __str__(self):
        return self.json

class PlayerRealmRoyale(BasePlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerId = kwargs.get("id")
        self.name = kwargs.get("name")
        self.steamID = kwargs.get("steam_id")
class PlayerSmite(BasePSPlayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.avatarURL = kwargs.get("Avatar_URL")
        self.rankStatConquest = kwargs.get("Rank_Stat_Conquest")
        self.rankStatDuel = kwargs.get("Rank_Stat_Duel")
        self.rankStatJoust = kwargs.get("Rank_Stat_Joust")
        self.rankedDuel = BaseRanked(**kwargs.get("RankedDuel"))
        self.rankedJoust = BaseRanked(**kwargs.get("RankedJoust"))
        self.tierJoust = kwargs.get("Tier_Joust")
        self.tierDuel = kwargs.get("Tier_Duel")

class PlayerStatus(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currentMatchID = int(kwargs.get("match_id", 0)) or int(kwargs.get("Match", 0))
        self.currentMatchQueueID = int(kwargs.get("match_queue_id", 0))
        self.playerStatus = int(kwargs.get("status_id", 0)) or kwargs.get("status", 0)
        self.playerStatusString = str(kwargs.get("status_string", None)) or str(kwargs.get("status", None))
        self.playerStatusMessage = str(kwargs.get("personal_status_message", None))

class Session(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sessionId = str(kwargs.get("session_id", 0))
        self.timeStamp = datetime.strptime(str(kwargs.get("timestamp", 0)), "%m/%d/%Y %H:%M:%S %p")
    def isApproved(self):
        return str(self.json).lower().find("approved") != -1
class SmiteItem(BaseItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.childItemId = int(kwargs.get("ChildItemId"))
        self.itemDescription = ItemDescription(**kwargs.get("ItemDescription"))
        self.itemTier = str(kwargs.get("ItemTier"))
        self.rootItemId = int(kwargs.get("RootItemId"))
        self.startingItem = str(kwargs.get("StartingItem"))
        self.type = str(kwargs.get("Type"))

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
