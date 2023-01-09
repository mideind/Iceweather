#!/usr/bin/env python3
"""

    iceweather: Look up information about Icelandic weather (observations, forecasts,
    human readable descriptive texts, etc.) using vedur.is xmlweather API.

    Copyright (c) 2019-2023 Miðeind ehf.
    Original author: Sveinbjorn Thordarson

    BSD 3-clause License (see License.txt).


    Try to fetch observation data from all weather stations.

"""

from pprint import pprint

from iceweather.stations import STATIONS
from iceweather import observation_for_station

for s in STATIONS:
    sid = s["id"]
    name = s["name"]
    # print(f"Checking {sid}: {name}")
    d = None
    try:
        d = observation_for_station(s["id"])
        err = d["results"][0]["err"]
        valid = d["results"][0]["valid"]
        if err or not valid:
            raise Exception(f"Error fetching data for station {sid}:{name}: {err}")
    except Exception as e:
        print(e)
    if d:
        pass
        # pprint(d)
    else:
        print("ERROR !!!! " + str(s))
