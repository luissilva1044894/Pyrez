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
  SKYE = 2057
  FERNANDO = 2071
  BARIK = 2073
  CASSIE = 2092
  GROHK = 2093
  EVIE = 2094
  BUCK = 2147
  RUCKUS = 2149
  ANDROXUS = 2205
  KINESSA = 2249
  GROVER = 2254
  YING = 2267
  DROGOZ = 2277
  BOMB_KING = 2281
  VIKTOR = 2285
  MAKOA = 2288
  MALDAMBA = 2303, "Mal'Damba"
  SHA_LIN = 2307
  TYRA = 2314
  TORVALD = 2322
  MAEVE = 2338
  INARA = 2348
  LEX = 2362
  SERIS = 2372
  WILLO = 2393
  ASH = 2404
  LIAN = 2417
  ZHIN = 2420
  JENOS = 2431
  STRIX = 2438
  TALUS = 2472
  TERMINUS = 2477
  KHAN = 2479
  VIVIAN = 2480
  MOJI = 2481
  FURIA = 2491
  KOGA = 2493
  DREDGE = 2495
  IMANI = 2509
  ATLAS = 2512
  IO = 2517
  RAUM = 2528
  TIBERIUS = 2529

  @property
  def carousel_url(self):
    return f'https://web2.hirez.com/paladins/assets/Carousel/{self.slugify}.png'
  @property
  def header_url(self):
    return f'https://web2.hirez.com/paladins/champion-headers/{self.slugify}.png'
  @property
  def header_bkg_url(self):
    return f'https://web2.hirez.com/paladins/champion-headers/{self.slugify}/bkg.jpg'
  @property
  def icon_url(self):
    return f'https://web2.hirez.com/paladins/champion-icons/{self.slugify}.jpg'

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

