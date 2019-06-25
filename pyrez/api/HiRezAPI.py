import requests

from pyrez.enumerations import Endpoint
from pyrez.models.HiRez import AccountInfo, Transaction, UserInfo
from .APIBase import APIBase
class HiRezAPI(APIBase):
    def __init__(self, username, password, web_token=None):
        from ..utils.http import build_user_agent
        super().__init__(build_user_agent(requests, 'https://my.hirezstudios.com'))#super(HiRezAPI, self).__init__()
        self.username = username
        self.password = password
        self.web_token = web_token
    @classmethod
    def _get_endpoint(cls, endpoint=None, act='/acct'):
        return '{}{}{}'.format(Endpoint.HIREZ, act if act else '', '/{}'.format(endpoint) if endpoint else '')
    def _login(self):
        _ = self.make_request('login', {'username': self.username, 'password': self.password})#data=json.dumps{'username': username, 'password': password})
        return AccountInfo(**_) if _ else None
    def __get_web_token(self):
        if not self.web_token:
            self.web_token = self._login().web_token
        return self.web_token
    def make_request(self, endpoint, payload=None, method_type='POST', action='/acct'):
        #self.payload.update('webToken': self.__get_web_token())
        return self._httpRequest(method=method_type, url=self._get_endpoint(endpoint=endpoint, act=action), json=payload)
    def change_email(self, new_email):
        return self.make_request('changeEmail', {'webToken': self.__get_web_token(), 'newEmail': newEmail, 'password': self.password})
    @staticmethod
    def create(username, password, email=None):
        """Create a Hi-Rez account"""
        from ..utils.http import build_user_agent
        _ = requests.request(method='POST', url=self._get_endpoint(endpoint='create').replace(' ', '%20'), json={'username': username, 'password': password, 'confirmPassword': password, 'email': email, 'over13':'true', 'subscribe':'on'}, headers=build_user_agent(requests, 'https://my.hirezstudios.com'))
        return HiRezAPI(username, password, _.json().get('webToken', None))
    def create_code(self):
        return self.make_request('createSingleUseCode', {'webToken': self.__get_web_token()})
    def create_verification(self):
        return self.make_request('createVerification', {'webToken': self.__get_web_token()})
    def get_rewards(self):
        """Get all rewards"""
        return self.make_request('rewards', {'webToken': self.__get_web_token()})
    def get_transactions(self):
        """Get all transactions"""
        _ = self.make_request('transactions', {'webToken': self.__get_web_token()})
        __ = [ Transaction(**___) for ___ in (_ or []) ]
        return __ or None
    def info(self):
        """Retrieves Hi-Rez account information"""
        _ = self.make_request('info', {'webToken': self.__get_web_token()})
        return UserInfo(**_) if _ else None
    def set_backup_email(self, backup_email):
        return self.make_request("setBackupEmail", {'webToken': self.__get_web_token(), 'email': backup_email})
    def subscribe(self, subscribe=False):
        return self.make_request('subscribe', {'webToken': self.__get_web_token(), 'subscribe': subscribe})
    def two_factor(notify_by_email=True, notify_by_sms=False, validation_period=1):
        return self.make_request('twoFactorOptIn', {'webToken': self.__get_web_token(), 'notifyBySms': notify_by_sms, 'notifyByEmail': notify_by_email, 'validationPeriod': validation_period})
    def verify(self, key):
        return self.make_request('verify', {'key': key})
