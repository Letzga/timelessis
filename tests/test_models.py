from datetime import datetime

from timeless.companies.models import Company
from timeless.reservations.models import ReservationSettings, Comment
from timeless.restaurants.models import Location, Floor, TableShape, Table


def test_new_company():
    """
    @todo #31:30min Move tests to related module tests folder
    Test creating new company"""
    new_company = Company(name="First company", code="C")
    assert (new_company.name is not None
            and new_company.code is not None)


def test_new_location():
    name = "Test location"
    code = "L"
    company_id = 123
    poster_id = 100
    synchronized_on = datetime.utcnow
    new_location = Location(name=name, code=code, company_id=company_id, poster_id=poster_id,
                            synchronized_on=synchronized_on)
    assert (new_location.name == name
            and new_location.code == code
            and new_location.company_id == company_id
            and new_location.poster_id == 100
            and new_location.synchronized_on == synchronized_on)


def test_new_comment():
    body = "My comment"
    date = datetime.utcnow
    comment = Comment(body=body, date=date)
    assert (comment.body == body
            and comment.date == date)


def test_new_floor():
    id = 1
    location_id = 456
    description = "First floor"
    new_floor = Floor(id=id, location_id=location_id, description=description)
    assert (new_floor.id == id
            and new_floor.location_id == location_id
            and new_floor.description == description)


def test_new_table_shape():
    id = 1
    description = "Round table"
    picture = "/static/pictures/roundtable.png"
    new_table_shape = TableShape(
        id=id, description=description, picture=picture
    )
    assert (new_table_shape.id == id
            and new_table_shape.description == description
            and new_table_shape.picture == picture)

def test_reservation_settings():
    greeting_by_time = {
        "6": "Good morning",
        "12": "Good afternoon",
        "18": "Good morning",
    }

    reservation_settings = ReservationSettings(
        id=1,
        name="Test name",
        default_duration=10,
        default_deposit=100,
        sms_notifications=False,
        threshold_sms_time=None,
        greeting_by_time=greeting_by_time,
        sex="M",
    )

    assert (
        reservation_settings.id == 1 and
        reservation_settings.name == "Test name" and
        reservation_settings.default_duration == 10 and
        reservation_settings.default_deposit == 100 and
        reservation_settings.sms_notifications is False and
        reservation_settings.threshold_sms_time is None and
        reservation_settings.greeting_by_time == greeting_by_time and
        reservation_settings.sex == "M"
    )


def test_new_table():
    id = 42
    name = "Philosopher's Table"
    floor_id=600,
    x=40,
    y=50,
    width=320,
    height=200,
    status="available",
    max_capacity=5,
    multiple=False,
    playstation=False,
    shape_id=3

    new_table = Table(
        id=id,
        name=name,
        floor_id=floor_id,
        x=x,
        y=y,
        width=width,
        height=height,
        status=status,
        max_capacity=max_capacity,
        multiple=multiple,
        playstation=playstation,
        shape_id=shape_id
    )
    assert (
        new_table.id == id and
        new_table.name == name and
        new_table.floor_id == floor_id and
        new_table.x == x and
        new_table.y == y and
        new_table.width == width and
        new_table.height == height and
        new_table.status == status and
        new_table.max_capacity == max_capacity and
        new_table.multiple == multiple and
        new_table.playstation == playstation and
        new_table.shape_id == shape_id
    )
