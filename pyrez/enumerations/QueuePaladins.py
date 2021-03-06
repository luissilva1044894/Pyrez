from .Queue import Queue
class QueuePaladins(Queue):
    Custom_Siege_Stone_Keep = 423
    Live_Siege= 424
    Live_Pratice_Siege = 425
    Custom_Siege_Bazaar = 426#Challenge_Match
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
    @property
    def isLiveMatch(self):
        return self in [ QueuePaladins.Live_Siege, QueuePaladins.Live_Onslaught, QueuePaladins.Live_Team_DeathMatch, QueuePaladins.Live_Competitive_GamePad, QueuePaladins.Live_Competitive_Keyboard ]
    @property
    def isPraticeMatch(self):
        return self in [ QueuePaladins.Live_Pratice_Siege, QueuePaladins.Practice, QueuePaladins.Live_Pratice_Onslaught, QueuePaladins.Live_Pratice_Team_Deathmatch ]
    @property
    def isRanked(self):
        return self in [ QueuePaladins.Live_Competitive_Keyboard, QueuePaladins.Live_Competitive_GamePad ]
