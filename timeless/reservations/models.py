"""File for models in reservations module"""
from timeless.models import TimestampMixin
from timeless import DB


class ReservationSettings(TimestampMixin, DB.Model):
    """Settings model for Reservations"""

    __tablename__ = "reservation_settings"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.String, unique=True)
    default_duration = DB.Column(DB.SmallInteger)
    default_deposit = DB.Column(DB.SmallInteger)
    sms_notifications = DB.Column(DB.Boolean)
    threshold_sms_time = DB.Column(DB.SmallInteger)
    greeting_by_time = DB.Column(DB.JSON)
    sex = DB.Column(DB.String)
