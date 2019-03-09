from http import HTTPStatus

from flask import url_for

import pytest
from tests import factories
from timeless.restaurants.models import Reservation


def test_list(client):
    reservation = factories.ReservationFactory()
    response = client.get(url_for("reservations.list"))
    assert response.status_code == HTTPStatus.OK
    html = response.data.decode("utf-8")
    assert reservation.comment in html
    assert html.count(reservation.comment) == 1


def test_create(client):
    reservation = factories.ReservationFactory.get_dict()
    url = url_for("reservations.create")
    response = client.post(url, data=reservation)
    assert response.status_code == HTTPStatus.FOUND
    assert Reservation.query.count() == 1


def test_edit(client):
    reservation_original = factories.ReservationFactory()
    reservation_edited = factories.ReservationFactory.get_dict()
    url = url_for("reservations.edit", id=reservation_original.id)
    response = client.post(url, data=reservation_edited)
    assert response.status_code == HTTPStatus.FOUND
    reservation = Reservation.query.get(reservation_original.id)
    assert reservation.comment == reservation_edited["comment"]


def test_delete(client):
    reservation = factories.ReservationFactory()
    url = url_for("reservations.delete", id=reservation.id)
    response = client.post(url)
    assert response.location.endswith(url_for("reservations.list"))
    assert Reservation.query.filter_by(id=reservation.id).count() == 0
