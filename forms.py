from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class SignupForm(FlaskForm):
    name = StringField("Username")
    email = StringField("Email")
    password = StringField("Password")
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    submit = SubmitField("Submit")
