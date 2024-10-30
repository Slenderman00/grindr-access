from .generic_request import generic_post, generic_get, generic_put, generic_jpeg_upload
from .paths import (
    SESSIONS,
    TAP,
    GET_USERS,
    TAPS_RECIEVED,
    GET_PROFILE,
    STATUS,
    ALBUM,
    PROFILE,
    IMAGES
)
from .utils import to_geohash
import binascii


class GrindrUser:
    def __init__(self):
        self.sessionId = None
        self.profileId = ""
        self.authToken = None
        self.xmppToken = ""

        self.proxy = None
        self.proxy_port = None

    def set_proxy(self, proxy, proxy_port):
        self.proxy = proxy
        self.proxy_port = proxy_port

    def login(self, email, password):
        response = generic_post(
            SESSIONS,
            {"email": email, "password": password, "token": ""},
            proxy=self.proxy,
            proxy_port=self.proxy_port,
        )
        if "code" in response:
            code = response["code"]

            if code == 30:
                raise Exception("You need to verify your account via phone number!")

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

        response = generic_get(
            GET_USERS,
            params,
            auth_token=self.sessionId,
            proxy=self.proxy,
            proxy_port=self.proxy_port,
        )
        return response

    def get_taps(self):
        response = generic_get(
            TAPS_RECIEVED,
            {},
            auth_token=self.sessionId,
            proxy=self.proxy,
            proxy_port=self.proxy_port,
        )
        return response

    # type is a number from 1 - ?
    def tap(self, profileId, type):
        response = generic_post(
            TAP,
            {"recipientId": profileId, "tapType": type},
            auth_token=self.sessionId,
            proxy=self.proxy,
            proxy_port=self.proxy_port,
        )
        return response

    def get_profile(self, profileId):
        response = generic_get(
            GET_PROFILE + profileId,
            {},
            auth_token=self.sessionId,
            proxy=self.proxy,
            proxy_port=self.proxy_port,
        )
        return response

    # profileIdList MUST be an array of profile ids
    def get_profile_statuses(self, profileIdList):
        response = generic_post(
            STATUS,
            {"profileIdList": profileIdList},
            auth_token=self.sessionId,
            proxy=self.proxy,
            proxy_port=self.proxy_port,
        )
        return response

    def get_album(self, profileId):
        response = generic_post(
            ALBUM,
            {"profileId": profileId},
            auth_token=self.sessionId,
            proxy=self.proxy,
            proxy_port=self.proxy_port,
        )
        return response

    # returns session data (might renew it)
    def sessions(self, email):
        response = generic_post(
            SESSIONS,
            {"email": email, "token": "", "authToken": self.authToken},
            auth_token=self.sessionId,
            proxy=self.proxy,
            proxy_port=self.proxy_port,
        )

        self.sessionId = response["sessionId"]
        self.profileId = response["profileId"]
        self.authToken = response["authToken"]
        self.xmppToken = response["xmppToken"]

        return response

    def update_profile(self, data):
        response = generic_put(
            PROFILE,
            data,
            auth_token=self.sessionId,
            proxy=self.proxy,
            proxy_port=self.proxy_port,
        )
        return response

    # generating plain auth
    def generate_plain_auth(self):
        auth = (
            self.profileId
            + "@chat.grindr.com"
            + "\00"
            + self.profileId
            + "\00"
            + self.xmppToken
        )
        _hex = binascii.b2a_base64(str.encode(auth), newline=False)
        _hex = str(_hex)
        _hex = _hex.replace("b'", "").replace("'", "")
        return _hex

    def upload_image(self, file_io):
        return generic_jpeg_upload(
            "/v3/me/profile/images?thumbCoords=194%2C0%2C174%2C20",
            file_io,
            auth_token=self.sessionId,
            proxy=self.proxy,
            proxy_port=self.proxy_port,
        )

    def set_image(self, primary_hash, secondary_hashes=[]):
        data = {
            "primaryImageHash": primary_hash,
            "secondaryImageHashes": secondary_hashes,
        }

        return generic_put(IMAGES, data, auth_token=self.sessionId, proxy=self.proxy, proxy_port=self.proxy_port)
