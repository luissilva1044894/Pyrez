from .API import API
from pyrez.enumerations import Endpoint, Format
class PaladinsStrikeAPI(API):
    def __init__(self, devId, authKey, response_format=Format.JSON, sessionId=None, storeSession=True):
        super().__init__(devId, authKey, Endpoint.PALADINS_STRIKE, response_format, sessionId, storeSession)
