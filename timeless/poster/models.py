"""File for models in poster module"""
from timeless import DB


class PosterSyncMixin(object):
    """Mixin with fields needed for data synchronization with Poster.
    """
    poster_id = DB.Column(DB.Integer)
    synchronized_on = DB.Column(DB.DateTime)
