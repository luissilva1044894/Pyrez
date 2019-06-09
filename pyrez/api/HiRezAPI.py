from sys import version_info
import requests

from pyrez import __version__ as pyrez
from pyrez.enumerations import Endpoint
from pyrez.models.HiRez import AccountInfo, Transaction, UserInfo
from .APIBase import APIBase
class HiRezAPI(APIBase):
    PYREZ_HEADER = { 'user-agent': '{pyrez} [Python/{python.major}.{python.minor}.{python.micro} requests/{requests}]'.format(pyrez=pyrez.__title__, python=version_info, requests=requests.__version__), 'Origin': 'https://my.hirezstudios.com' }
    def __init__(self, username, password, webToken=None):
        super().__init__(self.PYREZ_HEADER)#super(HiRezAPI, self).__init__()
        self.username = username
        self.password = password
        self.webToken = webToken
    @classmethod
    def _getEndpoint(cls, endpoint=None, act='/acct'):
        return "{}{}{}".format(Endpoint.HIREZ, act if act else '', '/{}'.format(endpoint) if endpoint else '')
    def _login(self):
        _ = self.makeRequest('login', {'username': self.username, 'password': self.password})#data=json.dumps{'username': username, 'password': password})
        return AccountInfo(**_) if _ else None
    def __getwebToken(self):
        if not self.webToken:
            self.webToken = self._login().webToken
        return self.webToken
    def makeRequest(self, endpoint, params=None, methodType='POST', action='/acct'):
        return self._httpRequest(method=methodType, url=self._getEndpoint(endpoint=endpoint, act=action), json=params)
    def changeEmail(self, newEmail):
        return self.makeRequest('changeEmail', {'webToken': self.__getwebToken(), 'newEmail': newEmail, 'password': self.password})
    @staticmethod
    def create(username, password, email=None):
        _ = requests.request(method='POST', url=self._getEndpoint(endpoint='create').replace(' ', '%20'), json={'username': username, 'password': password, 'confirmPassword': password, 'email': email, 'over13':'true', 'subscribe':'on'}, headers=HiRezAPI.PYREZ_HEADER)
        return HiRezAPI(username, password, _.json().get('webToken', None))
    def createSingleUseCode(self):
        return self.makeRequest('createSingleUseCode', {'webToken': self.__getwebToken()})
    def createVerification(self):
        return self.makeRequest('createVerification', {'webToken': self.__getwebToken()})
    def getRewards(self):
        return self.makeRequest('rewards', {'webToken': self.__getwebToken()})
    def getTransactions(self):
        _ = self.makeRequest('transactions', {'webToken': self.__getwebToken()})
        __ = [ Transaction(**___) for ___ in (_ or []) ]
        return __ or None
    def info(self):
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
