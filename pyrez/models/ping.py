
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

from datetime import datetime

from .api_response import APIResponse

class Ping(APIResponse):
  def __init__(self, v, *args, **kw):
    _js, _json = str(v).split(' '), {}
    if len(_js) > 11:
      _json['api_name'] = _js[0]
      _json['api_version'] = _js[2].replace(')', '')
      _json['game_patch'] = _js[5].replace(']', '')
      _json['ping'] = _js[8] == 'successful.'
      #_json['date'] = datetime.strptime('{} {} {}'.format(_js[10].replace('Date:', ''), _js[11], _js[12]), '%m/%d/%Y %I:%M:%S %p')
      _json['timestamp'] = f'{_js[10].replace("Date:", "")} {_js[11]} {_js[12]}'
    super().__init__(*args, **{**_json, **kw})
