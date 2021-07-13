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
    # TODO: Implement tests here
    pass


def test_forecast_for_station():
    # TODO: Implement tests here
    pass


def test_forecast_text():
    """Test descriptive text endpoint."""

    def _test_forc_text(types: tuple) -> None:
        results = forecast_text(types)
        assert (
            "results" in results
            and isinstance(results["results"], list)
            and len(results["results"]) > 0
        )

        for text in results["results"]:
            assert "title" in text and isinstance(text["title"], str)
            assert "creation" in text and isinstance(text["creation"], str)
            assert "valid_from" in text and isinstance(text["valid_from"], str)
            assert "valid_to" in text and isinstance(text["valid_to"], str)
            assert "content" in text and isinstance(text["content"], str)
            assert "id" in text and isinstance(text["id"], str)
            if isinstance(types, int) or isinstance(types, str):
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

    for t in all_types.keys():
        _test_forc_text(t)

    _test_forc_text(("2", "3", "5", "6"))
    _test_forc_text(("2", "37", "31", "42"))


def test_closest_stations():
    """Test closest station logic."""
    assert len(closest_stations(_RVK_COORDS[0], _RVK_COORDS[1])) == 1
    assert len(closest_stations(_RVK_COORDS[0], _RVK_COORDS[1], limit=3)) == 3
    assert closest_stations(_RVK_COORDS[0], _RVK_COORDS[1])[0]["name"] == "Reykjavík"
    assert (
        "Seltjarnarnes"
        in closest_stations(_SELTJ_COORDS[0], _SELTJ_COORDS[1])[0]["name"]
    )
