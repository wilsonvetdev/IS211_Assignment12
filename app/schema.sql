CREATE TABLE students (
    id INTEGER PRIMARY KEY ASC,
    first_name TEXT,
    last_name TEXT
);

CREATE TABLE quizzes (
    id INTEGER PRIMARY KEY ASC,
    subject TEXT,
    num_of_questions INTEGER,
    date TEXT
);

CREATE TABLE results (
    id INTEGER PRIMARY KEY ASC,
    student_id INTEGER,
    quiz_id INTEGER,
    score INTEGER,
);