from .Enum import Enum
class Champions(Enum):
    """Represents a Paladins Champion. This is a sub-class of :class:`.Enum`.

    Supported Operations:

    +-----------+-------------------------------------------------+
    | Operation |                 Description                     |
    +===========+=================================================+
    | x == y    | Checks if two Champions are equal.              |
    +-----------+-------------------------------------------------+
    | x != y    | Checks if two Champions are not equal.          |
    +-----------+-------------------------------------------------+
    | hash(x)   | Return the Champion's hash.                     |
    +-----------+-------------------------------------------------+
    | str(x)    | Returns the Champion's name with discriminator. |
    +-----------+-------------------------------------------------+
    | int(x)    | Return the Champion's value as int.             |
    +-----------+-------------------------------------------------+
    """
    Androxus = 2205
    Ash = 2404
    Atlas = 2512
    Barik = 2073
    Bomb_King = 2281
    Buck = 2147
    Cassie = 2092
    Corvus = 2533
    Dredge = 2495
    Drogoz = 2277
    Evie = 2094
    Fernando = 2071
    Furia = 2491
    Grohk = 2093
    Grover = 2254
    Imani = 2509
    Inara = 2348
    Io = 2517
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
    Raum = 2528
    Ruckus = 2149
    Seris = 2372
    Sha_Lin = 2307
    Skye = 2057
    Strix = 2438
    Talus = 2472
    Terminus = 2477
    Tiberius = 2529
    Torvald = 2322
    Tyra = 2314
    Viktor = 2285
    Vivian = 2480
    Vora = 2536
    Willo = 2393
    Yagorath = 2538
    Ying = 2267
    Zhin = 2420
    @property
    def getHeader(self):
        return "https://web2.hirez.com/paladins/champion-headers/{}.png".format(self.getName().lower().replace(' ', '-')) #.replace(' ', '')
    @property
    def getIcon(self):
        return "https://web2.hirez.com/paladins/champion-icons/{}.jpg".format(self.getName().lower().replace(' ', '-'))
    @property
    def isDamage(self):
        return self in [Champions.Bomb_King, Champions.Cassie, Champions.Dredge, Champions.Drogoz, Champions.Imani, Champions.Kinessa, Champions.Lian, Champions.Sha_Lin, Champions.Strix, Champions.Tiberius, Champions.Tyra, Champions.Viktor, Champions.Vivian, Champions.Willo]
    @property
    def isFlank(self):
        return self in [Champions.Androxus, Champions.Buck, Champions.Evie, Champions.Koga, Champions.Lex, Champions.Maeve, Champions.Moji, Champions.Skye, Champions.Talus, Champions.Zhin]
    @property
    def isFrontline(self):
        return self in [Champions.Ash, Champions.Atlas, Champions.Barik, Champions.Fernando, Champions.Inara, Champions.Khan, Champions.Makoa, Champions.Raum, Champions.Ruckus, Champions.Terminus, Champions.Torvald]
    @property
    def isSupport(self):
        return self in [Champions.Corvus, Champions.Furia, Champions.Grohk, Champions.Grover, Champions.Io, Champions.Jenos, Champions.Mal_Damba, Champions.Pip, Champions.Seris, Champions.Ying]
