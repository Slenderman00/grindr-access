import pygeohash as gh
import uuid
import random


def to_geohash(lat, lon, precision=5):
    return gh.encode(lat, lon, precision=precision)


def from_geohash(geohash):
    return gh.decode(geohash)


def gen_l_dev_info(): 
    identifier = uuid.uuid4()
    hex_identifier = identifier.hex
    random_integer = random.randint(1000000000, 9999999999)
    return f'{hex_identifier};GLOBAL;2;{random_integer};2277x1080;{identifier}'
