import pymysql
from database.config import Host, User, Database, Password    
def get_db_connection():
    return pymysql.connect(
        host="localhost",database="student_management_system",  
        user="root", password="vedank10")



