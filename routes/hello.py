from flask import Blueprint
from firebase_admin import db

bp = Blueprint('hello', __name__)


@bp.route('/')
def hi():
    return 'hi'
