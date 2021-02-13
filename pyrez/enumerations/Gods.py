from .Enum import Enum
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
    Baba_Yaga = 3925
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
    Cthulhu = 3945
    Cu_Chulainn = 2319
    Cupid = 1778
    Da_Ji = 2270
    Danzaburou = 3984
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
    Heimdallr = 3812
    Hel = 1718
    Hera = 3558
    Hercules = 1848
    Horus = 3611
    Hou_Yi = 2040
    Hun_Batz = 1673
    Isis = 1918
    Izanami = 2179
    Janus = 1999
    Jing_Wei = 2122
    Jormungandr = 3585
    Kali = 1649
    Khepri = 2066
    King_Arthur = 3565
    Kukulkan = 1677
    Kumbhakarna = 1993
    Kuzenbo = 2260
    Loki = 1797
    Medusa = 2051
    Mercury = 1941
    Merlin = 3566
    Mulan = 3881
    Ne_Zha = 1915
    Neith = 1872
    Nemesis = 1980
    Nike = 2214
    Nox = 2036
    Nu_Wa = 1958
    Odin = 1669
    Olorun = 3664
    Osiris = 2000
    Pele = 3543
    Persephone = 3705
    Poseidon = 1881
    Ra = 1698
    Raijin = 2113
    Rama = 2002
    Ratatoskr = 2063
    Ravana = 2065
    Scylla = 1988
    Serqet = 2005
    Set = 3612
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
    Tsukuyomi = 3954
    Tyr = 1924
    Ullr = 1991
    Vamana = 1723
    Vulcan = 1869
    Xbalanque = 1864
    Xing_Tian = 2072
    Yemoja = 3811
    Ymir = 1670
    Zeus = 1672
    Zhong_Kui = 1926
    @property
    def isWarrior(self):
        return self in [ Gods.Achilles, Gods.Amaterasu, Gods.Bellona, Gods.Chaac, Gods.Cu_Chulainn, Gods.Erlang_Shen, Gods.Guan_Yu, Gods.Hercules, Gods.Horus, Gods.King_Arthur, Gods.Mulan, Gods.Nike, Gods.Odin, Gods.Osiris, Gods.Sun_Wukong, Gods.Tyr, Gods.Vamana ]
    @property
    def isMage(self):
        return self in [ Gods.Agni, Gods.Ah_Puch, Gods.Anubis, Gods.Ao_Kuang, Gods.Aphrodite, Gods.Baba_Yaga, Gods.Baron_Samedi, Gods.Change, Gods.Chronos, Gods.Discordia, Gods.Freya, Gods.Hades, Gods.He_Bo, Gods.Hel, Gods.Hera, Gods.Isis, Gods.Janus, Gods.Kukulkan, Gods.Merlin, Gods.Nox, Gods.Nu_Wa, Gods.Olorun, Gods.Persephone, Gods.Poseidon, Gods.Ra, Gods.Raijin, Gods.Scylla, Gods.Sol, Gods.The_Morrigan, Gods.Thoth, Gods.Vulcan, Gods.Zeus, Gods.Zhong_Kui ]
    @property
    def isHunter(self):
        return self in [ Gods.Ah_Muzen_Cab, Gods.Anhur, Gods.Apollo, Gods.Artemis, Gods.Cernunnos, Gods.Chernobog, Gods.Chiron, Gods.Cupid, Gods.Hachiman, Gods.Heimdallr, Gods.Hou_Yi, Gods.Izanami, Gods.Jing_Wei, Gods.Medusa, Gods.Neith, Gods.Rama, Gods.Skadi, Gods.Ullr, Gods.Xbalanque ]
    @property
    def isAssassin(self):
        return self in [ Gods.Arachne, Gods.Awilix, Gods.Bakasura, Gods.Bastet, Gods.Camazotz, Gods.Da_Ji, Gods.Fenrir, Gods.Hun_Batz, Gods.Kali, Gods.Loki, Gods.Mercury, Gods.Ne_Zha, Gods.Nemesis, Gods.Pele, Gods.Ratatoskr, Gods.Ravana, Gods.Serqet, Gods.Set, Gods.Susano, Gods.Thanatos, Gods.Thor, Gods.Yemoja ]
    @property
    def isGuardian(self):
        return self in [ Gods.Ares, Gods.Artio, Gods.Athena, Gods.Bacchus, Gods.Cabrakan, Gods.Cerberus, Gods.Fafnir, Gods.Ganesha, Gods.Geb, Gods.Jormungandr, Gods.Khepri, Gods.Kumbhakarna, Gods.Kuzenbo, Gods.Sobek, Gods.Sylvanus, Gods.Terra, Gods.Xing_Tian, Gods.Ymir ]
    @property
    def getCard(self):
        return "https://web2.hirez.com/smite/god-cards/{}.jpg".format(self.name.lower().replace('_', '-'))
    @property
    def getIcon(self):
        return "https://web2.hirez.com/smite/god-icons/{}.jpg".format(self.name.lower().replace('_', '-'))
