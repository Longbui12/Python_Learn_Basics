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
studentList = ["Peter", "Rush", "Micheal", "Obama", "Trump", "Biden" , "Clinton", "Snoop-dogg",'Joinwick', 'Joincena','Rechar','Monica']
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