from timeless.companies import models as companies_models


def test_new_company():
    """
    @todo #31:30min Move tests to related module tests folder
    Test creating new company"""
    new_company = companies_models.Company(name="First company", code="C")
    assert (new_company.name is not None
            and new_company.code is not None)


def test_new_location(new_location):
    assert (new_location.name == "Test location"
            and new_location.code == "L"
            and new_location.company_id == 123)


def test_new_floor(new_floor):
    assert (new_floor.id == 1
            and new_floor.location_id == 456
            and new_floor.description == "First floor")
