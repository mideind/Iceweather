#!/usr/bin/env python
"""
    Scrape coordinates of all weather stations in Iceland from vedur.is
"""

from bs4 import BeautifulSoup
import requests
import time
from pprint import pprint

STATIONS_URL = "https://www.vedur.is/vedur/stodvar"

STATIONS = {}

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
    tr = td.parent
    tdloc = tr.find_all("td")[-1]
    loctxt = str(tdloc.find(text=True))
    
    station_id = int(loctxt)

    # Coordinates
    td = s.find("td", string="Staðsetning")
    tr = td.parent

    tdloc = tr.find_all("td")[-1]
    loctxt = str(tdloc.find(text=True))

    numloc = loctxt.split("(")[-1].rstrip(")")

    (lat, lon) = numloc.split(", ")

    lat = float(lat.strip().replace(",", "."))
    lon = float(lon.strip().replace(",", ".")) * -1

    print(lat, lon)

    STATIONS[station_id] = {
        "name": name,
        "lat": lat,
        "lon": lon,
    }

    # Let's be polite
    time.sleep(0.5)


pprint(STATIONS)







