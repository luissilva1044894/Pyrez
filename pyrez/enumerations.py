from enum import Enum, IntFlag

class BaseEnum (Enum):
    def __str__ (self):
        return str (self.value)

class ResponseFormat (BaseEnum):
    JSON = "json"
    XML = "xml"

class LanguageCode (IntFlag):
    CHINESE = 5
    ENGLISH = 1
    FRENCH = 3
    GERMAN = 2
    POLISH = 12
    PORTUGUESE = 10
    RUSSIAN = 11
    SPANISH = 7
    SPANISH_LATIN_AMERICA = 9
    TURKISH = 13

    def isRight (self):
        return self.value == 5 or self.value == 1 or self.value == 3 or self.value == 2 or self.value == 12 or self.value == 10 or self.value == 11 or self.value == 7 or self.value == 9 or self.value == 13

class Endpoint (BaseEnum):
    PALADINS_PC = "http://api.paladins.com/paladinsapi.svc"
    PALADINS_PS4 = "http://api.ps4.paladins.com/paladinsapi.svc"
    PALADINS_XBOX = "http://api.xbox.paladins.com/paladinsapi.svc"
    REALM_ROYALE_PC = "http://api.realmroyale.com/realmapi.svc"
    REALM_ROYALE_PS4 = "http://api.ps4.realmroyale.com/realmapi.svc"
    REALM_ROYALE_XBOX = "http://api.xbox.realmroyale.com/realmapi.svc"
    SMITE_PC = "http://api.smitegame.com/smiteapi.svc"
    SMITE_PS4 = "http://api.ps4.smitegame.com/smiteapi.svc"
    SMITE_XBOX = "http://api.xbox.smitegame.com/smiteapi.svc"

class Platform (BaseEnum):
    PC = "PC"
    PS4 = "PS4"
    XBOX = "XBOX"

class Classes (BaseEnum):
    ASSASSIN = 2496
    ENGINEER = 2495
    HUNTER = 2493
    MAGE = 2494
    WARRIOR = 2285

class Champions (BaseEnum):
    ANDROXUS = 2205
    ASH = 2404
    BARIK = 2073
    BOMB_KING = 2281
    BUCK = 2147
    CASSIE = 2092
    DROGOZ = 2277
    EVIE = 2094
    FERNANDO = 2071
    GROHK = 2093
    GROVER = 2254
    INARA = 2348
    JENOS = 2431
    KHAN = 2479
    KINESSA = 2249
    LEX = 2362
    LIAN = 2417
    MAEVE = 2338
    MAKOA = 2288
    MAL_DAMBA = 2303
    MOJI = 2481
    PIP = 2056
    RUCKUS = 2149
    SERIS = 2372
    SHA_LIN = 2307
    SKYE = 2057
    STRIX = 2438
    TALUS = 2472
    TERMINUS = 2477
    TORVALD = 2322
    TYRA = 2314
    VIKTOR = 2285
    VIVIAN = 2480
    WILLO = 2393
    YING = 2267
    ZHIN = 2420

    def __str__ (self):
        return str (self.name.replace ("_", " "))
class ItemType (BaseEnum):
    Unknown = 0
    Defense = 1
    Utility = 2
    Healing = 3
    Damage = 4

class Status (BaseEnum):
    Offline = 0
    In_Lobby = 1
    God_Selection = 2
    In_Game = 3
    Online = 4
    Not_Found = 5

class Tier (BaseEnum):
    #Qualifying
    Unranked = 0
    #BRONZE_V = 1
    Bronze_V = 1
    Bronze_IV = 2
    Bronze_III = 3
    Bronze_II = 4
    Bronze_I = 5
    Silver_V = 6
    Silver_IV = 7
    Silver_III = 8
    Silver_II = 9
    Silver_I = 10
    Gold_V = 11
    Gold_IV = 12
    Gold_III = 13
    Gold_II = 14
    Gold_I = 15
    Platinum_V = 16
    Platinum_IV = 17
    Platinum_III = 18
    Platinum_II = 19
    Platinum_I = 20
    Diamond_V = 21
    Diamond_IV = 22
    Diamond_III = 23
    Diamond_II = 24
    Diamond_I = 25
    Master = 26
    Grandmaster = 27

    def __str__ (self):
        return str (self.name.replace ("_", " "))

class RealmRoyaleQueue (BaseEnum):
    DUO = 475
    SOLO = 474
    SQUAD = 476
class SmiteQueue (BaseEnum):
    Conquest5v5 = 423
    NoviceQueue = 424
    Conquest = 426
    Practice = 427
    ConquestChallenge = 429
    #ConquestRanked = 430
    Domination = 433
    MOTD = 434
    ArenaQueue = 435
    ArenaChallenge = 438
    DominationChallenge = 439
    JoustLeague = 440
    JoustChallenge = 441
    Assault = 445
    AssaultChallenge = 446
    JoustQueue_3v3 = 448
    ConquestRanked = 451#ConquestLeague
    ArenaLeague = 452
    Clash = 466
    Adventure_Horde = 495

class PaladinsQueue (BaseEnum):
    Custom_Siege_StoneKeep = 423
    Live_Casual = 424
    Live_Pratice_Siege = 425
    ChallengeMatch = 426
    Practice = 427
    Live_Competitive = 428
    zzRETIRED = 429
    Custom_Siege_TimberMill = 430
    Custom_Siege_FishMarket = 431
    Custom_Siege_FrozenGuard = 432
    Custom_Siege_FrogIsle = 433
    ShootingRange = 434
    PerfCaptureMap = 435
    TencentAlphaTestQueueCoop = 436
    Payload = 437
    Custom_Siege_JaguarFalls = 438
    Custom_Siege_IceMines = 439
    Custom_Siege_SerpeantBeach = 440
    Challenge_TP = 441
    Challenge_FP = 442
    Challenge_IP = 443
    Tutorial = 444
    Live_TestMaps = 445
    PvE_HandsThatBind = 446
    WIPPvE_LosPollosFernandos = 447
    WIPPvE_HighRollers = 448
    PvE_HnS = 449
    WIPPvE_LeapFrogs = 450
    PvE_Survival = 451
    Live_Onslaught = 452
    Live_Onslaught_Pratice = 453
    Custom_Onslaught_SnowfallJunction = 454
    Custom_Onslaught_PrimalCourt = 455
    Custom_Siege_Brightmarsh = 458
    Custom_Siege_SplitstoneQuarry = 459
    Custom_Onslaught_ForemanRise = 462
    Custom_Onslaught_MagistrateArchives = 464
    ClassicSiege = 465
    Custom_TeamDeathmatch_TradeDistrict = 468
    Live_TeamDeathMatch = 469
    Live_TeamDeathmatch_Pratice = 470
    Custom_TeamDeathmatch_ForemanRise = 471
    Custom_TeamDeathmatch_MagistrateArchives = 472
    Live_Battlegrounds_Solo = 474
    Live_Battlegrounds_Duo = 475
    Live_Battlegrounds_Quad = 476
    Ascension_Peak = 477 # LIVE HH (Event)
    Rise_Of_Furia = 478 # LIVE HH (Event)

    Multi_Queue = 999
