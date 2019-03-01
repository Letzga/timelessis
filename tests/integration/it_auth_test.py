from datetime import datetime
from http import HTTPStatus
import pytest

import flask

from timeless.auth.auth import login, hash as auth_hash
from timeless.employees.models import Employee

"""
    Unit test for authentication related poster accesses.
"""


def test_incorrect_username(db_session):
    """Do not remove db_session dependency. It is injected
    in order to trigger db migration.
    """
    assert (login("unknown", "unknown") == "login.failed")


def test_incorrect_password(db_session):
    employee = Employee(first_name="Alice", last_name="Cooper",
                        username="vgv", phone_number="1", account_status="A",
                        birth_date=datetime.utcnow(), pin_code=4567,
                        registration_date=datetime.utcnow(), user_status="U",
                        email="test@test.com", password="pass")
    db_session.add(employee)
    db_session.commit()
    assert (login("unknown", "unknown") == "login.failed")


def test_login(db_session):
    employee = Employee(first_name="Alice", last_name="Cooper",
                        username="vgv", phone_number="1", account_status="A",
                        birth_date=datetime.utcnow(), pin_code=4567,
                        registration_date=datetime.utcnow(), user_status="U",
                        email="test@test.com", password=auth_hash("pass"))
    db_session.add(employee)
    db_session.commit()
    error = login("vgv", "pass")
    assert not error
    assert flask.session['user_id'] == employee.id


def test_forgot_password(client):
    response = client.get("/auth/forgotpassword")
    decoded = response.data.decode("utf-8")
    assert "<h1>Forgot password</h1>" in decoded
    assert "<label for=\"email\">E-mail</label>" in decoded
    assert "<input name=\"email\" id=\"email\" required>" in decoded
    assert "<input type=\"submit\" value=\"Forgot my password\">" in decoded
    assert response.status_code == 200


def test_activate(client):
    assert client.get("/auth/activate").status_code == 405
    response = client.post("/auth/activate")
    decoded_response = response.data.decode("utf-8")
    assert response.status_code == 200
    assert "<h1>You are not logged in</h1>" in decoded_response
    assert "Successfully activated your account." not in decoded_response


"""
    @todo #370:30min Forgot password routine. At the moment we are showing the
     e-mail from which we sent the new password link at the forgot_password_post 
     page. We should mask this e-mail somehow (like p******o@gmail.com) so 
     just the user get a hint to where the email was sent. After implementing 
     the masking correct it in the test below
    @todo #370:30min Forgot password routine. Create a forgot password logic: 
     create an random password, change it for the user with the received e-mail 
     and send it to the e-mail. Then cover the implementation with tests
"""


@pytest.mark.skip(reason="Can't inject mock user base")
def test_forgot_password_post(client):
    email = "test@mail.com"
    response = client.post(flask.url_for("auth.forgot_password"), data={
        "email": email
    })
    decoded = response.data.decode("utf-8")
    assert "<h1>Forgot password</h1>" in decoded
    assert (
        f"We've sent an e-mail to {email} with your new password."
        in decoded
    )
    assert "Please use it to log in and change it." in decoded
    assert response.status_code == HTTPStatus.OK
