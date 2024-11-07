# # import library:
# import mysql.connector

# # connect to database by path to this file :
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="managestudentlist"
# )
# print(mydb)

# disconnect:
#mydb.close()

# Create object cursor:
# cursor = mydb.cursor()

# # create command SQL :
# sql= 'SELECT * FROM students'
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)

# SELECT :
# sql= 'SELECT * FROM students WHERE students.average_score >= 8'
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
# cursor.close()

# INSERT
# sql = 'INSERT INTO students(student_code, full_name, average_score) VALUES("18","Lu thi le", 5.5)'
# cursor.execute(sql)
# # Commit the transaction
# cursor._connection.commit()
# cursor.close()
# result = cursor.fetchall()
# print(result)

# UPDATE :
# sql = 'UPDATE students SET average_score=average_score + 1 WHERE student_code = 1 ' # Update average_score for all students
# # sql = 'UPDATE students SET average_score=average_score - 1 WHERE student_code = 1 ' # Update average_score for ID of student
# cursor.execute(sql)
# # Commit the transaction
# cursor._connection.commit()
# cursor.close()

# DELETE :
# sql = 'DELETE FROM students WHERE average_score >= 10 ' # Update average_score for all students
# cursor.execute(sql)
# # Commit the transaction
# cursor._connection.commit()
# cursor.close()

# create fuction print out each line:
# def printAll(result):
#   for item in result:
#     print(item)

# create command SQL :
# sql= 'SELECT * FROM students'
# sql= 'SELECT * FROM students ORDER BY student_code DESC'# or ESC
# cursor.execute(sql)
# result = cursor.fetchall()
# cursor.close()

# printAll(result)