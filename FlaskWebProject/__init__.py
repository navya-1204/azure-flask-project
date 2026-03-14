"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

# Explicitly setting the static_url_path for Azure compatibility
app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)

# --- UPDATED LOGGING SECTION ---
app.logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
app.logger.addHandler(stream_handler)
# -------------------------------

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views, FlaskWebProject.models
