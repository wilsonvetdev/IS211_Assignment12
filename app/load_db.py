
import sqlite3 as lite 

students = (
    (1, 'James', 'Smith'),
    (2, 'Diana', 'Greene'),
    (3, 'Sara', 'White'),
    (4, 'William', 'Gibson')
)

quizzes = ( 
    (1, 'Python Basics', 10, '2021-02-15'),
    (2, 'SQL Basics', 10, '2021-02-15')
)

results = (
    (1, 1, 1, 100),
    (2, 2, 1, 100),
    (3, 3, 2, 100),
    (4, 4, 2, 80),
)

if __name__ == '__main__':

    con = lite.connect('hw12.db')

    with con:
        cur = con.cursor()

        cur.executescript('''
        DROP TABLE IF EXISTS students;
        DROP TABLE IF EXISTS quizzes;
        DROP TABLE IF EXISTS results;
        CREATE TABLE students(id INTEGER PRIMARY KEY ASC, first_name TEXT, last_name TEXT);
        CREATE TABLE quizzes(id INTEGER PRIMARY KEY ASC, subject TEXT, num_of_questions INTEGER, date TEXT);
        CREATE TABLE results(id INTEGER PRIMARY KEY ASC, student_id INTEGER, quiz_id INTEGER, score INTEGER);
        ''')

        cur.executemany('INSERT INTO students VALUES(?, ?, ?)', students)
        cur.executemany('INSERT INTO quizzes VALUES(?, ?, ?, ?)', quizzes)
        cur.executemany('INSERT INTO results VALUES(?, ?, ?, ?)', results)