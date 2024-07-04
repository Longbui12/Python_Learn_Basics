# Comparison operator & logic in Programing Python :

# Comparison operator (true or false)
print('Example about compare !!!👌👌👌')
x = int(input('x : '))
y= int(input('y : '))
print('{0}<{1} be {2}'.format(x,y, x < y))
print('{0}>{1} be {2}'.format(x,y, x > y))
print('{0}=={1} be {2}'.format(x,y, x == y))
print('{0}<={1} be {2}'.format(x,y, x <= y))
print('{0}>={1} be {2}'.format(x,y, x >= y))
print('{0}!={1} be {2}'.format(x,y, x != y))

# operator Logic : (and , or , not)
print('Example about logic !!!👌👌👌')
z = int(input("z : "))
print("({0}<{1}) and {2}<{3} = {4}".format(x,y,y,z, (x < y) and (y < z)))
print("({0}<{1}) or {2}<{3} = {4}".format(x,y,y,z, (x < y) or (y < z)))
print("not ({0}>{1}) = {2}".format(x,z,not (x > z)))