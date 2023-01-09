"""

    iceweather: Look up information about Icelandic weather (observations, forecasts,
    human readable descriptive texts, etc.) using vedur.is xmlweather API.

    Copyright (c) 2019-2023 Miðeind ehf.

    BSD 3-clause License (see LICENSE.txt).

"""

from .weather import (
    observation_for_stations,
    observation_for_station,
    observation_for_stations,
    observation_for_closest,
    forecast_for_stations,
    forecast_for_station,
    forecast_for_closest,
    forecast_text,
    station_list,
    closest_stations,
    id_for_station,
    station_for_id,
    STATIONS,
)

__version__ = "0.2.3"
__author__ = "Miðeind ehf."
__copyright__ = "(C) 2022 Miðeind ehf."
__license__ = "BSD 3-clause License"
