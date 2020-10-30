#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

from . import Named
from ..utils.http import img_download

class God(Named):
  '''Represents a Smite God. This is a sub-class of :class:`.Enum`.

  Supported Operations:
  +-----------+--------------------------------------------+
  | Operation |           Description                      |
  +===========+============================================+
  | x == y    | Checks if two Gods are equal.              |
  +-----------+--------------------------------------------+
  | x != y    | Checks if two Gods are not equal.          |
  +-----------+--------------------------------------------+
  | hash(x)   | Return the Gods's hash.                    |
  +-----------+--------------------------------------------+
  | str(x)    | Returns the God's name with discriminator. |
  +-----------+--------------------------------------------+
  | int(x)    | Return the God's value as int.             |
  +-----------+--------------------------------------------+
  '''

  UNKNOWN = 0
  KALI = 1649
  ANUBIS = 1668
  ODIN = 1669
  YMIR = 1670
  ZEUS = 1672
  HUN_BATZ = 1673
  HE_BO = 1674
  HADES = 1676
  KUKULKAN = 1677
  BASTET = 1678
  RA = 1698
  ARACHNE = 1699
  HEL = 1718
  VAMANA = 1723
  AGNI = 1737
  SOBEK = 1747
  ARTEMIS = 1748
  BAKASURA = 1755
  GUAN_YU = 1763
  ANHUR = 1773
  CUPID = 1778
  THOR = 1779
  ARES = 1782
  FREYA = 1784
  LOKI = 1797
  BACCHUS = 1809
  FENRIR = 1843
  HERCULES = 1848
  XBALANQUE = 1864
  VULCAN = 1869
  NEITH = 1872
  POSEIDON = 1881
  APHRODITE = 1898
  APOLLO = 1899
  NE_ZHA = 1915
  ISIS = 1918
  ATHENA = 1919
  CHRONOS = 1920
  CHANGE = 1921, "Chang'e"
  TYR = 1924
  ZHONG_KUI = 1926
  MERCURY = 1941
  THANATOS = 1943
  SUN_WUKONG = 1944
  AH_MUZEN_CAB = 1956
  NU_WA = 1958
  CHAAC = 1966
  GEB = 1978
  NEMESIS = 1980
  SCYLLA = 1988
  ULLR = 1991
  KUMBHAKARNA = 1993
  JANUS = 1999
  OSIRIS = 2000
  RAMA = 2002
  SERQET = 2005
  CABRAKAN = 2008
  SYLVANUS = 2030
  AO_KUANG = 2034
  NOX = 2036
  AWILIX = 2037
  HOU_YI = 2040
  BELLONA = 2047
  MEDUSA = 2051
  AH_PUCH = 2056
  RATATOSKR = 2063
  RAVANA = 2065
  KHEPRI = 2066
  XING_TIAN = 2072
  SOL = 2074
  CHIRON = 2075
  SKADI = 2107
  AMATERASU = 2110
  RAIJIN = 2113
  JING_WEI = 2122
  SUSANO = 2123
  FAFNIR = 2136
  ERLANG_SHEN = 2138
  TERRA = 2147
  IZANAMI = 2179
  CAMAZOTZ = 2189
  THOTH = 2203
  NIKE = 2214
  THE_MORRIGAN = 2226
  KUZENBO = 2260
  CERNUNNOS = 2268
  GANESHA = 2269
  DA_JI = 2270
  CU_CHULAINN = 2319
  ARTIO = 3336
  HACHIMAN = 3344
  DISCORDIA = 3377
  CERBERUS = 3419
  ACHILLES = 3492
  CHERNOBOG = 3509
  BARON_SAMEDI = 3518
  PELE = 3543
  HERA = 3558
  KING_ARTHUR = 3565
  MERLIN = 3566
  JORMUNGANDR = 3585
  HORUS = 3611
  SET = 3612
  OLORUN = 3664
  PERSEPHONE = 3705
  YEMOJA = 3811
  HEIMDALLR = 3812
  MULAN = 3881
  BABA_YAGA = 3925
  CTHULHU = 3945
  TSUKUYOMI = 3954

  def icon(self, c=None):
    if self != God.UNKNOWN:
      __url__ = f'https://web2.hirez.com/smite/god-icons/{self.slugify}.jpg'
      if c:
        return img_download(__url__, c)
      return __url__
  def card(self, c=None):
    if self != God.UNKNOWN:
      __url__ = f'https://web2.hirez.com/smite/god-cards/{self.slugify}.jpg'
      if c:
        return img_download(__url__, c)
      return __url__

  @property
  def is_warrior(self):
    return self in [God.ACHILLES, God.AMATERASU, God.BELLONA, God.CHAAC, God.CU_CHULAINN, God.ERLANG_SHEN, God.GUAN_YU, God.HERCULES, God.HORUS, God.KING_ARTHUR, God.MULAN, God.NIKE, God.ODIN, God.OSIRIS, God.SUN_WUKONG, God.TYR, God.VAMANA]
  @property
  def is_mage(self):
    return self in [God.AGNI, God.AH_PUCH, God.ANUBIS, God.AO_KUANG, God.APHRODITE, God.BABA_YAGA, God.BARON_SAMEDI, God.CHANGE, God.CHRONOS, God.DISCORDIA, God.FREYA, God.HADES, God.HE_BO, God.HEL, God.HERA, God.ISIS, God.JANUS, God.KUKULKAN, God.MERLIN, God.NOX, God.NU_WA, God.OLORUN, God.PERSEPHONE, God.POSEIDON, God.RA, God.RAIJIN, God.SCYLLA, God.SOL, God.THE_MORRIGAN, God.THOTH, God.VULCAN, God.ZEUS, God.ZHONG_KUI]
  @property
  def is_hunter(self):
    return self in [God.AH_MUZEN_CAB, God.ANHUR, God.APOLLO, God.ARTEMIS, God.CERNUNNOS, God.CHERNOBOG, God.CHIRON, God.CUPID, God.HACHIMAN, God.HEIMDALLR, God.HOU_YI, God.IZANAMI, God.JING_WEI, God.MEDUSA, God.NEITH, God.RAMA, God.SKADI, God.ULLR, God.XBALANQUE]
  @property
  def is_guardian(self):
    return self in [God.ARES, God.ARTIO, God.ATHENA, God.BACCHUS, God.CABRAKAN, God.CERBERUS, God.CTHULHU, God.FAFNIR, God.GANESHA, God.GEB, God.JORMUNGANDR, God.KHEPRI, God.KUMBHAKARNA, God.KUZENBO, God.SOBEK, God.SYLVANUS, God.TERRA, God.XING_TIAN, God.YEMOJA, God.YMIR]
  @property
  def is_assassin(self):
    return self in [God.ARACHNE, God.AWILIX, God.BAKASURA, God.BASTET, God.CAMAZOTZ, God.DA_JI, God.FENRIR, God.HUN_BATZ, God.KALI, God.LOKI, God.MERCURY, God.NE_ZHA, God.NEMESIS, God.PELE, God.RATATOSKR, God.RAVANA, God.SERQET, God.SET, God.SUSANO, God.THANATOS, God.THOR, God.TSUKUYOMI]

__all__ = (
  'God',
)
