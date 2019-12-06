
champion_enum_template = """#!/usr/bin/env python
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

  Unknown = 0, 'Unknown'
  [CHAMPS]

  @property
  def header_url(self):
    return 'https://web2.hirez.com/paladins/champion-headers/{}.png'.format(self.name.lower().replace(' ', '-'))#.replace(' ', '')
  @property
  def icon_url(self):
    return 'https://web2.hirez.com/paladins/champion-icons/{}.jpg'.format(self.name.lower().replace(' ', '-'))

  @property
  def is_damage(self):
    return self in [[DMGS]]
  @property
  def is_flank(self):
    return self in [[FLANKS]]
  @property
  def is_tank(self):
    return self in [[TANKS]]
  @property
  def is_support(self):
    return self in [[SUPS]]

__all__ = (
  'Champion',
)

"""

def fix_name(o):
  return str(o).replace(' ', '_').replace("'", '')
def create_value(_):
  #Named enum doesn't allow alias?
  _x = f'{fix_name(_.get("feName"))} = {_.get("id")}, "{_.get("feName")}"\n  {fix_name(_.get("feName"))} = \'{fix_name(_.get("feName")).lower()}\', "{_.get("feName")}"'
  if ' ' in _.get('feName'):
    _n = _.get('feName').replace(' ', '').replace("'", '').lower()
    _x += f'\n  {fix_name(_.get("feName"))} = \'{_n}\', "{_.get("feName")}"'
  if "'" in _.get('feName'):
    _n = _.get('feName').replace(' ', '').lower()
    _x += f'\n  {fix_name(_.get("feName"))} = "{_n}", "{_.get("feName")}"'
  return _x
def update(*args, **kw):
  from ..utils.file import get_path, read_file
  root_path = f'{get_path(root=True)}'
  __json__ = read_file(f'{root_path}\\data\\links.json').get('paladins')

  from ..utils.http import Client
  _session_ = Client(*args, **kw)
  champs = _session_.get(f'{__json__["website"]["api"]}champion-hub/1') or {}
  if champs:
    flanks = [f'Champion.{fix_name(_.get("feName"))}' for _ in champs if 'flank' in _.get('role','').lower()]
    supports = [f'Champion.{fix_name(_.get("feName"))}' for _ in champs if 'support' in _.get('role','').lower()]
    damages = [f'Champion.{fix_name(_.get("feName"))}' for _ in champs if 'damage' in _.get('role','').lower()]
    fronts = [f'Champion.{fix_name(_.get("feName"))}' for _ in champs if 'front' in _.get('role','').lower()]
    champs = [f'{create_value(_)}' for _ in champs if _]
    __ = champion_enum_template.replace('[CHAMPS]', '\n  '.join(champs)).replace('[FLANKS]', ', '.join(flanks)).replace('[SUPS]', ', '.join(supports)).replace('[DMGS]', ', '.join(damages)).replace('[TANKS]', ', '.join(fronts))

    try:
      with open(f'{root_path}\\enums\\champion.py', 'w', encoding='utf-8') as f:
        f.write(__)
    except OSError as exc:
      print(exc)
