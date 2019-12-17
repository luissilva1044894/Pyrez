
enum_template = """#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

from . import Named
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

  Unknown = 0, 'Unknown'
  [GODS]

  @property
  def icon_url(self):
    return 'https://web2.hirez.com/smite/god-icons/{}.jpg'.format(self.name.lower().replace('_', '-'))
  @property
  def card_url(self):
    return 'https://web2.hirez.com/smite/god-cards/{}.jpg'.format(self.name.lower().replace('_', '-'))

  @property
  def is_warrior(self):
    return self in [[WARRIORS]]
  @property
  def is_mage(self):
    return self in [[MAGES]]
  @property
  def is_hunter(self):
    return self in [[HUNTERS]]
  @property
  def is_guardian(self):
    return self in [[GUARDIANS]]
  @property
  def is_assassin(self):
    return self in [[ASSASSINS]]

__all__ = (
  'God',
)

"""

def fix_name(o):
  return str(o).replace(' ', '_').replace("'", '')
def create_value(_):
  return f'{fix_name(_.get("god_name_EN")).upper()} = {_.get("id")}, "{_.get("god_name_EN")}"'
def update(*args, **kw):
  #May add Pantheon? [ Arthurian, Celtic, Chinese, Egyptian, Greek, Hindu, Japanese, Mayan, Norse, Polynesian, Roman, Slavic, Voodoo, Yoruba ]
  from ..utils.file import get_path, read_file
  root_path = f'{get_path(root=True)}'
  __json__ = read_file(f'{root_path}\\data\\links.json').get('smite')

  from ..utils.http import Client
  _session_ = Client(*args, **kw)
  gods = _session_.get(f'{__json__["website"]["api"]}all-gods/1') or {}
  if gods:
    warriors = [f'God.{fix_name(_.get("god_name_EN")).upper()}' for _ in gods if 'warrior' in _.get('role_EN','').lower()]
    mages = [f'God.{fix_name(_.get("god_name_EN")).upper()}' for _ in gods if 'mage' in _.get('role_EN','').lower()]
    hunters = [f'God.{fix_name(_.get("god_name_EN")).upper()}' for _ in gods if 'hunter' in _.get('role_EN','').lower()]
    guardians = [f'God.{fix_name(_.get("god_name_EN")).upper()}' for _ in gods if 'guardian' in _.get('role_EN','').lower()]
    assassins = [f'God.{fix_name(_.get("god_name_EN")).upper()}' for _ in gods if 'assassin' in _.get('role_EN','').lower()]
    gods = [f'{create_value(_)}' for _ in sorted(gods, key=lambda x: x.get("id")) if _]
    __ = enum_template.replace('[GODS]', '\n  '.join(gods)).replace('[WARRIORS]', ', '.join(warriors)).replace('[MAGES]', ', '.join(mages)).replace('[HUNTERS]', ', '.join(hunters)).replace('[GUARDIANS]', ', '.join(guardians)).replace('[ASSASSINS]', ', '.join(assassins))

    try:
      with open(f'{root_path}\\enums\\god.py', 'w', encoding='utf-8') as f:
        f.write(__)
    except OSError as exc:
      print(exc)
