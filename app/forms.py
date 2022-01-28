from dataclasses import field
from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label="Username")
    email = StringField(label = "Email")
    password = PasswordField(label="Password")
    phone = StringField(label="Mobile Number")

    name = StringField(label = "Name")
    education = StringField(label = "Class")
    field = StringField(label = "Area of Interest")
    project = StringField(label = "Projects/Work")

    submit = SubmitField(label="Submit")