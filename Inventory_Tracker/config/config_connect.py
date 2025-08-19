import pymysql
def get_db_connection():
    try:
        connection=pymysql.connect(host="localhost",user="root",password="vedank10",database="inventory_tracker")
        return connection
    except pymysql.MySQLError as e:
        return f"Error connecting to the database: {e}"
    

