class Session:
    def __init__(self, session_id, date, meeting_type, date_created, duration, location, doctor_id, patient_id,
                 payment_method, desc, category):
        self.session_id = session_id
        self.date = date
        self.meeting_type = meeting_type
        self.duration = duration
        self.location = location
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.payment_method = payment_method
        self.desc = desc
        self.category = category
        self.date_created = date_created
