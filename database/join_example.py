import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT        
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT,
        student_id INTEGER,
        FOREIGN KEY(student_id) REFERENCE students(student_id)
    )
''')

cursor.execute("INSERT INTO students (name) VALUES ('Alice')")
cursor.execute("INSERT INTO students (name) VALUES ('Bob')")

cursor.execute("INSERT INTO courses ( course_name, student_id) VALUES ('math', 1)")
cursor.execute("INSERT INTO courses ( course_name, student_id) VALUES ('science', 1)")
cursor.execute("INSERT INTO courses ( course_name, student_id) VALUES ('art', 2)")

conn.commit()

cursor.execute('''
    SELECT student.name, courses.course_name from students
    JOIN courses on students.student_id = courses_id
''')

rows = cursor.fetchall()

from row in rows:
    print(f"Student: {row[0]}, Course: {row[1]}")

conn.close()
