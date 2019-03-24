from enum import Enum, IntFlag

class BaseEnum(Enum):
    def __str__(self):
        return str(self.value) # return str(self.name)

class HiRezServerFeedsFormat(BaseEnum):
    ATOM = "atom"
    RSS = "rss"
    JSON = "json"

class ResponseFormat(BaseEnum):
    JSON = "json"
    XML = "xml"

class LanguageCode(IntFlag): # LanguageCode(5) == LanguageCode lang =(LanguageCode) 5;
    English = 1
    German = 2
    French = 3
    Chinese = 5
    Spanish = 7
    Spanish_Latin_America = 9
    Portuguese = 10
    Russian = 11
    Polish = 12
    Turkish = 13

class PaladinsLinks(BaseEnum):
    PALADINS_CRYSTAL_IMAGES = "https://app.box.com/s/orqsgij1kfyyo3co5gsg6k27ai9wab5d"
    PALADINS_MAPS_IMAGES = "https://app.box.com/s/rji72ijexal3mzl0mwfj3gimdoj5ii1i"
    PALADINS_WALLPAPERS = "https://app.box.com/s/xshio67sqe7wxrse4tipaw3e3oipffnd"
    PALADINS_CHAMPIONS_SKINS = "https://app.box.com/s/qzi4jn7gu0upjspab78i6pn3fsw0vvrf"
    
class Endpoint(BaseEnum):
    """
    The endpoint that you want to access to retrieve information from the Hi-Rez Studios' API.
    """
    PALADINS = "http://api.paladins.com/paladinsapi.svc"
    REALM_ROYALE = "http://api.realmroyale.com/realmapi.svc"
    SMITE = "http://api.smitegame.com/smiteapi.svc"
    
    HAND_OF_THE_GODS = "http://api.handofthegods.com/handofthegodsapi.svc"
    PALADINS_STRIKE = "http://api.paladinsstrike.com/paladinsstrike.svc"
    
class Platform(BaseEnum):
    MOBILE = "MOBILE"
    NINTENDO_SWITCH = "Nintendo"
    PC = "HiRez"
    PS4 = "PSN"
    XBOX = "XboxLive"
    STEAM = "Steam"
    #UNKNOWN = "unknown" #XBOX = "xbox" #SWITCH = "switch"
    
class Classes(BaseEnum):
    Warrior = 2285
    Hunter = 2493
    Mage = 2494
    Engineer = 2495
    Assassin = 2496

class AvatarPaladins(Enum):
    Default = 0
    Origin = 9918
    Terminating = 23226
    The_Lost_Hand = 23549
    Oni_Mask = 23550
    Cutesy_Maeve = 23552
    Cutesy_Snek = 23553
    Cutest_Zhin = 23554
    Goodnight = 23555
    Shadowblade = 23564
    Flametongue = 23661
    Snack_Time = 23662
    Death_Speaker = 23714
    Knightmare = 23715
    Day_Walker = 23716
    Harbinger = 23717
    Synth = 23924
    Nom_Nom = 23925
    Cutesy_Yeti = 24079
    Cutesy_Lian = 24080
    Rowdy_Corsair = 24081
    Winter_Workout = 24088
    Shield_Bearer = 24143
    Paladins_Defense_Force = 24202
    Imperial_Magistrate = 24203
    Fire_and_Ice = 24204
    Queen_of_Hearts = 24350
    def getId(self):
        return int(self.value)
    def __str__(self):
        return str(self.name.replace('_', ' '))

class Champions(Enum):
    Androxus = 2205
    Ash = 2404
    Barik = 2073
    Bomb_King = 2281
    Buck = 2147
    Cassie = 2092
    Dredge = 2495
    Drogoz = 2277
    Evie = 2094
    Fernando = 2071
    Furia = 2491
    Grohk = 2093
    Grover = 2254
    Imani = 2509
    Inara = 2348
    Jenos = 2431
    Khan = 2479
    Kinessa = 2249
    Koga = 2493
    Lex = 2362
    Lian = 2417
    Maeve = 2338
    Makoa = 2288
    Mal_Damba = 2303
    Moji = 2481
    Pip = 2056
    Ruckus = 2149
    Seris = 2372
    Sha_Lin = 2307
    Skye = 2057
    Strix = 2438
    Talus = 2472
    Terminus = 2477
    Torvald = 2322
    Tyra = 2314
    Viktor = 2285
    Vivian = 2480
    Willo = 2393
    Ying = 2267
    Zhin = 2420
    def getId(self):
        return int(self.value)
    def getIcon(self):
        return "https://web2.hirez.com/paladins/champion-icons/{0}.jpg".format(self.name.lower().replace('_', '-'))
    def __str__(self):
        return str(self.name.replace("_", " "))

class Gods(Enum):
    Achilles = 3492
    Agni = 1737
    Ah_Muzen_Cab = 1956
    Ah_Puch = 2056
    Amaterasu = 2110
    Anhur = 1773
    Anubis = 1668
    Ao_Kuang = 2034
    Aphrodite = 1898
    Apollo = 1899
    Arachne = 1699
    Ares = 1782
    Artemis = 1748
    Artio = 3336
    Athena = 1919
    Awilix = 2037
    Bacchus = 1809
    Bakasura = 1755
    Baron_Samedi = 3518
    Bastet = 1678
    Bellona = 2047
    Cabrakan = 2008
    Camazotz = 2189
    Cerberus = 3419
    Cernunnos = 2268
    Chaac = 1966
    Change = 1921 # Chang'e
    Chernobog = 3509
    Chiron = 2075
    Chronos = 1920
    Cu_Chulainn = 2319
    Cupid = 1778
    Da_Ji = 2270
    Discordia = 3377
    Erlang_Shen = 2138
    Fafnir = 2136
    Fenrir = 1843
    Freya = 1784
    Ganesha = 2269
    Geb = 1978
    Guan_Yu = 1763
    Hachiman = 3344
    Hades = 1676
    He_Bo = 1674
    Hel = 1718
    Hera = 3558
    Hercules = 1848
    Hou_Yi = 2040
    Hun_Batz = 1673
    Isis = 1918
    Izanami = 2179
    Janus = 1999
    Jing_Wei = 2122
    Kali = 1649
    Khepri = 2066
    King_Arthur = 3565
    Kukulkan = 1677
    Kumbhakarna = 1993
    Kuzenbo = 2260
    Loki = 1797
    Medusa = 2051
    Merlin = 3566
    Mercury = 1941
    Ne_Zha = 1915
    Neith = 1872
    Nemesis = 1980
    Nike = 2214
    Nox = 2036
    Nu_Wa = 1958
    Odin = 1669
    Osiris = 2000
    Pele = 3543
    Poseidon = 1881
    Ra = 1698
    Raijin = 2113
    Rama = 2002
    Ratatoskr = 2063
    Ravana = 2065
    Scylla = 1988
    Serqet = 2005
    Skadi = 2107
    Sobek = 1747
    Sol = 2074
    Sun_Wukong = 1944
    Susano = 2123
    Sylvanus = 2030
    Terra = 2147
    Thanatos = 1943
    The_Morrigan = 2226
    Thor = 1779
    Thoth = 2203
    Tyr = 1924
    Ullr = 1991
    Vamana = 1723
    Vulcan = 1869
    Xbalanque = 1864
    Xing_Tian = 2072
    Ymir = 1670
    Zeus = 1672
    Zhong_Kui = 1926
    def getId(self):
        return int(self.value)
    def getCard(self):
        return "https://web2.hirez.com/smite/god-cards/{0}.jpg".format(self.name.lower().replace('_', '-'))
    def getIcon(self):
        return "https://web2.hirez.com/smite/god-icons/{0}.jpg".format(self.name.lower().replace('_', '-'))
    def __str__(self):
        return str(self.name.replace('_', ' '))

class ItemType(IntFlag):
    Unknown = 0
    Defense = 1
    Utility = 2
    Healing = 3
    Damage = 4

class PortalId(IntFlag):
    PortalNotYetSupported = -1
    HiRez = 1
    Steam = 5
    PS4 = 9
    Xbox = 10
    Switch = 22
    Discord = 25

class PlatformType(IntFlag):
    Windows = 1
    Mac = 2
    Xbox_Nintendo = 3
    PSN = 4
    #9: ????? #10: ?????

class InputType(IntFlag):
    KeyboardMouse = 1
    Controller = 2

class Status(Enum):
    Offline = 0
    In_Lobby = 1
    God_Selection = 2
    In_Game = 3
    Online = 4
    Not_Found = 5
    def __str__(self):
        return str(self.name.replace("_", " "))
class Tier(Enum):
    Unranked = 0 # Qualifying
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
    def __str__(self):
        return str(self.name.replace("_", " "))

class RealmRoyaleQueue(BaseEnum):
    Live_Solo = 474
    Live_Duo = 475
    Live_Squad = 476
    Live_Wars = 477
    Live_Tutorial = 478
    Live_Solo_Mid_Level = 479
    Live_Solo_Low_Level = 480
    Live_Squad_Mid_Level = 481
    Live_Squad_Low_Level = 482
    Live_Duo_Mid_Level = 483
    Live_Duo_Low_Level = 484
    #Challenge_Solo = 10188
    #Challenge_Duo = 10189
    #Challenge_Squad = 10190
    #Storm = 10192
    #Solo_With_Bots = 10193
    #Deathmatch = 10194
    #Tutorial = 10195
class SmiteQueue(BaseEnum):
    """
    For Smite, queue_id’s 426, 435, 440, 445, 448, 451, 459, & 450 are the only ones considered for player win/loss stats from /getplayer.
    """
    Conquest_5v5 = 423
    Novice_Queue = 424
    Conquest = 426
    Practice = 427
    Conquest_Challenge = 429 #Conquest_Ranked = 430
    Domination = 433
    MOTD = 434
    Arena_Queue = 435
    Basic_Tutorial = 436
    Arena_Challenge = 438
    Domination_Challenge = 439
    Joust_1v1_Ranked_Keyboard = 440
    Joust_Challenge = 441
    Arena_Practice_Easy = 443
    Jungle_Practice = 444
    Assault = 445
    Assault_Challenge = 446
    Joust_Queue_3v3 = 448
    Joust_3v3_Ranked_Keyboard = 450
    Conquest_Ranked_Keyboard = 451 # ConquestLeague
    Arena_League = 452
    Assault_vs_AI_Medium = 454
    Joust_vs_AI_Medium = 456
    Arena_vs_AI_Easy = 457
    Conquest_Practice_Easy = 458
    Siege_4v4 = 459
    Siege_Challenge = 460
    Conquest_vs_AI_Medium = 461
    Arena_Tutorial = 462
    Conquest_Tutorial = 463
    Joust_Practice_Easy = 464
    Clash = 466
    Clash_Challenge = 467
    Arena_vs_AI_Medium = 468
    Clash_vs_AI_Medium = 469
    Clash_Practice_Easy = 470
    Clash_Tutorial = 471
    Arena_Practice_Medium = 472
    Joust_Practice_Medium = 473
    Joust_vs_AI_Easy = 474
    Conquest_Practice_Medium = 475
    Conquest_vs_AI_Easy = 476
    Clash_Practice_Medium = 477
    Clash_vs_AI_Easy = 478
    Assault_Practice_Easy = 479
    Assault_Practice_Medium = 480
    Assault_vs_AI_Easy = 481
    Joust_3v3_Training = 482
    Arena_Training = 483
    Adventure_Horde = 495
    Jungle_Practice_Presele_ = 496
    Adventure_Joust = 499
    Adventure_CH10 = 500
    Loki_Dungeon = 501
    Joust_1v1_Ranked_GamePad = 502
    Joust_3v3_Ranked_GamePad = 503
    Conquest_Ranked_GamePad = 504
    def isRanked(self):
        return self.value == SmiteQueue.Joust_1v1_Ranked_Keyboard.value or self.value == SmiteQueue.Joust_3v3_Ranked_Keyboard.value or self.value == SmiteQueue.Conquest_Ranked_Keyboard.value or self.value == SmiteQueue.Joust_1v1_Ranked_GamePad.value or self.value == SmiteQueue.Joust_3v3_Ranked_GamePad.value or self.value == SmiteQueue.Conquest_Ranked_GamePad.value
    def __str__(self):
        return str(self.name.replace("_", " "))

class PaladinsQueue(BaseEnum):
    Custom_Siege_Stone_Keep = 423
    Live_Siege= 424
    Live_Pratice_Siege = 425
    Challenge_Match = 426
    Practice = 427
    Live_Competitive_GamePad = 428 #ControllerRankedQueue (GamePad)
    zzRETIRED = 429
    Custom_Siege_Timber_Mill = 430
    Custom_Siege_Fish_Market = 431
    Custom_Siege_Frozen_Guard = 432
    Custom_Siege_Frog_Isle = 433
    Shooting_Range = 434
    Perf_Capture_Map = 435
    Tencent_Alpha_Test_Queue_Coop = 436
    Payload = 437
    Custom_Siege_Jaguar_Falls = 438
    Custom_Siege_Ice_Mines = 439
    Custom_Siege_Serpeant_Beach = 440
    Challenge_TP = 441
    Challenge_FP = 442
    Challenge_IP = 443
    Tutorial = 444
    Live_Test_Maps = 445
    PvE_Hands_That_Bind = 446
    WIPPvE_Los_Pollos_Fernandos = 447
    WIPPvE_High_Rollers = 448
    PvE_HnS = 449
    WIPPvE_Leap_Frogs = 450
    PvE_Survival = 451
    Live_Onslaught = 452
    Live_Pratice_Onslaught = 453
    Custom_Onslaught_Snowfall_Junction = 454
    Custom_Onslaught_Primal_Court = 455
    Custom_Siege_Brightmarsh = 458
    Custom_Siege_Splitstone_Quarry = 459
    Custom_Onslaught_Foreman_Rise = 462
    Custom_Onslaught_Magistrate_Archives = 464
    Classic_Siege = 465
    Custom_Team_Deathmatch_Trade_District = 468
    Live_Team_DeathMatch = 469
    Live_Pratice_Team_Deathmatch = 470
    Custom_Team_Deathmatch_Foreman_Rise = 471
    Custom_Team_Deathmatch_Magistrates_Archives = 472
    Custom_Siege_Ascension_Peak = 473
    Live_Battlegrounds_Solo = 474
    Live_Battlegrounds_Duo = 475
    Live_Battlegrounds_Quad = 476
    Live_Event_Ascension_Peak = 477 # LIVE HH(Event)
    Live_Event_Rise_Of_Furia = 478 # LIVE HH(Event)
    Custom_Team_Deathmatch_Abyss = 479
    Custom_Team_Deathmatch_Throne = 480
    Custom_Onslaught_Marauders_Port = 483
    Custom_Team_Deathmatch_Dragon_Arena = 484
    Custom_Siege_Warders_Gate = 485
    Live_Competitive_Keyboard = 486 #KeyboardRankedQueue (KBM)
    Custom_Siege_Shattered_Desert = 487
    Live_Event_End_Times = 488
    Custom_Event_End_Times = 489
    Multi_Queue = 999
    def isRanked(self):
        return self.value == PaladinsQueue.Live_Competitive_Keyboard.value or self.value == PaladinsQueue.Live_Competitive_GamePad.value
    def __str__(self):
        return str(self.name.replace("_", " "))
