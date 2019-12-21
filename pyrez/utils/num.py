
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

def format_decimal(data, form=',d'):
  if data:
    return format(int(data), form)
  return 0

def num_or_string(v, d=None):
  """Loads a value from MO into either an int or string value.
  String is returned if we can't turn it into an int.
  """
  try:
    return int(str(v))#.replace(',', '')
  except (ValueError, TypeError):
    try:
      _value = float(str(v).replace(',', '.'))
      return 0 if _value == 0 else _value
    except (ValueError, TypeError):
      pass
  return d or v

def random(min, max, as_int=True):
  import random
  if as_int:
    return random.randint(min, max)
  return random.randrange(min, max)

def winratio(wins, matches_played):
  _w = wins /((matches_played) if matches_played > 1 else 1) * 100.0
  return int(_w) if _w % 2 == 0 else round(_w, 2)
