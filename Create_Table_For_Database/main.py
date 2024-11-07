# import mysql.connector

# # connect with database :
# connectDB = mysql.connector.connect (
#     host = "localhost",
#     user = 'root',
#     password = '',
#     database = 'student_list_example',
#     autocommit= True,
#     # connection_timeout= 300
# )
# print('This is my DB :', connectDB)

# # Create information about table class :
# # -) Steps to create a table :
# # +) Create table:
# # c is cursor
# c = connectDB.cursor()

# # Delete the table if it already exists:
# c.execute('DROP TABLE IF EXISTS class_students')
# c.execute('DROP TABLE IF EXISTS students')
# # Create table:
# mySQL = '''
#     CREATE TABLE class_students (
#         class_code varchar(50) NOT NULL PRIMARY KEY,
#         class_name varchar(255) NULL DEFAULT NULL
#     )
# '''
# c.execute(mySQL)

# # INSERT data :
# mySQL = '''
#     INSERT INTO class_students(class_code, class_name)
#     VALUES 
#         ('Python', 'Python programing'),
#         ('Java', 'Java and Kotlin programing Android'),
#         ('Javascript','Javascript programing website')
# '''
# c.execute(mySQL)
# # c._connection.commit()

# # try:
# #     # Code to create tables and insert data here
# #     c.execute(mySQL)
# #     connectDB.commit()
# # except mysql.connector.Error as err:
# #     print("Error: {}".format(err))

# # ================================================================== #
# # Create information about table student :
# # c is cursor
# # c = connectDB.cursor()

# # Delete the table if it already exists:
# # c.execute('DROP TABLE IF EXISTS students')
# # Create table:
# mySQL = '''
#     CREATE TABLE students (
#         student_code varchar(50) NOT NULL PRIMARY KEY,
#         fullname varchar(255) NULL DEFAULT NULL,
#         date_of_birth date NULL DEFAULT NULL,
#         class_code varchar(255) NOT NULL,
#         FOREIGN KEY (class_code) REFERENCES class_students(class_code) 
#         ON DELETE CASCADE ON UPDATE CASCADE
#     )
# '''
# c.execute(mySQL)

# # INSERT data :
# mySQL = '''
#     INSERT INTO students(student_code, fullname, date_of_birth, class_code)
#     VALUES 
#         ('SS01001', 'Bui VAN A', '2001-09-08','Javascript'),
#         ('SS01112', 'Lý THI B', '1997-07-11','Python'),
#         ('SS01123', 'Trương THANH C', '2004-12-27','Java');
#     '''
# c.execute(mySQL)
# c._connection.commit()

# # Close the cursor and connection
# c.close()
# connectDB.close()
# # try:
# #     # Code to create tables and insert data here
# #     c.execute(mySQL)
# #     c._connection.commit()
# # except mysql.connector.Error as err:
# #     print("Error: {}".format(err))

# ===================================================================== #

# import mysql.connector

# # Connect with the database
# connectDB = mysql.connector.connect(
#     host="localhost",
#     user='root',
#     password='',
#     database='student_list_example',
#     autocommit=True
# )
# print('This is my DB:', connectDB)

# # Create a cursor object
# c = connectDB.cursor()

# # Step 1: Drop the tables if they exist
# try:
#     c.execute('DROP TABLE IF EXISTS students')
#     c.execute('DROP TABLE IF EXISTS class_students')
#     print("Dropped existing tables.")   
# except mysql.connector.Error as err:
#     print("Error dropping tables: {}".format(err))

# # Step 2: Create class_students table
# try:
#     mySQL = '''
#         CREATE TABLE class_students (
#             class_code varchar(50) NOT NULL PRIMARY KEY,
#             class_name varchar(255) NULL DEFAULT NULL
#         )
#     '''
#     c.execute(mySQL)
#     print("Created class_students table.")
# except mysql.connector.Error as err:
#     print("Error creating class_students table: {}".format(err))

# # Step 3: Insert data into class_students
# try:
#     mySQL = '''
#         INSERT INTO class_students(class_code, class_name)
#         VALUES 
#             ('Python', 'Python programming'),
#             ('Java', 'Java and Kotlin programming Android'),
#             ('Javascript', 'Javascript programming website')
#     '''
#     c.execute(mySQL)
#     print("Inserted data into class_students.")
# except mysql.connector.Error as err:
#     print("Error inserting data into class_students: {}".format(err))

# # Step 4: Create students table
# try:
#     mySQL = '''
#         CREATE TABLE students (
#             student_code varchar(50) NOT NULL PRIMARY KEY,
#             fullname varchar(255) NULL DEFAULT NULL,
#             date_of_birth date NULL DEFAULT NULL,
#             class_code varchar(255) NOT NULL,
#             FOREIGN KEY (class_code) REFERENCES class_students(class_code) 
#             ON DELETE CASCADE ON UPDATE CASCADE
#         )
#     '''
#     c.execute(mySQL)
#     print("Created students table.")
# except mysql.connector.Error as err:
#     print("Error creating students table: {}".format(err))

# # Step 5: Insert data into students
# try:
#     mySQL = '''
#         INSERT INTO students(student_code, fullname, date_of_birth, class_code)
#         VALUES 
#             ('SS222', 'Bui VAN TEP', '2002-03-18', 'Java'),
#             ('SS034', 'Lý THI TEO', '1990-01-01', 'Javascript'),
#             ('SS01', 'Trương THANH D', '2000-12-31', 'Python');
#     '''
#     c.execute(mySQL)
#     print("Inserted data into students.")
# except mysql.connector.Error as err:
#     print("Error inserting data into students: {}".format(err))

# # Commit the changes
# connectDB.commit()

# # Close the cursor and connection
# c.close()
# connectDB.close()


#================================================== #
import mysql.connector

# Connect with the database
connectDB = mysql.connector.connect(
    host="localhost",
    user='root',
    password='',
    database='student_list_example',
    autocommit=True
)
print('This is my DB:', connectDB)

# Create a cursor object
c = connectDB.cursor()

# Step 1: Create class_students table if it doesn't exist
try:
    mySQL = '''
        CREATE TABLE IF NOT EXISTS class_students (
            class_code varchar(50) NOT NULL PRIMARY KEY,
            class_name varchar(255) NULL DEFAULT NULL
        )
    '''
    c.execute(mySQL)
    print("Created class_students table if it didn't exist.🚀🚀🚀")
except mysql.connector.Error as err:
    print("Error creating class_students table: {}".format(err))

# Step 2: Insert data into class_students if it doesn't exist
try:
    mySQL = '''
        INSERT INTO class_students(class_code, class_name)
        VALUES 
            ('Python', 'Python programming'),
            ('Java', 'Java and Kotlin programming Android'),
            ('Javascript', 'Javascript programming website')
        ON DUPLICATE KEY UPDATE class_name = VALUES(class_name);
    '''
    c.execute(mySQL)
    print("Inserted data into class_students or updated existing records.")
except mysql.connector.Error as err:
    print("Error inserting data into class_students: {}".format(err))

# Step 3: Create students table if it doesn't exist
try:
    mySQL = '''
        CREATE TABLE IF NOT EXISTS students (
            student_code varchar(50) NOT NULL PRIMARY KEY,
            fullname varchar(255) NULL DEFAULT NULL,
            date_of_birth date NULL DEFAULT NULL,
            class_code varchar(255) NOT NULL,
            FOREIGN KEY (class_code) REFERENCES class_students(class_code) 
            ON DELETE CASCADE ON UPDATE CASCADE
        )
    '''
    c.execute(mySQL)
    print("Created students table if it didn't exist.🧨🧨🧨")
except mysql.connector.Error as err:
    print("Error creating students table: {}".format(err))

# Step 4: Insert data into students if it doesn't exist
try:
    mySQL = '''
        INSERT INTO students(student_code, fullname, date_of_birth, class_code)
        VALUES 
            ('SS001', 'Bui VAN TY', '2002-03-18', 'Java'),
            ('SS0333', 'Lý THI Lam', '1990-01-01', 'Javascript'),
            ('SS01999', 'Trương THANH Dung', '2000-12-31', 'Python')
        ON DUPLICATE KEY UPDATE fullname = VALUES(fullname), date_of_birth = VALUES(date_of_birth), class_code = VALUES(class_code);
    '''
    c.execute(mySQL)
    print("Inserted data into students or updated existing records.")
except mysql.connector.Error as err:
    print("Error inserting data into students: {}".format(err))

# Commit the changes
connectDB.commit()

# Close the cursor and connection
c.close()
connectDB.close()

