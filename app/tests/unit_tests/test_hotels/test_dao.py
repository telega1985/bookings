import pytest

from app.hotels.service import HotelService


@pytest.mark.parametrize("hotel_id,exists", [
    (1, True),
    (6, True),
    (7, False)
])
async def test_get_hotel_by_id(hotel_id, exists):
    hotel = await HotelService.service_get_hotel_by_id(hotel_id)

    if exists:
        assert hotel
        assert hotel.id == hotel_id
    else:
        assert not hotel
