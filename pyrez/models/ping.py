#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

class Ping:
  def __init__(self, v, *args, **kw):
    self.json = str(v)
    _js = str(v).split(' ')
    if len(_js) > 11:
      from datetime import datetime
      self.api_name = _js[0]
      self.api_version = _js[2].replace(')', '')
      self.game_patch = _js[5].replace(']', '')
      self.ping = _js[8] == 'successful.'
      self.date = datetime.strptime('{} {} {}'.format(_js[10].replace('Date:', ''), _js[11], _js[12]), '%m/%d/%Y %I:%M:%S %p')
  def __str__(self):
    return f'API Name: {self.api_name} API Version: {self.api_version} Game Version: {self.game_patch} Date: {self.date}'
