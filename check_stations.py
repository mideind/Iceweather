#!/usr/bin/env python3

from pprint import pprint

from iceweather.stations import STATIONS
from iceweather import observation_for_station

for s in STATIONS:
    print("Checking {0}: {1}".format(s["id"], s["name"]))
    try:
        d = observation_for_station(s["id"])
    except Exception as e:
        print(e)
    if d:
        pprint(d)
    else:
        print("ERROR !!!! " + str(s))