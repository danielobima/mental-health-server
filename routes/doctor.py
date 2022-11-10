from flask import Flask, request
from flask import Blueprint
from firebase_admin import db
from .models.doctor_model import Doctor

bp = Blueprint('doctor', __name__,url_prefix= '/doctor')


@bp.route("/add_details", methods=['POST'])
def add_details():
    data = request.json['doctor']
    doctor_id = data['doctor_id']
    new_doctor = Doctor(**data)
    db.reference('/doctors/' + doctor_id).set(new_doctor.__dict__)
    return 'success'
