create database student_management_system;
use student_management_system;
create table students(student_id int,first_name varchar(25),last_name varchar(25),email varchar(25));
create table courses(course_id int,course_name varchar(25),instructor varchar(25));
create table grades(student_id int,course_id int,marks int)

