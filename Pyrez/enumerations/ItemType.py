from enum import IntFlag

class ItemType(IntFlag):
    Unknown = 0
    Defense = 1
    Utility = 2
    Healing = 3
    Damage = 4
