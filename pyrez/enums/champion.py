#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

from . import Named
class Champion(Named):
  '''Represents a Paladins Champion. This is a sub-class of :class:`.Enum`.

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
  '''

  UNKNOWN = 0
  PIP = 2056
  PIP = '皮皮'
  PIP = 'пип'
  SKYE = 2057
  SKYE = '斯卡伊'
  SKYE = 'скай'
  FERNANDO = 2071
  FERNANDO = '费尔南多'
  FERNANDO = 'фернандо'
  BARIK = 2073
  BARIK = '巴里克'
  BARIK = 'барик'
  CASSIE = 2092
  CASSIE = '凯茜'
  CASSIE = 'кэсси'
  GROHK = 2093
  GROHK = '古洛克'
  GROHK = 'грок'
  EVIE = 2094
  EVIE = '伊薇'
  EVIE = 'иви'
  BUCK = 2147
  BUCK = '巴克'
  BUCK = 'бак'
  RUCKUS = 2149
  RUCKUS = '吵吵先生'
  RUCKUS = 'рукус'
  ANDROXUS = 2205
  ANDROXUS = '安卓克瑟斯'
  ANDROXUS = 'андроксус'
  KINESSA = 2249
  KINESSA = '凯尼莎'
  KINESSA = 'кинесса'
  GROVER = 2254
  GROVER = '格鲁'
  GROVER = 'гровер'
  YING = 2267
  YING = '樱'
  YING = 'инь'
  DROGOZ = 2277
  DROGOZ = '卓格斯'
  DROGOZ = 'дрогоз'
  BOMB_KING = 2281
  BOMB_KING = '炸弹王'
  BOMB_KING = 'король_бомб'
  VIKTOR = 2285
  VIKTOR = '维克托'
  VIKTOR = 'виктор'
  MAKOA = 2288
  MAKOA = '莫科亚'
  MAKOA = 'макоа'
  MALDAMBA = 2303, "Mal'Damba"
  MALDAMBA = '马尔丹巴'
  MALDAMBA = 'мэл_дэмба'
  SHA_LIN = 2307
  SHA_LIN = '沙林'
  SHA_LIN = 'ша_линь'
  TYRA = 2314
  TYRA = '媞拉'
  TYRA = 'тайра'
  TORVALD = 2322
  TORVALD = '托瓦德'
  TORVALD = 'торвальд'
  MAEVE = 2338
  MAEVE = '梅芙'
  MAEVE = 'мейв'
  INARA = 2348
  INARA = '伊娜拉'
  INARA = 'инара'
  LEX = 2362
  LEX = '雷克斯'
  LEX = 'лекс'
  SERIS = 2372
  SERIS = '赛丽丝'
  SERIS = 'серис'
  WILLO = 2393
  WILLO = '薇洛'
  WILLO = 'вилло'
  ASH = 2404
  ASH = '艾什'
  ASH = 'эш'
  LIAN = 2417
  LIAN = '莲'
  LIAN = 'лиан'
  ZHIN = 2420
  ZHIN = '烬'
  ZHIN = 'дзин'
  JENOS = 2431
  JENOS = '杰诺斯'
  JENOS = 'дженос'
  STRIX = 2438
  STRIX = '夜鹰'
  STRIX = 'стрикс'
  TALUS = 2472
  TALUS = '泰兰'
  TALUS = 'талус'
  TERMINUS = 2477
  TERMINUS = '特米纳斯'
  TERMINUS = 'терминус'
  KHAN = 2479
  KHAN = '凯'
  KHAN = 'хан'
  VIVIAN = 2480
  VIVIAN = '薇薇安'
  VIVIAN = 'вивиан'
  MOJI = 2481
  MOJI = '莫吉'
  MOJI = 'моджи'
  FURIA = 2491
  FURIA = '芙瑞雅'
  FURIA = 'фурия'
  KOGA = 2493
  KOGA = '古贺'
  KOGA = 'кога'
  DREDGE = 2495
  DREDGE = 'дредж'
  IMANI = 2509
  IMANI = 'mage'
  IMANI = 'имани'
  ATLAS = 2512
  ATLAS = 'атлас'
  IO = 2517
  IO = 'ио'
  RAUM = 2528
  RAUM = 'demon'
  RAUM = 'раум'
  TIBERIUS = 2529
  TIBERIUS = 'tigron'
  TIBERIUS = 'тибериус'
  CORVUS = 2533
  CORVUS = "корвус"

  def carousel(self, c=None, **kw):
    if self:
      __url__ = f'https://web2.hirez.com/paladins/assets/carousel/{self.slugify}.png'
      if c:
        if hasattr(c, 'http'):
          return c.http.get(__url__, **kw)
        return c.get(__url__, **kw)
      return __url__

  def header(self, c=None, **kw):
    if self:
      __url__ = f'https://web2.hirez.com/paladins/champion-headers/{self.slugify}.png'
      if c:
        if hasattr(c, 'http'):
          return c.http.get(__url__, **kw)
        return c.get(__url__, **kw)
      return __url__

  def header_bkg(self, c=None, **kw):
    if self:
      __url__ = f'https://web2.hirez.com/paladins/champion-headers/{self.slugify}/bkg.jpg'
      if c:
        if hasattr(c, 'http'):
          return c.http.get(__url__, **kw)
        return c.get(__url__, **kw)
      return __url__

  def icon(self, c=None, **kw):
    if self:
      __url__ = f'https://web2.hirez.com/paladins/champion-icons/{self.slugify}.jpg'
      if c:
        if hasattr(c, 'http'):
          return c.http.get(__url__, **kw)
        return c.get(__url__, **kw)
      return __url__

  @property
  def is_damage(self):
    return self in [Champion.BOMB_KING, Champion.CASSIE, Champion.DREDGE, Champion.DROGOZ, Champion.IMANI, Champion.KINESSA, Champion.LIAN, Champion.SHA_LIN, Champion.STRIX, Champion.TIBERIUS, Champion.TYRA, Champion.VIKTOR, Champion.VIVIAN, Champion.WILLO]
  @property
  def is_flank(self):
    return self in [Champion.ANDROXUS, Champion.BUCK, Champion.EVIE, Champion.KOGA, Champion.LEX, Champion.MAEVE, Champion.MOJI, Champion.SKYE, Champion.TALUS, Champion.ZHIN]
  @property
  def is_tank(self):
    return self in [Champion.ASH, Champion.ATLAS, Champion.BARIK, Champion.FERNANDO, Champion.INARA, Champion.KHAN, Champion.MAKOA, Champion.RAUM, Champion.RUCKUS, Champion.TERMINUS, Champion.TORVALD]
  @property
  def is_support(self):
    return self in [Champion.FURIA, Champion.GROHK, Champion.GROVER, Champion.IO, Champion.JENOS, Champion.MALDAMBA, Champion.PIP, Champion.SERIS, Champion.YING]

__all__ = (
  'Champion',
)

