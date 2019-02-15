"""File for models in customer module"""
from datetime import datetime
from timeless import DB
from timeless.poster.models import PosterSyncMixin
from timeless.models import validate_required


class Customer(PosterSyncMixin, DB.Model):
    """Model for customer business entity.
    @todo #102:30min Set up celery to project which will provide async
     jobs. Docs is here - http://flask.pocoo.org/docs/1.0/patterns/celery/
     Create celery task for customer synchronization.
    """
    __tablename__ = "customers"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    first_name = DB.Column(DB.String, nullable=False)
    last_name = DB.Column(DB.String, nullable=False)
    phone_number = DB.Column(DB.String, nullable=False)
    created_on = DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    updated_on = DB.Column(DB.DateTime, onupdate=datetime.utcnow)

    @validate_required("first_name", "last_name", "phone_number", "created_on")

    def __init__(self, **kwargs):
        super(Customer, self).__init__(**kwargs)
        self.first_name = "Customer First Name"
        self.last_name = "Customer Last Name"
        self.phone_number = "99 9999-9999"
        self.created_on = datetime.utcnow()

    def __repr__(self):
        return "<Customer(name=%s %s)>" % (self.first_name, self.last_name)
