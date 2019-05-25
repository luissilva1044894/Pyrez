from .API import API
from pyrez.enumerations import Endpoint, Format
class PaladinsStrikeAPI(API):
    def __init__(self, devId, authKey, responseFormat=Format.JSON, sessionId=None, storeSession=True):
        super().__init__(devId, authKey, Endpoint.PALADINS_STRIKE, responseFormat, sessionId, storeSession)
