import sqlite3

def perform_crud():
    connection = sqlite3.connect("assignment.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, marks INTEGER)")
    cursor.execute("DELETE FROM students")
    cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Pratik", 85))
    cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Rahul", 90))
    cursor.execute("SELECT * FROM students")
    print(cursor.fetchall())
    cursor.execute("UPDATE students SET marks = ? WHERE name = ?", (95, "Pratik"))
    cursor.execute("DELETE FROM students WHERE name = ?", ("Rahul",))
    cursor.execute("SELECT * FROM students")
    print(cursor.fetchall())
    connection.commit()
    connection.close()

perform_crud()