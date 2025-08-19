from class_file.student import Student
from class_file.course import Course    
from class_file.grade import Grade
from operation.operations import add_student, add_course, add_grade, get_student_performance
print("Welcome to the Student Management System")
print("You can perform the following operations:")
print("1. Add Student")
print("2. Add Course")  
print("3. Add Grade")
print("4. Get Student Performance")
user_input = input("Enter operation (1-4): ")
if user_input == "1":
    student_id = input("Enter Student ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    add_student(student_id, first_name, last_name, email)
if user_input == "2":
    course_id = input("Enter Course ID: ")
    course_name = input("Enter Course Name: ")
    instructor = input("Enter Instructor Name: ")
    add_course(course_id, course_name, instructor)
if user_input == "3":
    student_id = input("Enter Student ID: ")
    course_id = input("Enter Course ID: ")
    marks = input("Enter Marks: ")
    add_grade(student_id, course_id, marks)
if user_input == "4":
    student_id = input("Enter Student ID to get performance: ")
    performance = get_student_performance(student_id)
    print(f"Performance of Student ID {student_id}: {performance}")




