from .API import API
from pyrez.enumerations import Endpoint, Format
class HandOfTheGodsAPI(API):
    def __init__(self, devId, authKey, response_format=Format.JSON, sessionId=None, storeSession=True):
        super().__init__(devId, authKey, Endpoint.HAND_OF_THE_GODS, response_format, sessionId, storeSession)
