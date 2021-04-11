from app import app

@app.route('/')
def index():
    return 'Hellow, World!'


# FLASK_APP=grades_app.py FLASK_ENV=development flask run