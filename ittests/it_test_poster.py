import unittest
from timeless.poster.api import Poster, Authenticated

"""Integration tests for Poster"""


class PosterITTests(unittest.TestCase):

    """
    @todo #67:30min Implement auth process for Poster API.
     client_id is required for authentication process, this id is the public key
     provided by the poster service to identify the applications
    """

    @unittest.skip("poster.auth not implemented yet")
    def test_auth(self):
        assert Authenticated(clientid="$0m3C1i3ntId").token() != "", "Poster did not authenticated user"
