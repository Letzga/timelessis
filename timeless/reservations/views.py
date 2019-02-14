""" Views for reservations """
from datetime import datetime

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, jsonify
)
from http import HTTPStatus
from flask import views

from timeless.reservations.controllers import SettingsController
from timeless.reservations.models import Comment
from timeless.views import CrudAPIView


bp = Blueprint("reservations", __name__, url_prefix="/reservations")


class SettingsView(views.MethodView):
    """ Reservation settings API """
    ctr = SettingsController()

    def get(self, id):
        """ GET method for reservation settings """
        if id:
            return self.ctr.get_settings_for_reservation(id), HTTPStatus.OK
        return self.ctr.get_all_reservation_settings(), HTTPStatus.OK

    def post(self):
        """ POST method for reservation settings """
        return self.ctr.create_settings_for_reservation(self), HTTPStatus.CREATED

    def put(self, id):
        """ PUT method for reservation settings """
        return self.ctr.update_reservation_settings(self, id), HTTPStatus.OK

    def delete(self, id):
        """ DELETE method for reservation settings """
        return self.ctr.delete_reservation_settings(id), HTTPStatus.NO_CONTENT


class CommentView(CrudAPIView):
    """API Resource for comments /api/comments
    @todo #123:30min After CrudView implementation is finished
     create necessary templates for the CommentView to operate on.
     See CrudAPIView description for more details about its usage.
    """
    model = Comment
    url_lookup = "comment_id"

    def post(self):
        """Post method of CommentView"""
        return "Post method of CommentViewSet", HTTPStatus.CREATED

    def put(self, comment_id):
        """Put method of CommentView"""
        if comment_id:
            return "Detail put method of CommentViewSet", HTTPStatus.OK
        return "Put method of CommentViewSet", HTTPStatus.OK

    def delete(self, comment_id):
        """Delete method of CommentView"""
        if comment_id:
            return "Detail delete method of CommentViewSet", HTTPStatus.NO_CONTENT
        return "Delete method of CommentViewSet", HTTPStatus.NO_CONTENT


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

@bp.route("/retrieve", methods=("GET", "POST"))
def retrieve_reservations():
    """Retrieve reservations based on login, location, and date.
        @todo #28:30min Implement actual fetching of reservations. We need to
         return a JSON list, filtered by reservations based on location and
         date. We also need to password protect this API, and filter only
         those belonging to the specific company,
    """
    reservations_json = {
        "1": {
            "start_time" : datetime(1, 1, 1),
            "end_time" : datetime(1, 1, 1),
            "customer_id" : 1,
            "num_of_persons" : 1,
            "comment" : "Test",
            "status" : 2
        }
    }
    return jsonify(reservations_json)

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
