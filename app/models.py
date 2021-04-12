from app import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}> - instance of class User.' 

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    results = db.relationship("Result", backref="student", lazy="dynamic")

    def __repr__(self):
        return f'<Student {self.first_name} {self.last_name} - instance of class Student>'

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(32), index=True)
    num_of_questions = db.Column(db.Integer)
    date = db.Column(db.String(64))
    results = db.relationship("Result", backref="quiz", lazy="dynamic")
    
    def __repr__(self):
        return f'<Quiz instance - subject:{self.subject}, num_of_questions:{self.num_of_questions}, date:{self.date}>'

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    quiz_id = db.Column(db.Integer, db.ForeignKey("quiz.id"))
    score = db.Column(db.Integer)

    def __repr__(self):
        return f'<Result instance>'