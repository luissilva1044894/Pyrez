from enum import Enum

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
    def getIconUrl(self):
        return "https://web2.hirez.com/paladins/champion-icons/{0}.jpg".format(self.name.lower().replace('_', '-'))
    def __str__(self):
        return str(self.name.replace("_", " "))
