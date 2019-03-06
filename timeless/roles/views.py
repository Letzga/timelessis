"""roles views module.
@todo #255:30min Continue implementing edit() method,
 using SQLAlchemy and Location model. In the index page it
 should be possible to sort and filter for every column. Location management
 page should be accessed by the Location page. Update html templates when
 methods are implemented. Create more tests for edit() route.
 Remember not to use DB layer directly. Please refer to
 timeless/companies/views.py as an example on how routes
 should be implemented.
"""
from http import HTTPStatus

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for,
    abort)

from timeless import views
from timeless.roles.forms import RoleForm
from timeless.roles.models import Role


BP = Blueprint("role", __name__, url_prefix="/roles")


class RoleListView(views.ListView):
    """ List the tables """
    model = Role
    template_name = "roles/list.html"


RoleListView.register(BP, "/")


@BP.route("/create", methods=("GET", "POST"))
def create():
    """ Create new table shape"""
    form = RoleForm(request.form)
    if request.method == "POST" and form.validate():
        form.save()
        return redirect(url_for("role.list_roles"))
    return render_template(
        "roles/create_edit.html", form=form)


@BP.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    """
    Role edit route
    :param id: Role id
    :return: Current role edit view
    """
    if request.method == "POST":
        table = Role.query.get(id)
        if not table:
            return abort(HTTPStatus.NOT_FOUND)
        flash("Edit not yet implemented")
    action = "edit"
    companies = [
        {"id": 1, "name": "Foo Inc.", "selected": False},
        {"id": 3, "name": "Foomatic Co.", "selected": True},
    ]
    return render_template(
        "roles/create_edit.html", action=action,
        companies=companies
    )


@BP.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    """
    Role delete route
    :param id: Role id
    :return: List roles view
    """
    roles = Role.query.get(id)
    if not roles:
        return abort(HTTPStatus.NOT_FOUND)
    Role.query.filter_by(id=id).delete()
    return redirect(url_for("role.list_roles"))
