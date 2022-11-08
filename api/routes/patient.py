from flask import Flask, request
from flask import Blueprint
from firebase_admin import db
from .models.patient_model import Patient

bp = Blueprint('patient', __name__, url_prefix='/patient')


@bp.route("/add_details", methods=['POST'])
def add_details():
    data = request.json['patient']
    patient_id = data['patient_id']
    new_patient = Patient(**data)
    db.reference('/patients/' + patient_id).set(new_patient.__dict__)
    return 'success'


@bp.route('/get_doctors', methods=['GET'])
def get_doctors():
    # TODO: Check patient preferences and location before returning doctors
    # patient_id = request.args.get('patient_id')
    return db.reference('/doctors').get()


