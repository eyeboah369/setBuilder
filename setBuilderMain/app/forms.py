from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

#built in forms that Flask provides for users to use
class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    #password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Continue')

#input form for the user to pass in data to the application
class AnswerForm(FlaskForm):
    userAnswer = StringField("Your answer goes here:", validators=[DataRequired()])
    submitAnswer = SubmitField("Check")
