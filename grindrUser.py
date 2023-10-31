import json
from genericRequest import genericPost, genericGet
from paths import *

class grindrUser:
    def __init__(self):
        self.sessionId = None
        self.profileId = None
        self.authToken = None
        self.xmppToken = None

    def login(self, email, password):
        response = genericPost(SESSIONS, { 'email': email, 'password': password, 'token': '' })
        response = json.loads(response)
        self.sessionId = response['sessionId']
        self.profileId = response['profileId']
        self.authToken = response['authToken']
        self.xmppToken = response['xmppToken']

    def getProfiles(self):
        params = {
            'nearbyGeoHash': '9q9hvuskv2cf',
            'onlineOnly': 'false',
            'photoOnly': 'false',
            'faceOnly': 'false',
            'notRecentlyChatted': 'false',
            'fresh': 'false',
            'pageNumber': '1',
            'rightNow': 'false',
        }

        response = genericGet(GET_USERS, params, auth_token=self.sessionId)
        return response
    
user = grindrUser()
mail = input('Email: ')
password = input('Password: ')

user.login(mail, password)
print(user.getProfiles())