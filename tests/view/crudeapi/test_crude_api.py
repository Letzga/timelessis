import pytest
import werkzeug
from timeless.views import CrudAPIView
from timeless.restaurants.models import Location
from timeless.companies.models import Company
"""
    Tests for CrudeAPIView.
    
    @todo #221:30min Continue with the implementation of CrudAPIView.
     Implement post, put and delete methods. We should return json
     representation of object model in methods. After that remove the ignore annotation from tests on
     test_crude_api.py.
"""

@pytest.mark.skip
def test_get_found_object():
    company = Company(
        name="Los Pollos Hermanos.",
        code="LPH",
        address="1200 - 12100 Coors Rd SW"
    )
    expected = Location(
        name="Los Pollos Hermanos Flagship Restaurant",
        code="FR",
        company_id=company.id,
        country="United States",
        region="Southwest",
        city="Albuquerque",
        address="1200 - 12100 Coors Rd SW",
        longitude=35.1046478,
        latitude=-106.6885328,
        type="T",
        status="open",
        comment="Flagship restaurant of Los Pollos Hermanos, from a famous television series"
    )
    apiview = CrudAPIView()
    apiview.model = Location
    apiview.url_lookup = "location_id"
    result = apiview.get(apiview,location_id=5)
    assert result[0] == expected, "Wrong location returned from CrudeAPI view"
    assert result[1] == 200, "Wrong response from CrudeAPI view"


def test_get_not_found_object():
    apiview = CrudAPIView()
    apiview.model = Location
    apiview.url_lookup = "location_id"

    with pytest.raises(werkzeug.exceptions.NotFound):
        apiview.get(apiview,location_id=5)
