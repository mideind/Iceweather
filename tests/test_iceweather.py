"""

    test_iceweather.py

    Tests for iceweather package

"""


from iceweather import closest_stations, station_for_id, id_for_station, STATIONS


_RVK_COORDS = (64.147550, -21.946171)
_SELTJ_COORDS = (64.155248, -21.998850)


def test_iceweather():
    """ Run all tests for iceweather package. """

    # Check integrity of station data
    for s in STATIONS:
        assert "id" in s
        assert "name" in s
        assert "lat" in s
        assert "lon" in s

    # Closest station logic
    assert len(closest_stations(_RVK_COORDS[0], _RVK_COORDS[1])) == 1
    assert len(closest_stations(_RVK_COORDS[0], _RVK_COORDS[1], limit=3)) == 3
    assert closest_stations(_RVK_COORDS[0], _RVK_COORDS[1])[0]["name"] == "Reykjavík"
    assert (
        "Seltjarnarnes"
        in closest_stations(_SELTJ_COORDS[0], _SELTJ_COORDS[1])[0]["name"]
    )

    # Lookup functions
    assert station_for_id(1)["name"] == "Reykjavík"
    assert id_for_station("Reykjavík") == 1
