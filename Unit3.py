# Unit 3: introduce about command "PRINT" 

# Types of print :
print()
print(5)
print('This is my test !!!')
print('My , name , is')
print('Heeloo, oosssls') ; print('hi , guys')
print(6); print("Code Demo")
print('my', 'name', 'is', 'teo')
print('my', 'name', 'is', 'teo', 12345)
print('my', 'name', 'is', 'teo' ,12345, sep=' ') # when use sep (khoảng cách các chữ  : , /n )
print('my', 'name', 'is', 'teo' ,12345, sep=',')
print('my', 'name', 'is', 'teo' ,12345, sep='\n')
print('my', 'name', 'is', 'teo', end=' ')
print('my', 'name', end=' : ') # when use end (khoảng cách các chữ  : , /n )
print('is Peter')

print('firsname = {0}, lastname = {1}'.format('peter','chang'))


#######################################
a= 2 
print('a={0}'.format(a)) ; print("a=",a)

# add "f" version python 3.6 grow-up
firstName = 'NGUYEN'
lastName = 'VAN A'
print(f'Hello {firstName} {lastName}')

#example about .format()
print("{} is a good option for beginners in python".format("Edureka"))

my_string = "{} is a good option for beginners in python"
print(my_string.format("Edureka"))
