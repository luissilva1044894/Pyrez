from .Queue import Queue
class QueueSmite(Queue):
    """For Smite, queue_id’s 426, 435, 440, 445, 448, 451, 459, & 450 are the only ones considered for player win/loss stats from /getplayer."""
    Conquest_5v5 = 423
    Novice_Queue = 424
    Conquest = 426
    Practice = 427
    Custom_Conquest = 429 #Conquest_Challenge=429#Conquest_Ranked=430
    Domination = 433
    MOTD = 434
    Arena_Queue = 435
    Basic_Tutorial = 436
    Custom_Arena = 438#Arena_Challenge = 438
    Domination_Challenge = 439
    Joust_1v1_Ranked_Keyboard = 440
    Custom_Joust = 441#Joust_Challenge = 441
    Arena_Practice_Easy = 443
    Jungle_Practice = 444
    Assault = 445
    Custom_Assault = 446#Assault_Challenge = 446
    Joust_Queue_3v3 = 448
    Joust_3v3_Ranked_Keyboard = 450
    Conquest_Ranked_Keyboard = 451 # ConquestLeague
    Arena_League = 452
    Assault_vs_AI_Medium = 454
    Joust_vs_AI_Medium = 456
    Arena_vs_AI_Easy = 457
    Conquest_Practice_Easy = 458
    Siege_4v4 = 459
    Custom_Siege = 460#Siege_Challenge = 460
    Conquest_vs_AI_Medium = 461
    Arena_Tutorial = 462
    Conquest_Tutorial = 463
    Joust_Practice_Easy = 464
    Clash = 466
    Custom_Clash = 467#Clash_Challenge = 467
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
    @property
    def isRanked(self):
        return self in [ QueueSmite.Joust_1v1_Ranked_Keyboard, QueueSmite.Joust_3v3_Ranked_Keyboard, QueueSmite.Conquest_Ranked_Keyboard, QueueSmite.Joust_1v1_Ranked_GamePad, QueueSmite.Joust_3v3_Ranked_GamePad, QueueSmite.Conquest_Ranked_GamePad ]
