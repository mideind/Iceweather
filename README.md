# iceweather

`ìceweather` is a Python 3.6+ package for obtaining Icelandic weather information and forecasts from
the [Icelandic Met Office](https://en.vedur.is/). Uses the [apis.is](https://apis.is) gateway.

## Installation

```
$ pip install iceweather
```

## Examples

### Observations

Get latest weather observations from the nearest weather station:

```python
>>> r = observation_for_closest(64.133097, -21.898145)
>>> pprint(r)
{'results': [{'D': 'SSV',
              'F': '3',
              'FG': '7',
              'FX': '4',
              'N': '',
              'P': '1001',
              'R': '0.2',
              'RH': '75',
              'RTE': '',
              'SED': '',
              'SNC': '',
              'SND': '',
              'T': '9.3',
              'TD': '5.1',
              'V': '',
              'W': '',
              'err': '',
              'id': '1',
              'link': 'http://www.vedur.is/vedur/athuganir/kort/hofudborgarsvaedid/#group=100&station=1',
              'name': 'Reykjavík',
              'time': '2019-09-12 13:00:00',
              'valid': '1'}]}
```

Keys are the following:

| Key   |                                   |
| ----- |-----------------------------------|
| F     | Wind speed (m/s)                  |
| FX    | Top wind speed (m/s)              |
| FG    | Top wind gust (m/s)               |
| D     | Wind direction                    |
| T     | Air temperature (°C)              |
| W     | Weather description               |
| V     | Visibility (km)                   |
| N     | Cloud cover (%)                   |
| P     | Air pressure                      |
| RH    | Humidity (%)                      |
| SNC   | Snow description                  |
| SND   | Snow depth                        |
| SED   | Snow type                         |
| RTE   | Road temperature (°C)             |
| TD    | Dew limit (°C)                    |
| R     | Cumulative precipitation (mm/h)   |

```python
>>> observation_for_station(1) # Reykjavík
...
```

See stations.py for a list of all weather stations in Iceland and their unique IDs.

### Forecasts

```python
forecast_for_closest(64.133097, -21.898145)
...
forecast_for_station(1) # Reykjavík
```

### Human-readable weather descriptions

Request a descriptive text from the weather API:

```python
# Human-readable Icelandic-language weather forecast for Iceland's Capital Region
>>> forecast_text(3)
{'results': [{'content': 'Suðvestan 5-10 m/s í dag en 8-13 á morgun. Skúrir og hiti 5 til 10 stig.',
              'creation': '2019-09-12 10:20:32',
              'id': '3',
              'title': 'Veðurhorfur á höfuðborgarsvæðinu',
              'valid_from': '2019-09-12 12:00:00',
              'valid_to': '2019-09-14 00:00:00'}]}
```

```
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
```

All functions accept the `lang` keyword parameter. Supported languages are `is` and `en` for Icelandic or English results, respectively.

## Version History

0.1 - Initial release (12/09/2019)

## BSD License 

Copyright (C) 2019-2021 Miðeind ehf.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or other
materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may
be used to endorse or promote products derived from this software without specific
prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

