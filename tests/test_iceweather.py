"""

    test_iceweather.py

    Tests for iceweather package

"""


from iceweather import *

_RVK_COORDS = (64.147550, -21.946171)
_SELTJ_COORDS = (64.155248, -21.998850)


def test_iceweather():
    """General tests for iceweather package."""

    # Check integrity of station data
    for s in STATIONS:
        assert "id" in s and isinstance(s["id"], int)
        assert "name" in s and isinstance(s["name"], str)
        s_name = s["name"]
        assert "lat" in s and isinstance(s["lat"], float)
        assert "lon" in s and isinstance(s["lon"], float)
        # Also check lookup functions
        assert station_for_id(s["id"])["name"] == s_name
        # (Some stations have the same name, this test circumvents that issue)
        assert station_for_id(id_for_station(s_name))["name"] == s_name

    # Check Reykjavík specifically
    assert id_for_station("Reykjavík") == 1
    assert station_for_id(1)["name"] == "Reykjavík"


def test_observation_for_station():
    """Test observation_for_station."""

    def _check_observation(stations, lang="is"):
        obs = observation_for_stations(stations, lang)
        assert (
            "results" in obs
            and isinstance(obs["results"], list)
            and len(obs["results"]) > 0
        )
        for station in obs["results"]:
            assert "id" in station and isinstance(station["id"], str)
            if isinstance(stations, (int, str)):
                assert station["id"] == stations or int(station["id"]) == stations
            else:
                assert station["id"] in stations or int(station["id"]) in stations
            assert "valid" in station and isinstance(station["valid"], str)
            assert "name" in station and isinstance(station["name"], str)
            assert "time" in station and isinstance(station["time"], str)
            assert "err" in station and isinstance(station["err"], str)
            assert "link" in station and isinstance(station["link"], str)
            assert "F" in station and isinstance(station["F"], str)
            assert "FX" in station and isinstance(station["FX"], str)
            assert "FG" in station and isinstance(station["FG"], str)
            assert "D" in station and isinstance(station["D"], str)
            assert "T" in station and isinstance(station["T"], str)
            assert "W" in station and isinstance(station["W"], str)
            assert "V" in station and isinstance(station["V"], str)
            assert "N" in station and isinstance(station["N"], str)
            assert "P" in station and isinstance(station["P"], str)
            assert "RH" in station and isinstance(station["RH"], str)
            assert "SNC" in station and isinstance(station["SNC"], str)
            assert "SND" in station and isinstance(station["SND"], str)
            assert "SED" in station and isinstance(station["SED"], str)
            assert "RTE" in station and isinstance(station["RTE"], str)
            assert "TD" in station and isinstance(station["TD"], str)
            assert "R" in station and isinstance(station["R"], str)

    _check_observation("1")
    _check_observation(1)
    _check_observation((1, 178, "422"))
    _check_observation(("422", "400"))
    _check_observation((422, 400))

    _check_observation("1", "en")
    _check_observation(1, "en")
    _check_observation((1, "178", 422), "en")
    _check_observation(("422", "400"), "en")
    _check_observation((422, 400), "en")

    assert observation_for_stations(422) == observation_for_station(422)
    assert observation_for_stations("178", "en") == observation_for_station("178", "en")


def test_forecast_for_station():
    """Test forecast_for_station."""

    def _check_forecast(stations, lang="is"):
        forc = forecast_for_stations(stations, lang)
        assert (
            "results" in forc
            and isinstance(forc["results"], list)
            and len(forc["results"]) > 0
        )
        for station in forc["results"]:
            assert "id" in station and isinstance(station["id"], str)
            if isinstance(stations, (int, str)):
                assert station["id"] == str(stations)
            else:
                assert station["id"] in stations or int(station["id"]) in stations
            assert "valid" in station and isinstance(station["valid"], str)
            assert "name" in station and isinstance(station["name"], str)
            assert "err" in station and isinstance(station["err"], str)
            assert "link" in station and isinstance(station["link"], str)
            assert "atime" in station and isinstance(station["atime"], str)
            assert (
                "forecast" in station
                and isinstance(station["forecast"], list)
                and len(station["forecast"]) >= 0
            )
            for forc in station["forecast"]:
                assert "D" in forc and isinstance(forc["D"], str)
                assert "F" in forc and isinstance(forc["F"], str)
                assert "N" in forc and isinstance(forc["N"], str)
                assert "R" in forc and isinstance(forc["R"], str)
                assert "T" in forc and isinstance(forc["T"], str)
                assert "TD" in forc and isinstance(forc["TD"], str)
                assert "W" in forc and isinstance(forc["W"], str)
                assert "ftime" in forc and isinstance(forc["ftime"], str)

    _check_forecast("1")
    _check_forecast(1)
    _check_forecast((1, 178, "422"))
    _check_forecast(("422", "400"))
    _check_forecast((422, 400))

    _check_forecast("1", "en")
    _check_forecast(1, "en")
    _check_forecast((1, "178", 422), "en")
    _check_forecast(("422", "400"), "en")
    _check_forecast((422, 400), "en")

    assert forecast_for_stations(422) == forecast_for_station(422)
    assert forecast_for_stations("178", "en") == forecast_for_station("178", "en")


def test_forecast_text():
    """Test descriptive text endpoint."""

    def _check_forc_text(types):
        forc_text = forecast_text(types)
        assert (
            "results" in forc_text
            and isinstance(forc_text["results"], list)
            and len(forc_text["results"]) > 0
        )

        for text in forc_text["results"]:
            assert "title" in text and isinstance(text["title"], str)
            assert "creation" in text and isinstance(text["creation"], str)
            assert "valid_from" in text and isinstance(text["valid_from"], str)
            assert "valid_to" in text and isinstance(text["valid_to"], str)
            assert "content" in text and isinstance(text["content"], str)
            assert "id" in text and isinstance(text["id"], str)
            if isinstance(types, (int, str)):
                assert text["id"] == types
            else:
                assert text["id"] in types

    all_types = {
        "2": "Veðurhorfur á landinu",
        "3": "Veðurhorfur á höfuðborgarsvæðinu",
        "5": "Veðurhorfur á landinu næstu daga",
        "6": "Veðurhorfur á landinu næstu daga",
        "7": "Weather outlook",
        "9": "Veðuryfirlit",
        # "10": "Veðurlýsing",
        "11": "Íslenskar viðvaranir fyrir land",
        "12": "Veðurhorfur á landinu",
        "14": "Enskar viðvaranir fyrir land",
        "27": "Weather forecast for the next several days",
        "30": "Miðhálendið",
        "31": "Suðurland",
        "32": "Faxaflói",
        "33": "Breiðafjörður",
        "34": "Vestfirðir",
        "35": "Strandir og Norðurland vestra",
        "36": "Norðurlandi eystra",
        "37": "Austurland að Glettingi",
        "38": "Austfirðir",
        "39": "Suðausturland",
        "42": "General synopsis",
    }

    for t in all_types:
        _check_forc_text(t)

    _check_forc_text(("2", "3", "5", "6"))
    _check_forc_text(("2", "37", "31", "42"))


def test_closest_stations():
    """Test closest station logic."""
    assert len(closest_stations(_RVK_COORDS[0], _RVK_COORDS[1])) == 1
    assert len(closest_stations(_RVK_COORDS[0], _RVK_COORDS[1], limit=3)) == 3
    assert "Reykjavík" in closest_stations(_RVK_COORDS[0], _RVK_COORDS[1])[0]["name"]
    assert (
        "Seltjarnarnes"
        in closest_stations(_SELTJ_COORDS[0], _SELTJ_COORDS[1])[0]["name"]
    )
