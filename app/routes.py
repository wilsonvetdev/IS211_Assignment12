from app.forms import AddResultForm, LoginForm, AddStudentForm, AddQuizForm
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Student, Quiz, Result


@app.route("/")
@app.route("/index")
@login_required
def index():

    students = Student.query.all()
    quizzes = Quiz.query.all()

    return render_template("index.html", title="Home", students=students, quizzes=quizzes)


@app.route("/student/<student_id>")
@login_required
def student_results(student_id):
    
    student = Student.query.get(student_id)

    return render_template("student_results.html", student=student)


@app.route("/student/add", methods=['GET', 'POST'])
@login_required
def add_student():

    add_student_form = AddStudentForm()

    if add_student_form.validate_on_submit():
        student = Student(first_name=add_student_form.first_name.data, last_name=add_student_form.last_name.data)
        db.session.add(student)
        db.session.commit()
        flash("You successfully added a new student!")
        return redirect(url_for("index"))

    return render_template("add_student.html", title="Add Student", add_student_form=add_student_form)


@app.route("/quiz/add", methods=['GET', 'POST'])
@login_required
def add_quiz():

    add_quiz_form = AddQuizForm()

    if add_quiz_form.validate_on_submit():
        quiz = Quiz(
            subject=add_quiz_form.subject.data, 
            num_of_questions=add_quiz_form.num_of_questions.data, 
            date=add_quiz_form.date.data)
        db.session.add(quiz)
        db.session.commit()
        flash("You successfully added a new quiz!")
        return redirect(url_for("index"))

    return render_template("add_quiz.html", title="Add Quiz", add_quiz_form=add_quiz_form)


@app.route("/result/add", methods=['GET', 'POST'])
@login_required
def add_result():
    
    add_result_form = AddResultForm()
    add_result_form.students.choices = [(student.id, student.get_fullname()) for student in Student.query.order_by('id')]
    add_result_form.quizzes.choices = [(quiz.id, quiz.get_quiz_info()) for quiz in Quiz.query.order_by('id')]

    if add_result_form.validate_on_submit():
        student_instance = Student.query.get(add_result_form.students.data)
        quiz_instance = Quiz.query.get(add_result_form.quizzes.data)
        score = int(add_result_form.score.data)
        new_result = Result(
            student = student_instance,
            quiz = quiz_instance,
            score = score
        )
        db.session.add(new_result)
        db.session.commit()
        flash(f"You successfully added a new quiz result for {student_instance.get_fullname()}! Go to the student's page to view their results.")
        return redirect(url_for("add_result"))


    return render_template(
        "add_result.html", 
        title="Add Result", 
        add_result_form=add_result_form
    )


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