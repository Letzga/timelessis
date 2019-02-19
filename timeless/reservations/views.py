""" Views for reservations """
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from timeless import views
from timeless.access_control.views import SecuredView
from timeless.restaurants.tables import forms
from timeless.reservations import models


bp = Blueprint("reservations", __name__, url_prefix="/reservations")


class SettingsList(views.ListView):
    """
    List view set for Reservation Settings
    @todo #186:30min For SettingsListView, SettingsCreateView,
     SettingsDetailView, SettingsDeleteView create correct templates
     for list, create/detail actions. When templates will be done, pls change
     `template_name` value in every View Class.
    @todo #173:30min Refactor (and uncomment) views below to use new
     base views once when they are avaiable. Current implementation is not
     generic enough.
    """
    model = models.ReservationSettings
    template_name = "restaurants/tables/list.html"


SettingsList.register(bp, "/settings/")

# class SettingsCreateUpdateView(views.CreateUpdateView):
#     """ Reservation settings create view """
#     template_name = "restaurants/tables/create_edit.html"
#     success_url_name = "reservation_settings_list"
#     form = forms.TableForm
#     model = models.ReservationSettings


# class SettingsDetailView(views.DetailView):
#     """ Reservation settings detail view"""
#     model = models.ReservationSettings
#     template_name = "restaurants/tables/create_edit.html"
#     success_url_name = "reservation_settings_list"
#     not_found_url_name = "reservation_settings_list"


# class SettingsDeleteView(views.DeleteView):
#     success_url_name = "reservation_settings_list"


class CommentView(SecuredView, views.CrudAPIView):
    """API Resource for comments /api/comments

    """
    model = models.Comment
    url_lookup = "comment_id"
    list_reservations = "reservation_comment"


@bp.route("/")
def list_reservations(reservations):
    """
        @todo #172:30min Refactor this after the implementation of GenericViews.
         Take a look at puzzles #134 and #173 where the requirements of generic
         views are described. Don't forget to cover the generated code with
         tests

    :param reservations:
    :return:
    """
    flash("List not yet implemented")
    return render_template(
        "restaurants/tables/list.html", reservations=reservations
    )


@bp.route("/create", methods=("GET", "POST"))
def create(reservation):
    if request.method == "POST":
        flash("Create not yet implemented")

    return render_template(
        "restaurants/tables/create_edit.html", action="create",
        reservation=reservation
    )


@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        flash("Edit not yet implemented")
    return render_template(
        "restaurants/tables/create_edit.html", action="edit",
        id=id
    )


@bp.route("/delete", methods=["POST"])
def delete():
    flash("Delete not yet implemented")
    return redirect(url_for("reservations.list_reservations"))
