import flask

from timeless.access_control.methods import Method
from timeless.restaurants.models import Location

"""
    @todo #242:30min Implement owner privileges regarding company. Owner 
     should be able to operate over employees of his own company only. Implement
     this rules on __employee_access and then uncomment test from 
     owner_privileges.py:test_can_not_manage_employees_from_different_company
"""
def has_privilege(method=None, resource=None, *args, **kwargs) -> bool:
    """Check if user with Owner role can access a particular resource."""
    return __resources.get(resource, lambda *arg: False)(method, *args, **kwargs)


def __location_access(method=None, *args, **kwargs):
    user_company = flask.g.get("user").company_id
    location_company = Location.query.get(kwargs.get("id")).company_id
    return user_company == location_company


def __employee_access(method=None, *args, **kwargs):
    permitted, user = False, flask.g.get("user")
    employee_id = kwargs.get("employee_id")
    if method == Method.READ and user:
        if employee_id:
            permitted = employee_id == user.id
        else:
            permitted = True
    return permitted


__resources = {
    "location": __location_access,
    "employee": __employee_access,
    "companies": __employee_access,
    "reservation_settings": __employee_access,
    "reservation_comment": __employee_access
}
