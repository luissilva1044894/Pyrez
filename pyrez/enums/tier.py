
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Enum
class Tier(Enum):
  UNRANKED = 0
  BRONZE_V = 1
  BRONZE_IV = 2
  BRONZE_III = 3
  BRONZE_II = 4
  BRONZE_I = 5
  SILVER_V = 6
  SILVER_IV = 7
  SILVER_III = 8
  SILVER_II = 9
  SILVER_I = 10
  GOLD_V = 11
  GOLD_IV = 12
  GOLD_III = 13
  GOLD_II = 14
  GOLD_I = 15
  PLATINUM_V = 16
  PLATINUM_IV = 17
  PLATINUM_III = 18
  PLATINUM_II = 19
  PLATINUM_I = 20
  DIAMOND_V = 21
  DIAMOND_IV = 22
  DIAMOND_III = 23
  DIAMOND_II = 24
  DIAMOND_I = 25
  MASTER = 26
  GRANDMASTER = 27

  def tier(self, lang=None):
    from .language import Language
    __tier__, __lang__ = self.name.title(), Language(lang)
    if not __lang__ == Language.ENGLISH:
      if __lang__ == Language.GERMAN:
        __tier__ = __tier__.replace('Platinum', 'Platin').replace('Diamond', 'Diamant').replace('Master', 'Meister').replace('Grandmaster', 'Großmeister')
      elif __lang__ == Language.FRENCH:
        __tier__ = __tier__.replace('Gold', 'Or').replace('Platinum', 'Platine').replace('Diamond', 'Diamant').replace('Master', 'Maître').replace('Grandmaster', 'Grand-maître')
      elif __lang__ in [Language.SPANISH, Language.SPANISH_LATIN_AMERICA]:
        __tier__ = __tier__.replace('Bronze', 'Bronce').replace('Silver', 'Plata').replace('Gold', 'Oro').replace('Platinum', 'Platino').replace('Diamond', 'Diamante').replace('Master', 'Maestro').replace('Grandmaster', 'Gran maestro')
      elif __lang__ == Language.PORTUGUESE:
        __tier__ = __tier__.replace('Silver', 'Prata').replace('Gold', 'Ouro').replace('Platinum', 'Platina').replace('Diamond', 'Diamante').replace('Master', 'Mestre').replace('Grandmaster', 'Grão-mestre')
      elif __lang__ == Language.RUSSIAN:
        #Gold: золото
        __tier__ = __tier__.replace('Gold', 'Золото').replace('Platinum', 'Платина').replace('Diamond', 'Алмаз').replace('Master', 'Мастер').replace('Grandmaster', 'Гроссмейстер')
      elif __lang__ == Language.POLISH:
        #Master: Mistrz, Grandmaster: Arcymistrz
        __tier__ = __tier__.replace('Unranked', 'Brak rangi').replace('Bronze', 'Brąz').replace('Silver', 'Srebro').replace('Gold', 'Złoto').replace('Platinum', 'Platyna').replace('Diamond', 'Diament').replace('Master', 'Mistrzostwo').replace('Grandmaster', 'Arcymistrzostwo')
      elif __lang__ == Language.TURKISH:
        __tier__ = __tier__.replace('Gold', 'Altın').replace('Platinum', 'Platin').replace('Diamond', 'Elmas').replace('Master', 'Usta').replace('Grandmaster', 'Büyük Usta')
    return __tier__.replace('IV', '4').replace('V', '5').replace('III', '3').replace('II', '2').replace('I', '1').replace('_', ' ')

  def divison(self, lang=None):
    if self in [Tier.UNRANKED, Tier.MASTER, Tier.GRANDMASTER]:
      return self.tier(lang)
    return self.tier(lang).split(' ', 1)[0]

  def loading_frame(self, c=None):
    __url__= f'https://hirez-api-docs.herokuapp.com/.assets/paladins/loading-frames/{"season-{}".format(2 if int(self) >= 11 else 1) if not self == Tier.UNRANKED else "default"}/{self.divison().lower()}.png'
    if c:
      from ..utils.http import img_download
      return img_download(c.http.get(__url__) if hasattr(c, 'http') else c.get(__url__), c._is_async if hasattr(c, '_is_async') else c.is_async)
    return __url__

  def icon(self, c=None):
    __url__ = f'https://hirez-api-docs.herokuapp.com/.assets/paladins/league-tier/{self}.png'
    if c:
      from ..utils.http import img_download
      return img_download(c.http.get(__url__) if hasattr(c, 'http') else c.get(__url__), c._is_async if hasattr(c, '_is_async') else c.is_async)
    return __url__

__all__ = (
  'Tier',
)
#Tier.Bronze_V.getId() / 5 >> Div by 5 = Current rank: <= 0.0: Unranked, > 0.0 && <= 1.0: Bronze, > 1.0 && <= 2.0: Silver, > 2.0 && <= 3.0: Gold, > 3.0 && <= 4.0: Platinum, > 4.0 && <= 5.0: Diamond, > 5.0 && <= 5.2: Master, > 5.2: Grandmaster
