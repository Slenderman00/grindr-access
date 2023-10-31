import pygeohash as gh

def to_geohash(lat, lon, precision=5):
    return gh.encode(lat, lon, precision=precision)

def from_geohash(geohash):
    return gh.decode(geohash)

