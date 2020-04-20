from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    #password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Continue')

class AnswerForm(FlaskForm):
    userAnswer = StringField("Your answer goes here:", validators=[DataRequired()])
    submitAnswer = SubmitField("Check")
