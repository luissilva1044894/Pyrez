from enum import Enum, IntFlag

class BaseEnum(Enum):
    def __str__(self):
        return str(self.value) # return str(self.name)

class ResponseFormat(BaseEnum):
    JSON = "json"
    XML = "xml"

class LanguageCode(IntFlag): # LanguageCode(5) == LanguageCode lang =(LanguageCode) 5;
    Chinese = 5
    English = 1
    French = 3
    German = 2
    Polish = 12
    Portuguese = 10
    Russian = 11
    Spanish = 7
    Spanish_Latin_America = 9
    Turkish = 13

class Endpoint(BaseEnum):
    HAND_OF_THE_GODS_PC = "http://api.handofthegods.com/handofthegodsapi.svc"
    PALADINS_PC = "http://api.paladins.com/paladinsapi.svc"
    PALADINS_PS4 = "http://api.ps4.paladins.com/paladinsapi.svc"
    PALADINS_XBOX = "http://api.xbox.paladins.com/paladinsapi.svc"
    PALADINS_STRIKE_MOBILE = "http://api.paladinsstrike.com/paladinsstrike.svc"
    REALM_ROYALE_PC = "http://api.realmroyale.com/realmapi.svc"
    REALM_ROYALE_PS4 = "http://api.ps4.realmroyale.com/realmapi.svc"
    REALM_ROYALE_XBOX = "http://api.xbox.realmroyale.com/realmapi.svc"
    SMITE_PC = "http://api.smitegame.com/smiteapi.svc"
    SMITE_PS4 = "http://api.ps4.smitegame.com/smiteapi.svc"
    SMITE_XBOX = "http://api.xbox.smitegame.com/smiteapi.svc"

class Platform(BaseEnum):
    MOBILE = "MOBILE"
    NINTENDO_SWITCH = "SWITCH"
    PC = "PC"
    PS4 = "PS4"
    XBOX = "XBOX"

class Classes(BaseEnum):
    Assassin = 2496
    Engineer = 2495
    Hunter = 2493
    Mage = 2494
    Warrior = 2285

class Champions(Enum):
    Androxus = 2205
    Ash = 2404
    Barik = 2073
    Bomb_King = 2281
    Buck = 2147
    Cassie = 2092
    Drogoz = 2277
    Evie = 2094
    Fernando = 2071
    Furia = 2491
    Grohk = 2093
    Grover = 2254
    Inara = 2348
    Jenos = 2431
    Khan = 2479
    Kinessa = 2249
    Koga = 2493
    Lex = 2362
    Lian = 2417
    Maeve = 2338
    Makoa = 2288
    MalDamba = 2303
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
    def getIconUrl(self):
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
    Hercules = 1848
    Hou_Yi = 2040
    Hun_Batz = 1673
    Isis = 1918
    Izanami = 2179
    Janus = 1999
    Jing_Wei = 2122
    Kali = 1649
    Khepri = 2066
    Kukulkan = 1677
    Kumbhakarna = 1993
    Kuzenbo = 2260
    Loki = 1797
    Medusa = 2051
    Mercury = 1941
    Ne_Zha = 1915
    Neith = 1872
    Nemesis = 1980
    Nike = 2214
    Nox = 2036
    Nu_Wa = 1958
    Odin = 1669
    Osiris = 2000
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
    def getCardUrl(self):
        return "https://web2.hirez.com/smite/god-cards/{0}.jpg".format(self.name.lower().replace('_', '-'))
    def getIconUrl(self):
        return "https://web2.hirez.com/smite/god-icons/{0}.jpg".format(self.name.lower().replace('_', '-'))
    def __str__(self):
        return str(self.name.replace('_', ' '))

class ItemType(IntFlag):
    Unknown = 0
    Defense = 1
    Utility = 2
    Healing = 3
    Damage = 4

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
    Duo = 475
    Solo = 474
    Squad = 476
class SmiteQueue(BaseEnum):
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
    ConquestRanked = 451 # ConquestLeague
    ArenaLeague = 452
    Clash = 466
    Adventure_Horde = 495

class PaladinsQueue(BaseEnum):
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
    Ascension_Peak = 477 # LIVE HH(Event)
    Rise_Of_Furia = 478 # LIVE HH(Event)

    Multi_Queue = 999
