from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.database import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_check):
        user = User.query.filter_by(username=username_check.data).first()
        if user:
            raise ValidationError('Username already exists! Try Again')
    
    def validate_email(self, email_check):
        user = User.query.filter_by(email=email_check.data).first()
        if user:
            raise ValidationError('email already exists! Try Again')

    username = StringField(label="Username",validators=[DataRequired()])
    email = StringField(label = "Email",validators=[DataRequired()])
    password = PasswordField(label="Password",validators=[DataRequired()])
    phone = StringField(label="Mobile Number",validators=[DataRequired()])

    name = StringField(label = "Name",validators=[DataRequired()])
    education = StringField(label = "Class",validators=[DataRequired()])
    field = StringField(label = "Area of Interest",validators=[DataRequired()])
    project = StringField(label = "Projects/Work",validators=[DataRequired()])

    submit = SubmitField(label="Submit",validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField(label="Username")
    password = PasswordField(label="Password")
    submit = SubmitField(label="Submit")