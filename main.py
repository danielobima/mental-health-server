from flask import Flask
import os
from flask_cors import CORS
import re
import firebase_admin
from firebase_admin import credentials
from routes import *

app = Flask(__name__)
CORS(app)

priv_key = re.sub(r'\\n', '\n', os.environ.get("FB_PRIVATE_KEY"))
cred = credentials.Certificate(
    {
        "type": "service_account",
        "project_id": os.environ.get("FB_PROJECT_ID"),
        "client_email": os.environ.get("FB_CLIENT_EMAIL"),
        "token_uri": os.environ.get("FB_TOKEN_URI"),
        "private_key": priv_key
    }
)
firebase_admin.initialize_app(
    cred, {"databaseURL": os.environ.get("FB_DATABASE_URL")}
)
app.register_blueprint(hello.bp)
app.register_blueprint(users.bp)
app.register_blueprint(session.bp)
app.register_blueprint(patient.bp)
app.register_blueprint(doctor.bp)

print(os.environ.get("PORT"))


if __name__ == '__main__':
    app.run()
