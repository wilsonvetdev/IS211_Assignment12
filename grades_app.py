from app import app, db 
from app.models import User, Student, Quiz, Result 

students = Student.query.all()
quizzes = Quiz.query.all()
results = Result.query.all()
users = User.query.all()

all_data = students + quizzes + results + users

for item in all_data:
    db.session.delete(item)

db.session.commit()

u = User(username='admin')
u.set_password('password')
s1 = Student(first_name='Spongebob', last_name='Squarepants')
s2 = Student(first_name='Patrick', last_name='Star')
s3 = Student(first_name='John', last_name='Smith')
q1 = Quiz(subject='Python Basics', num_of_questions=10, date='February 25th, 2021')
q2 = Quiz(subject='Python Intermediate', num_of_questions=15, date='March 29th, 2021')
q3 = Quiz(subject='Advanced SQL', num_of_questions=10, date='April 25th, 2021')
r1 = Result(student=s1, quiz=q1, score=100)
r2 = Result(student=s1, quiz=q2, score=85)
r3 = Result(student=s1, quiz=q3, score=95)

seed = [u, s1, s2, s3, q1, q2, q3]

for item in seed:
    db.session.add(item)

db.session.commit()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Student": Student, "Quiz": Quiz, "Result": Result}



