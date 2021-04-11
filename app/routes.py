from app.forms import LoginForm
from flask import render_template
from app import app
from app.forms import LoginForm

@app.route("/")
def index():
    credential = {
        "user": "admin",
        "password": "password"
    }

    return render_template("index.html", title="Home", user=credential)


@app.route("/login")
def login():
    form = LoginForm()
    
    return render_template("login.html", title="Log In", form=form)

# FLASK_APP=grades_app.py FLASK_ENV=development flask run