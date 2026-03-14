"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# --- UPDATED LOGGING SECTION ---
# This tells Flask to capture "INFO" level messages (like successful logins)
app.logger.setLevel(logging.INFO)

# This handler redirects the logs to the terminal/console so Azure Log Stream can see them
stream_handler = logging.StreamHandler()
app.logger.addHandler(stream_handler)
# -------------------------------

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
