from class_file.student import Student
from class_file.course import Course
from class_file.grade import Grade
from database.config_connection import get_db_connection


def add_student(student_id, first_name, last_name, email):
    connection = get_db_connection()
    cursor = connection.cursor()
    student = Student(student_id, first_name, last_name, email)
    query = "INSERT INTO students (student_id, first_name, last_name, email) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (student.student_id, student.first_name, student.last_name, student.email))
    connection.commit()
    cursor.close()
    connection.close()

def add_course(course_id, course_name, instructor):
    connection = get_db_connection()
    cursor = connection.cursor()
    course = Course(course_id, course_name, instructor)
    query = "INSERT INTO courses (course_id, course_name, instructor) VALUES (%s, %s, %s)"
    cursor.execute(query, (course.course_id, course.course_name, course.instructor))
    connection.commit()
    cursor.close()
    connection.close()

def add_grade(student_id, course_id, marks):
    connection = get_db_connection()
    cursor = connection.cursor()
    grade = Grade(student_id, course_id, marks)
    query = "INSERT INTO grades (student_id, course_id, marks) VALUES (%s, %s, %s)"
    cursor.execute(query, (grade.student_id, grade.course, grade.grade))
    connection.commit()
    cursor.close()
    connection.close()

def get_student_performance(student_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT s.first_name, s.last_name, c.course_name, g.marks
        FROM students s
        JOIN grades g ON s.student_id = g.student_id
        JOIN courses c ON g.course_id = c.course_id
        WHERE s.student_id = %s
    """
    cursor.execute(query, (student_id))
    results = cursor.fetchone()
    cursor.close()
    connection.close()
    return results if results is not None else "No records found for this student."