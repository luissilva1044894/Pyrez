import requests

from pyrez.enumerations import Endpoint
from pyrez.models.HiRez import AccountInfo, Transaction, UserInfo
from .APIBase import APIBase
class HiRezAPI(APIBase):
    def __init__(self, username, password, webToken=None):
        from ..utils import get_user_agent
        super().__init__(get_user_agent(requests, 'https://my.hirezstudios.com'))#super(HiRezAPI, self).__init__()
        self.username = username
        self.password = password
        self.webToken = webToken
    @classmethod
    def _getEndpoint(cls, endpoint=None, act='/acct'):
        return '{}{}{}'.format(Endpoint.HIREZ, act if act else '', '/{}'.format(endpoint) if endpoint else '')
    def _login(self):
        _ = self.makeRequest('login', {'username': self.username, 'password': self.password})#data=json.dumps{'username': username, 'password': password})
        return AccountInfo(**_) if _ else None
    def __getwebToken(self):
        if not self.webToken:
            self.webToken = self._login().webToken
        return self.webToken
    def makeRequest(self, endpoint, payload=None, methodType='POST', action='/acct'):
        return self._httpRequest(method=methodType, url=self._getEndpoint(endpoint=endpoint, act=action), json=payload)
    def changeEmail(self, newEmail):
        return self.makeRequest('changeEmail', {'webToken': self.__getwebToken(), 'newEmail': newEmail, 'password': self.password})
    @staticmethod
    def create(username, password, email=None):
        """Create a Hi-Rez account"""
        _ = requests.request(method='POST', url=self._getEndpoint(endpoint='create').replace(' ', '%20'), json={'username': username, 'password': password, 'confirmPassword': password, 'email': email, 'over13':'true', 'subscribe':'on'}, headers=HiRezAPI.PYREZ_HEADER)
        return HiRezAPI(username, password, _.json().get('webToken', None))
    def createSingleUseCode(self):
        return self.makeRequest('createSingleUseCode', {'webToken': self.__getwebToken()})
    def createVerification(self):
        return self.makeRequest('createVerification', {'webToken': self.__getwebToken()})
    def getRewards(self):
        """Get all rewards"""
        return self.makeRequest('rewards', {'webToken': self.__getwebToken()})
    def getTransactions(self):
        """Get all transactions"""
        _ = self.makeRequest('transactions', {'webToken': self.__getwebToken()})
        __ = [ Transaction(**___) for ___ in (_ or []) ]
        return __ or None
    def info(self):
        """Retrieves Hi-Rez account information"""
        _ = self.makeRequest('info', {'webToken': self.__getwebToken()})
        return UserInfo(**_) if _ else None
    def setBackupEmail(self, backupEmail):
        return self.makeRequest("setBackupEmail", {'webToken': self.__getwebToken(), 'email': backupEmail})
    def subscribe(self, subscribe=False):
        return self.makeRequest('subscribe', {'webToken': self.__getwebToken(), 'subscribe': subscribe})
    def twoFactor(notifyByEmail=True, notifyBySms=False, validationPeriod=1):
        return self.makeRequest('twoFactorOptIn', {'webToken': self.__getwebToken(), 'notifyBySms': notifyBySms, 'notifyByEmail': notifyByEmail, 'validationPeriod': validationPeriod})
    def verify(self, key):
        return self.makeRequest('verify', {'key': key})
