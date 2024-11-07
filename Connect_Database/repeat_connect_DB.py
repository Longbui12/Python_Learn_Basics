# # connect DB:
# import mysql.connector


# # Connect to database by path to this file :
# try:
#     myDB = mysql.connector.connect(
#       host = 'localhost',
#       user = 'root',
#       password = '',
#       # password = 'ToilaTeo123456@@',
#       database = 'managestudentlist'
#     )
#     if myDB.is_connected():
#         print('Database is running:', myDB)
# except mysql.connector.Error as err:
#     print(f'Error : {err}')
#     myDB = None
# finally:
#     if mysql.():
#         myDB.close()
#         print('Database is closed .👌👌👌')

import mysql.connector

# Connect to the database
try:
    myDB = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='managestudentlist'
    )
    if myDB.is_connected():
        print('Database is running:', myDB)
except mysql.connector.Error as err:
    print(f'Error: {err}')
    # myDB = None  # Ensure myDB is None if connection fails
# finally:
#     # if myDB is not None and myDB.is_connected():
#     if myDB is not myDB.is_connected():
#         myDB.close()
#         print('Database is closed. 👌👌👌')
#     else:
#         print('Database was not connected, so it is closed. 👌👌👌')






# # Establishing the connection
# try:
#     connection = mysql.connector.connect(**myDB)
#     if connection.is_connected():
#         print("Connected to the database successfully.")
# except mysql.connector.Error as err:
#     print(f"Error: {err}")
# finally:
#     if connection.is_connected():
#         connection.close()
#         print("Connection closed.")


# ===================================================================
# import mysql.connector

# # Connect to database
# try:
#     myDB = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='ToilaTeo123456@@',  # Ensure this password is correct
#         database='managestudentlist'
#     )
    
#     # Check if the connection is successful
#     if myDB.is_connected():
#         print("Connected to the database successfully.")
    
# except mysql.connector.Error as err:
#     print(f"Error: {err}")

# finally:
#     # Close the connection if it was established
#     if 'myDB' in locals() and myDB.is_connected():
#         myDB.close()
#         print("Connection closed.")

# Create object cursor:
cursor = myDB.cursor()

# SELECT :
# SQL = 'SELECT * FROM students'
# # SQL = 'SELECT * FROM students WHERE students.student_code = 7'
# cursor.execute(SQL)
# result = cursor.fetchall()
# print('This is my :', result)
# cursor.close()

# INSERT :
# SQL = 'INSERT INTO students(student_code, full_name, average_score) VALUES ("", "MR.PETER_CHANG", "9.5")'
# cursor.execute(SQL)
# cursor._connection.commit()
# cursor.close()
# result = cursor.fetchall()
# print('This is my :', result)

# UPDATE :
# SQL = "UPDATE students SET student_code = student_code + 1 "
# cursor.execute(SQL)
# cursor._connection.commit()
# cursor.close()

# DELETE :
# SQL = 'DELETE FROM students WHERE student_code = -5'
# cursor.execute(SQL)
# cursor._connection.commit()
# cursor.close()

# create function :
def printAll(values):
    for item in values:
        print(item)
SQL = 'SELECT * FROM students'
# SQL = 'SELECT * FROM students ORDER BY student_code DECS'
cursor.execute(SQL)
values = cursor.fetchall()
# cursor.close()
printAll(values)

