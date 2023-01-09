#!/usr/bin/env python3
"""

    iceweather: Look up information about Icelandic weather (observations, forecasts,
    human readable descriptive texts, etc.) using vedur.is xmlweather API.

    Copyright (c) 2019-2023 Miðeind ehf.
    Original author: Sveinbjorn Thordarson

    BSD 3-clause License (see License.txt).


    Scrape coordinates of all weather stations in Iceland from vedur.is

"""

import time
from pprint import pprint

import requests
from bs4 import BeautifulSoup

STATIONS_URL = "https://www.vedur.is/vedur/stodvar"

STATIONS = []

result = requests.get(STATIONS_URL)

if result.status_code != 200:
    exit("Failed to get station url")


c = result.content

soup = BeautifulSoup(c, "html.parser")

samples = soup.find_all("td", "name")

for s in samples:
    name = s.contents[0]

    tr = s.parent

    a = tr.find_all("a", string="Uppl.")
    href = a[0]["href"]

    uppl_url = "https://www.vedur.is" + href
    result = requests.get(uppl_url)
    if result.status_code != 200:
        print("Failed to fetch " + uppl_url)
        continue

    s = BeautifulSoup(result.content, "html.parser")

    print(name)

    # Station ID
    td = s.find("td", string="Stöðvanúmer")
    assert td
    tr = td.parent
    assert tr
    tdloc = tr.find_all("td")[-1]
    loctxt = str(tdloc.find(text=True))

    station_id = int(loctxt)

    # Coordinates
    td = s.find("td", string="Staðsetning")
    assert td
    tr = td.parent
    assert tr
    tdloc = tr.find_all("td")[-1]
    loctxt = str(tdloc.find(text=True))

    numloc = loctxt.split("(")[-1].rstrip(")")

    (lat, lon) = numloc.split(", ")

    lat = float(lat.strip().replace(",", "."))
    lon = float(lon.strip().replace(",", ".")) * -1

    station_info = {
        "id": station_id,
        "name": name,
        "lat": lat,
        "lon": lon,
    }

    STATIONS.append(station_info)
    pprint(station_info)

    # Let's be polite and give the server some breathing space
    time.sleep(0.5)

print("-------------------")
pprint(STATIONS)
