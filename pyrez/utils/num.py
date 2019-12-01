
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

def try_int(value, default=None):
  try:
    return int(value)
  except (ValueError, TypeError):
    pass
  return default or value

def random(min, max, as_int=True):
  import random
  if as_int:
    return random.randint(min, max)
  return random.randrange(min, max)

def winratio(wins, matches_played):
  _w = wins /((matches_played) if matches_played > 1 else 1) * 100.0
  return int(_w) if _w % 2 == 0 else round(_w, 2)
