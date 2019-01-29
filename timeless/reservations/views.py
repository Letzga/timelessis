from flask import Blueprint


bp = Blueprint('reservations', __name__, url_prefix='/reservations')


@bp.route('/settings')
def base():
    """
    @todo #32:30min Continue implementing Settings page for Reservations, it will be deployed on a different subdomain
    """
    return 'Settings API entry point'
