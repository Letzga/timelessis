"""TableShape views module."""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from timeless.db import DB
from timeless.restaurants import models
from timeless.restaurants.table_shapes import forms
from timeless.templates.views import order_by

bp = Blueprint("table_shape", __name__, url_prefix="/table_shapes")


@bp.route("/")
def list():
    """List all table shapes
    @todo #203:30min Implement filtering of TableShape model for
     all columns. Update html templates if its needed. Do not forget
     to write tests.
    """
    order_fields = request.args.getlist("order_by")
    query = models.TableShape.query
    if order_fields:
        query = order_by(query, order_fields)
    return render_template(
        "restaurants/table_shapes/list.html",
        table_shapes=query.all())


@bp.route("/create", methods=("GET", "POST"))
def create():
    """ Create new table shape"""
    form = forms.TableShapeForm(request.form)

    if request.method == "POST" and form.validate():
        """
        @todo #162:30min Initialize CSRF token protection for app and add
         token to this template. Implementation detail you can find by the
         following page: https://flask-wtf.readthedocs.io/en/stable/csrf.html
        @todo #162:30min This form currenly cannot save pictures. Need have a
         look how WTF form processes files. Implement generic solution to use
         it everywhere when it's needed.
        """
        """
        Uncomment after correction
        form.save()
        """
        return redirect(url_for("table_shape.list"))
    return render_template(
        "restaurants/table_shapes/create_edit.html", form=form)


@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    """ Edit table shape with id
    @todo #162:30min Implement edit() method of TableShape model and
     update template. Use TableShapeForm for that, see how in works in
     create function. Check and update html template if it's needed.
    """
    if request.method == "POST":
        flash("Edit not yet implemented")

    form = forms.TableShapeForm()
    return render_template(
        "restaurants/table_shapes/create_edit.html", form=form)


@bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    """ Delete table shape with id """
    table_shape = models.TableShape.query.get(id)
    DB.session.delete(table_shape)
    return redirect(url_for("table_shape.list"))
