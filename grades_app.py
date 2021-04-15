from app import app, db 
from app.models import User, Student, Quiz, Result 

students = Student.query.all()
quizzes = Quiz.query.all()
results = Result.query.all()

all_data = students + quizzes + results 

for item in all_data:
    db.session.delete(item)

db.session.commit()

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Student": Student, "Quiz": Quiz, "Result": Result}

    

