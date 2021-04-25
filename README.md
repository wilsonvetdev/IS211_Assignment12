# IS211_Assignment12

### Dependencies and Requirements:
* Python 3.9.1
* pip
* flask
* flask-wtf
* flask-sqlalchemy
* flask-migrate
* flask-login



### Setup - Python 3.9.1

1. Git clone this repository onto local environment
2. cd into the repo
  * Run below command to ensure Python 3 environment, and not the Python that comes installed with your local machine.
  * $ python3 -m venv env
  * $ source env/bin/activate
  * $ pip install -r requirements.txt
3. run in CLI - $ FLASK_APP=grades_app.py FLASK_ENV=development flask run
4. visit http://127.0.0.1:5000/ on your browser
5. Please use <b>username: admin</b> and <b>password: password</b> to log in and test functionalities of the app.