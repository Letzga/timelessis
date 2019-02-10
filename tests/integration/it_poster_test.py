import unittest

import pytest

from timeless.poster.api import Poster, Authenticated

"""Integration tests for Poster"""


@pytest.mark.skip(
    reason="Authentication mechanism (Authenticated#auth()) is not yet implemented!"
)
def test_auth():
    assert Authenticated(
        clientid="$0m3C1i3ntId"
    ).access_token(), "Poster did not authenticate the user!"

