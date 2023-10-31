import json
from genericRequest import genericPost, genericGet
from paths import *
from utils import *


class grindrUser:
    def __init__(self):
        self.sessionId = None
        self.profileId = None
        self.authToken = None
        self.xmppToken = None

    def login(self, email, password):
        response = genericPost(
            SESSIONS, {"email": email, "password": password, "token": ""}
        )
        self.sessionId = response["sessionId"]
        self.profileId = response["profileId"]
        self.authToken = response["authToken"]
        self.xmppToken = response["xmppToken"]

    def getProfiles(self, lat, lon):
        params = {
            "nearbyGeoHash": to_geohash(lat, lon),
            "onlineOnly": "false",
            "photoOnly": "false",
            "faceOnly": "false",
            "notRecentlyChatted": "false",
            "fresh": "false",
            "pageNumber": "1",
            "rightNow": "false",
        }

        response = genericGet(GET_USERS, params, auth_token=self.sessionId)
        return response

    def getTaps(self):
        response = genericGet(TAPS_RECIEVED, {}, auth_token=self.sessionId)
        return response

    # type is a number from 1 - ?
    def tap(self, profileId, type):
        response = genericPost(
            TAP, {"recipientId": profileId, "tapType": type}, auth_token=self.sessionId
        )
        return response

    def getProfile(self, profileId):
        response = genericGet(GET_PROFILE + profileId, {}, auth_token=self.sessionId)
        return response

    # profileIdList MUST be an array of profile ids
    def getProfileStatuses(self, profileIdList):
        response = genericPost(
            STATUS, {"profileIdList": profileIdList}, auth_token=self.sessionId
        )
        return response

    def getAlbum(self, profileId):
        response = genericPost(
            ALBUM, {"profileId": profileId}, auth_token=self.sessionId
        )
        return response

    #returns session data (might renew it)
    def sessions(self, email):
        response = genericPost(
            SESSIONS,
            {"email": email, "token": "", "authToken": self.authToken},
            auth_token=self.sessionId,
        )

        self.sessionId = response["sessionId"]
        self.profileId = response["profileId"]
        self.authToken = response["authToken"]
        self.xmppToken = response["xmppToken"]

        return response
