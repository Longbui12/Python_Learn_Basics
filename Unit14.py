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
studentList = ["Peter", "Rush" , "Micheal", "Obama", "Trump", "Biden" , "Clinton", "Snoop-dogg",'Joinwick', 'Joincena','Rechar','Monica']
"""
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
studentList.append('Taylor')
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
print('Count :', studentList.count('Taylor'))
"""
# in /Check in data inside List :
"""
if 'Monica' in studentList :
   # studentList.remove('Rush')
    print('List students current for have your name :', studentList)
else :
    print('The current student list does not have this data !! 🧨💢')

# remove() data in list : delete by value list : 
studentList.remove('Rush')
print('List students present :' , studentList)

if 'Peter' in studentList:
    studentList.remove('Peter')
    print('Remove completed :', studentList)
else: 
    print('Remove failed')
"""
# POP() : delete by position  :
studentList.pop(0)
print(studentList)

# reverse(): Reverse the list from last to first :
studentList.reverse()
print('StudentList use reverse() :' ,studentList)

# sort() : sort alphabetically or numerically in ascending order :sắp xếp theo thứ tự bảng chữ cái or số thứ tự tăng dần :
studentList.sort()
print('SORT() :', studentList)

numbers = [7,6,3,5,10,200, 51, 45]
numbers.sort()
print('Numbers :', numbers)

# kết hợp sort() & reverse() : sắp xếp theo hướng ngược lại (số từ lớn về nhỏ), 
numbers.sort(reverse= True)
print('Numbers :', numbers)

print('Length of the list :',len(studentList))
studentList.sort(reverse= True)
print('studentList :', studentList)

# clear() => Delete all data in lists :
studentList.clear()
print('Delete all list :', studentList)

