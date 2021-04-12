from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")


class AddStudentForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    submit = SubmitField("Add Student")

class AddQuizForm(FlaskForm):
    subject = StringField("Subject", validators=[DataRequired()])
    num_of_questions = StringField("Number of Questions", validators=[DataRequired()])
    date = StringField("Date", validators=[DataRequired()])
    submit = SubmitField("Add Quiz")