
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

from ...models.api_response import APIResponse
class Token(APIResponse):
  def __init__(self, **kw):
    super().__init__(**kw)
    self.web_token = kw.get('webToken') or kw.get('decryptedToken') or kw.get('encryptedToken') or None

  @property
  def is_encrypted(self):
    return self.get('encryptedToken') is not None
  
