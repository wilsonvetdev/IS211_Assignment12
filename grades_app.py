from app import app, db 
from app.models import User, Student, Quiz, Result 

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Student": Student, "Quiz": Quiz, "Result": Result}

    

