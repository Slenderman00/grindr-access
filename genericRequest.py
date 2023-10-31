import pycurl
import json
import zlib


def genericPost(path, data, auth_token=None):
    response_data = []

    request_data = data

    data_json = json.dumps(request_data)
    c = pycurl.Curl()
    c.setopt(c.URL, "https://grindr.mobi" + path)
    c.setopt(c.CUSTOMREQUEST, "POST")

    headers = [
        "accept: application/json",
        "accept-encoding: gzip",
        "accept-language: en-US",
        "connection: Keep-Alive",
        "content-type: application/json; charset=UTF-8",
        "host: grindr.mobi",
        "l-device-info: 2938f76cff50af57;GLOBAL;2;2069590016;2277x1080;a9ffffa4-2b0e-479d-b3db-ae117c0a9686",
        "l-locale: en_US",
        "l-time-zone: Europe/Oslo",
        "requirerealdeviceinfo: true",
        "user-agent: grindr3/9.17.3.118538;118538;Free;Android 14;sdk_gphone64_x86_64;Google",
    ]

    if auth_token is not None:
        headers.append("authorization: Grindr3 " + auth_token)

    c.setopt(c.HTTPHEADER, headers)

    c.setopt(c.POSTFIELDS, data_json)

    def handle_response(data):
        response_data.append(data)

    c.setopt(c.WRITEFUNCTION, handle_response)
    c.perform()
    c.close()

    response_data = b"".join(response_data)
    decompressed_response = zlib.decompress(response_data, zlib.MAX_WBITS | 16)
    return json.loads(decompressed_response)


def genericGet(path, data, auth_token=None):
    response_data = []

    request_data = data

    c = pycurl.Curl()

    c.setopt(
        c.URL,
        "https://grindr.mobi"
        + path
        + "?"
        + "&".join([key + "=" + request_data[key] for key in request_data]),
    )
    c.setopt(c.CUSTOMREQUEST, "GET")

    headers = [
        "accept: application/json",
        "accept-encoding: gzip",
        "accept-language: en-US",
        "connection: Keep-Alive",
        "content-type: application/json; charset=UTF-8",
        "host: grindr.mobi",
        "l-device-info: 2938f76cff50af57;GLOBAL;2;2069590016;2277x1080;a9ffffa4-2b0e-479d-b3db-ae117c0a9686",
        "l-locale: en_US",
        "l-time-zone: Europe/Oslo",
        "requirerealdeviceinfo: true",
        "user-agent: grindr3/9.17.3.118538;118538;Free;Android 14;sdk_gphone64_x86_64;Google",
    ]

    if auth_token is not None:
        headers.append("authorization: Grindr3 " + auth_token)

    c.setopt(c.HTTPHEADER, headers)

    def handle_response(data):
        response_data.append(data)

    c.setopt(c.WRITEFUNCTION, handle_response)
    c.perform()
    c.close()

    response_data = b"".join(response_data)

    decompressed_response = zlib.decompress(response_data, zlib.MAX_WBITS | 16)
    return json.loads(decompressed_response)
