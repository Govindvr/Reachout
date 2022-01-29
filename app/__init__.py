from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '3de5c18805c57febf0607ae1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from app import routes