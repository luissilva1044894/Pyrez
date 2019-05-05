from .Enum import Enum
class Tier(Enum):
    # Tier.Bronze_V.getId() / 5 >> Div by 5 = Current rank: <= 0.0: Unranked, > 0.0 && <= 1.0: Bronze, > 1.0 && <= 2.0: Silver, > 2.0 && <= 3.0: Gold, > 3.0 && <= 4.0: Platinum, > 4.0 && <= 5.0: Diamond, > 5.0 && <= 5.2: Master, > 5.2: Grandmaster
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
