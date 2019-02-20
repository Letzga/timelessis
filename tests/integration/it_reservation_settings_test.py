"""
@todo #291:30min Enable all tests below when then functionality in for
 ReservationSettings will be enabled. There will be tuning needed because there
 are no endpoint names in the views.
"""
import datetime
from http import HTTPStatus

import pytest
from flask import url_for

from timeless.reservations import models


@pytest.mark.skip
def test_list(client):
    data = reservation_data("nicer comment here")
    client.post(url_for("reservations.settings_create"), data=data)
    response = client.get(url_for("reservations.settings_list"))
    assert response.status_code == HTTPStatus.OK
    html = response.data.decode('utf-8')
    assert html.count(data["num_of_persons"]) == 1
    assert html.count(data["comment"]) == 1


@pytest.mark.skip
def test_create(client):
    data = reservation_data("nice comment here")
    response = client.post(url_for("reservations.settings_create"), data=data)
    assert response.status_code == HTTPStatus.FOUND
    assert response.location.endswith(url_for("reservations.settings_list"))


@pytest.mark.skip
def test_edit(client):
    data = reservation_data("nicer comment here")
    new_data = reservation_data("different comment here")
    client.post(url_for("reservations.settings_create"), data=data)
    identifier = models.ReservationSettings.query.first().id
    client.post(
        url_for("reservations.settings_create", id=identifier), data=new_data
    )
    response = client.get(url_for("reservations.settings_list"))
    assert response.status_code == HTTPStatus.OK
    html = response.data.decode('utf-8')
    assert html.count(data["num_of_persons"]) == 1
    assert html.count(data["comment"]) == 0
    assert html.count(new_data["comment"]) == 1


@pytest.mark.skip
def test_delete(client):
    assert client.get(
        url_for("reservations.settings_delete", id=1)
    ).status_code == HTTPStatus.OK
    data = reservation_data("my very unique comment")
    client.post(url_for("reservations.settings_create"), data=data)
    identifier = models.ReservationSettings.query.first().id
    client.post(
        url_for("reservations.settings_delete"),
        data={"id": identifier}
    )
    response = client.get(url_for("reservations.settings_list"))
    assert response.status_code == HTTPStatus.OK
    html = response.data.decode('utf-8')
    assert html.count(data["num_of_persons"]) == 0
    assert html.count(data["comment"]) == 0


def reservation_data(comment):
    data = {
        "start_time": datetime.datetime.now(),
        "end_time": datetime.datetime.now() + datetime.timedelta(hours=1),
        "customer_id": 1,
        "num_of_persons": 932,
        "comment": comment,
        "status": "on",
        "multiple": True,
        "tables": 1
    }
    return data
