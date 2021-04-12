from app.forms import LoginForm
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route("/index")
def index():
    credential = {
        "user": "admin",
        "password": "password"
    }

    return render_template("index.html", title="Home", user=credential)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return render_template("/dashboard.html")

    return render_template("login.html", title="Log In", form=form)
    


# FLASK_APP=grades_app.py FLASK_ENV=development flask run
# FLASK_APP=grades_app.py FLASK_ENV=development flask db init
# FLASK_APP=grades_app.py FLASK_ENV=development flask shell