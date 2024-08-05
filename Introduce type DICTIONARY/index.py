# example :
students = {
    'fullName': 'Nguyen Van A',
    'codeClass': 'Dh01',
    'mediumScore': 8.5,
    'id': 1
}
print(students)
print(students['id'])
print(students['fullName'])

# Use GET() to take values :
print(students.get('codeClass'))

# Change values: can change 1 or more values :
students['mediumScore'] = 9.0
print(students)

students.update({'codeClass': 'Dh02'})
print(students)

students.update({'codeClass': 'Dh02', 'mediumScore':9.5})
print(students)

# add items : can add 1 or more values
students['age'] = 20
print(students)

students.update({'placeOfBirth': 'Da Nang city', 'schoolYear': 2024})
print(students)

# Remove items : method {pop(), popitem(), del}:
students.pop('placeOfBirth')
print(students)

students.popitem()
print(students)

del students['fullName'] 
print(students)

del students # delete all students
print(students)

studentss = {
    'fullName': 'Nguyen Van B',
    'codeClass': 'Dh11',
    'mediumScore': 6.5,
    'id': 2
}

# Method Clear() : delete all data
print(studentss)

studentss.clear()
print(studentss)

# get all values in Dictionary, one by one :
for x in studentss:
    print(x) 

print('-------------------------------')
# Browse value :
for x in studentss.values():
    print(x) 

print('-------------------------------')
# Browse key:
for x in studentss.keys():
    print(x) 

print('-------------------------------')
# Browse keys and values :
for x, y in studentss.items():
    print(x , y)