import flask

from timeless.employees.models import Employee


def has_privilege(method=None, resource=None, *args, **kwargs) -> bool:
    """Check if user with Director role can access a particular resource."""
    return __resources.get(resource, lambda *arg: False)(
        method, *args, **kwargs
    )


def __employee_access(method=None, *args, **kwargs):
    permitted, user = False, flask.g.get("user")
    employee_id = kwargs.get("employee_id")
    if user:
        if employee_id:
            permitted = check_rights(method, employee_id, user)
        else:
            permitted = True
    return permitted


def check_rights(method, employee_id, user):
    """
    Check the rights a director has over an employee profile.
    In principle, a director can access their own profile and the
    profile of the employees with a lower role, who work at the same company.
    """
    if employee_id == user.id:
        return True
    else:
        other = Employee.query.get(employee_id)
        return user.company_id == other.company_id and user.role.is_director()


__resources = {
    "employee": __employee_access
}
