def printAll(values):
    for item in values:
        print(item)
# SQL = 'SELECT * FROM students'
SQL = 'SELECT * FROM students ORDER BY student_code DECS'
cursor.execute(SQL)
values = cursor.fetchall()
# cursor.close()
printAll(values)