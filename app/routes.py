from app.forms import LoginForm, AddStudentForm, AddQuizForm
from flask import render_template, flash, redirect, url_for
from app import app
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

@app.route("/index")
@login_required
def index():

    return render_template("index.html", title="Home")


@app.route("/student/add", methods=['GET', 'POST'])
def add_student():

    add_student_form = AddStudentForm()

    return render_template("add_student.html", title="Add Student", add_student_form=add_student_form)


@app.route("/quiz/add", methods=['GET', 'POST'])
def add_quiz():

    add_quiz_form = AddQuizForm()

    return render_template("add_quiz.html", title="Add Quiz", add_quiz_form=add_quiz_form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for("login"))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', title='Log In', form=form)
    

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

# FLASK_APP=grades_app.py FLASK_ENV=development flask run
# FLASK_APP=grades_app.py FLASK_ENV=development flask db init
# FLASK_APP=grades_app.py FLASK_ENV=development flask shell