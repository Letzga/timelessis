import datetime
import pytest
import werkzeug
from http import HTTPStatus
from timeless.reservations.views import CommentView
from timeless.reservations.views import Comment

"""
    Tests for CommentView
    @todo #222:30min Finish CommentView implementation and CommentView tests. 
     Methods for GET, POST and DELETE operation must be implemented, after the 
     implementation remove the skip annotations from these tests.

"""


def test_get_found_comment():
    commentview = CommentView()
    expected = Comment(
        id=1,
        employee_id=2,
        body="Comments for GET method",
        date=datetime.utcnow
    )
    result = commentview.get(commentview, comment_id=5)
    assert result[0] == expected, "Wrong comment returned from CommentView"
    assert result[1] == HTTPStatus.OK, "Wrong status returned from CommentView"


def test_get_not_found_comment():
    commentview = CommentView()

    with pytest.raises(werkzeug.exceptions.NotFound):
        result = commentview.get(commentview, comment_id=5)


@pytest.mark.skip
def test_post_found(self):
    commentview = CommentView()
    expected = Comment(
        id=1,
        employee_id=2,
        body="Comments for POST method",
        date=datetime.utcnow
    )
    result = commentview.post(commentview, comment_id=5)
    assert result[0] == expected, "Wrong comment returned from CommentView"
    assert result[1] == HTTPStatus.OK, "Wrong status returned from CommentView"


def test_post_not_found_comment():
    commentview = CommentView()

    with pytest.raises(werkzeug.exceptions.NotFound):
        result = commentview.post(commentview, comment_id=5)



def test_delete_found():
    commentview = CommentView()
    expected = Comment(
        id=1,
        employee_id=2,
        body="Comments for DELETE method",
        date=datetime.utcnow
    )
    result = commentview.delete(commentview, comment_id=5)
    assert result[1] == HTTPStatus.NO_CONTENT, "Wrong status returned from CommentView"


def test_delete_not_found():
    commentview = CommentView()
    result = commentview.delete(commentview, comment_id=5)
    with pytest.raises(werkzeug.exceptions.NotFound):
        result = commentview.post(commentview, comment_id=5)


def test_put_comment():
    commentview = CommentView()
    expected = Comment(
        id=1,
        employee_id=2,
        body="Comments for PUT method",
        date=datetime.utcnow
    )
    result = commentview.put(commentview)
    assert result[0] == expected, "Wrong comment returned from CommentView"
    assert result[1] == HTTPStatus.OK, "Wrong status returned from CommentView"


def test_put_found_comment():
    commentview = CommentView()
    original = Comment(
        id=1,
        employee_id=2,
        body="Comments for PUT method that does not exists",
        date=datetime.utcnow
    )
    commentview.put(commentview)
    altered = Comment(
        id=1,
        employee_id=2,
        body="Comments for PUT method that does not exists",
        date=datetime.utcnow
    )
    result = commentview.put(commentview)
    assert result[0] == altered, "Wrong comment returned from CommentView"
    assert result[1] == HTTPStatus.OK, "Wrong status returned from CommentView"
