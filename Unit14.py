# Types LIST in Python :
# Create list null :
emptyList = []

# Create an object list :
emptyList2 = list() 

print('check list 1 :', emptyList)
print('check list 2 :', emptyList2)

# Create a list has data :
# Example 1 :
colors = ['Red', 'Blue', 'Grey', 'Black', 'White', 'Orange', 'Navy', 'Pink', 'Violet', 'Purple', 'Green']
print('Check result :', colors)

# Example 2: 
# List [] will start : 0 to .... , to left to Right :
studentList = ["Peter", "Rush", "Rush" , "Micheal", "Obama", "Trump", "Biden" , "Clinton", "Snoop-dogg",'Joinwick', 'Joincena','Rechar','Monica']
print('Filter name in Lists :', studentList[2])
print('Filter name in Lists :', studentList[6])
print('Filter name in Lists :', studentList[:])
print('Filter name in Lists :', studentList[0 : 4])
print('Filter name in Lists :', studentList[4 : 20])

# .append()/add data in studentList : 
studentList.append('Chang')
print('New list students :', studentList)
studentList.append('Justin')
print('New list students :', studentList)

# len(): /add data to the end of the list :
studentList[len(studentList):]= ['Ti anh'] 
print('New list students :', studentList)

# .insert()/ insert data in studentList:
studentList.insert(2, 'Teo em')
print('New list students :', studentList)

# Number of elements in the list :
print('Length of the list :',len(studentList))

# count() /Count the number of elements that satisfy the condition :
print('Count :', studentList.count('Rush'))