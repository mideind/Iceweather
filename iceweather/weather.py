"""

    iceweather: Look up information about Icelandic weather (observations, forecasts, 
    human readable descriptive texts, etc.). Wrapper for apis.is weather API.

    Copyright (c) 2019 Miðeind ehf.

"""

import math
import json
import requests
from requests import RequestException

from .stations import STATIONS


_DEFAULT_LANG = "is"

_EARTH_RADIUS = 6371.0088  # Earth's radius in km


def _distance(loc1, loc2):
    """
    Calculate the Haversine distance.
    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)
    Returns
    -------
    distance_in_km : float
    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    Source:
    https://stackoverflow.com/questions/19412462
        /getting-distance-between-two-points-based-on-latitude-longitude
    """
    lat1, lon1 = loc1
    lat2, lon2 = loc2

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    slat = math.sin(dlat / 2)
    slon = math.sin(dlon / 2)
    a = (
        slat * slat
        + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * slon * slon
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return _EARTH_RADIUS * c


def _api_call(url):
    """ Use requests to call the apis.is weather API """
    result = requests.get(url)
    if result.status_code != 200:
        raise RequestException("API status code not 200 OK for URL: {0}".format(url))

    return json.loads(result.text)


_OBSERVATIONS_URL = "https://apis.is/weather/observations/{0}?stations={1}"


def observation_for_station(station_id, lang=_DEFAULT_LANG):
    """
        Returns weather observations for the given station ID. Keys
        in the resulting dictionary are the following:

        'F'   : { 'is': 'Vindhraði (m/s)',
                  'en': 'Wind speed (m/s)'},
        'FX'  : { 'is': 'Mesti vindhraði (m/s)',
                  'en': 'Top wind speed (m/s)'},
        'FG'  : { 'is': 'Mesta vindhviða (m/s)',
                  'en': 'Top wind gust (m/s)'},
        'D'   : { 'is': 'Vindstefna',
                  'en': 'Wind direction'},
        'T'   : { 'is': 'Hiti (°C)',
                  'en': 'Air temperature (°C)'},
        'W'   : { 'is': 'Veðurlýsing',
                  'en': 'Weather description'},
        'V'   : { 'is': 'Skyggni (km)',
                  'en': 'Visibility (km)'},
        'N'   : { 'is': 'Skýjahula (%)',
                  'en': 'Cloud cover (%)'},
        'P'   : { 'is': 'Loftþrýstingur (hPa)',
                  'en': 'Air pressure'},
        'RH'  : { 'is': 'Rakastig (%)',
                  'en': 'Humidity (%)'},
        'SNC' : { 'is': 'Lýsing á snjó',
                  'en': 'Snow description'},
        'SND' : { 'is': 'Snjódýpt',
                  'en': 'Snow depth'},
        'SED' : { 'is': 'Snjólag',
                  'en': 'Snow type'},
        'RTE' : { 'is': 'Vegahiti (°C)',
                  'en': 'Road temperature (°C)'},
        'TD'  : { 'is': 'Daggarmark (°C)',
                  'en': 'Dew limit (°C)'},
        'R'   : { 'is': 'Uppsöfnuð úrkoma (mm/klst) úr sjálfvirkum mælum',
                  'en': 'Cumulative precipitation (mm/h) from automatic measuring units'}
    """
    return _api_call(_OBSERVATIONS_URL.format(lang, station_id))


def observation_for_closest(lat, lon, lang=_DEFAULT_LANG):
    """ Returns weather observation from closest weather station given coordinates """
    station = closest_station(lat, lon)
    return observation_for_station(station["id"], lang=lang)


_FORECASTS_URL = "https://apis.is/weather/forecasts/{0}?stations={1}"


def forecast_for_station(station_id, lang=_DEFAULT_LANG):
    """ Returns weather forecast from a given weather station """
    return _api_call(_FORECASTS_URL.format(lang, station_id))


def forecast_for_closest(lat, lon, lang=_DEFAULT_LANG):
    """ Returns weather forecast from closest weather station given coordinates """
    station = closest_station(lat, lon)
    return forecast_for_station(station["id"], lang=lang)


_TEXT_URL = "http://apis.is/weather/texts?types={0}"


def forecast_text(types):
    """
        Request a descriptive text from the weather API.

        Text types:

        "2" = "Veðurhorfur á landinu"
        "3" = "Veðurhorfur á höfuðborgarsvæðinu"
        "5" = "Veðurhorfur á landinu næstu daga"
        "6" = "Veðurhorfur á landinu næstu daga"
        "7" = "Weather outlook"
        "9" = "Veðuryfirlit"
        "10" = "Veðurlýsing"
        "11" = "Íslenskar viðvaranir fyrir land"
        "12" = "Veðurhorfur á landinu"
        "14" = "Enskar viðvaranir fyrir land"
        "27" = "Weather forecast for the next several days"
        "30" = "Miðhálendið"
        "31" = "Suðurland"
        "32" = "Faxaflói"
        "33" = "Breiðafjörður"
        "34" = "Vestfirðir"
        "35" = "Strandir og Norðurland vestra"
        "36" = "Norðurlandi eystra"
        "37" = "Austurland að Glettingi"
        "38" = "Austfirðir"
        "39" = "Suðausturland"
        "42" = "General synopsis
    """
    if type(types) is list:
        t = [str(x) for x in types]
    else:
        t = [str(types)]
    return _api_call(_TEXT_URL.format(",".join(t)))


def station_list():
    """ Return a list of all weather stations in Iceland """
    return STATIONS


def closest_station(lat, lon):
    """ Find the weather station closest to the given location. """
    dist_sorted = sorted(
        STATIONS, key=lambda s: _distance((lat, lon), (s["lat"], s["lon"]))
    )

    return dist_sorted[0]


def id_for_station(station_name):
    """ Return the numerical ID for a weather station, given its name """
    for s in STATIONS:
        if s["name"] == station_name:
            return s


def station_for_id(station_id):
    """ Return the name of a weather station, given its numerical ID """
    for s in STATIONS:
        if s["id"] == station_id:
            return s
