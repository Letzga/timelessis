from datetime import datetime
import flask

from timeless.access_control.location_admin_privileges import has_privilege
from timeless.access_control.methods import Method
from timeless.companies.models import Company
from timeless.employees.models import Employee
from timeless.restaurants.models import Location, Floor, TableShape, Table


def test_can_access_location_tables(app, db_session):
    """User with Location Admin role can access the tables
    from a Location owned by the company they work at"""
    company = Company(
        id=1, name="Foo Inc.", code="code1", address="addr"
    )
    location = Location(
        id=1,
        name="name",
        code="123",
        company_id=company.id,
        country="US",
        region="region",
        city="city",
        address="address",
        longitude="123",
        latitude="123",
        type="type",
        status="status"
    )
    floor = Floor(
        id=1, description="1st Floor", location_id=location.id
    )
    shape = TableShape(
        id=1, description="Round Table", picture="/path/to/file.jpg"
    )
    table = Table(
        id=1,
        name="some table",
        floor_id=floor.id,
        x=40,
        y=50,
        width=320,
        height=150,
        status=1,
        max_capacity=12,
        multiple=False,
        playstation=False,
        shape_id=1
    )
    db_session.add(company)
    db_session.add(location)
    db_session.add(floor)
    db_session.add(shape)
    db_session.commit()
    db_session.add(table)
    user = Employee(
        id=1, first_name="Alice", last_name="Cooper",
        username="alice", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=3333,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=company.id,
        email="test@test.com", password="bla"
    )
    flask.g.user = user
    db_session.add(user)
    db_session.commit()
    assert has_privilege(
        method=Method.READ, resource="tables", id=table.id
    )


def test_cannot_access_tables_from_other_locations(app, db_session):
    """User with Location Admin role cannot access the tables
    from a Location which is not owned by the company they work at"""
    company = Company(
        id=1, name="Foo Inc.", code="code1", address="addr"
    )
    other = Company(
        id=2, name="Other Foo Inc.", code="code2", address="addr2"
    )
    location = Location(
        id=1,
        name="name",
        code="123",
        company_id=other.id,
        country="US",
        region="region",
        city="city",
        address="address",
        longitude="123",
        latitude="123",
        type="type",
        status="status"
    )
    floor = Floor(
        id=1, description="1st Floor", location_id=location.id
    )
    shape = TableShape(
        id=1, description="Round Table", picture="/path/to/file.jpg"
    )
    table = Table(
        id=1,
        name="some table",
        floor_id=floor.id,
        x=40,
        y=50,
        width=320,
        height=150,
        status=1,
        max_capacity=12,
        multiple=False,
        playstation=False,
        shape_id=1
    )
    db_session.add(company)
    db_session.add(other)
    db_session.add(location)
    db_session.add(floor)
    db_session.add(shape)
    db_session.commit()
    db_session.add(table)
    user = Employee(
        id=1, first_name="Alice", last_name="Cooper",
        username="alice", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=3333,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=company.id,
        email="test@test.com", password="bla"
    )
    flask.g.user = user
    db_session.add(user)
    db_session.commit()
    assert not has_privilege(
        method=Method.READ, resource="tables", id=table.id
    )
