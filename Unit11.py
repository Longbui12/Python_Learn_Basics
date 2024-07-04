# Condition operator (ternary operator) in Python programing :
#x = "TRUE" if(5 > 3)else "FALSE"
#print()
"""
x = input('Please enter Number : ')
x = int(x)
Result = "even" if( x % 2 == 0 ) else "odd"
print(x , "Is number", Result)


# example 2:
y = input('Please enter in here : ')
y= int(y)
Result = "Complete" if(y / 2 == 3) else " Not complete"
print(y , ": Result ==> ", Result)
"""

# * Branch statement (if...else ) in Python :
#example 3 : (if)
z = input("Please enter integer z : ")
z = float(z)
if z > 0 :
    print(z,': is positive numbers')
    print('__________________')

# example 4:(if else)
if z % 2 == 0 :
     print(z,': is Even number')
     print('__________________')
else:
    print(z,': is Odd number')
    print('__________________')


# example 5: (if elif else)
if z >= 9 :
   print("Classification : Excellent")
elif z>=8:
  print('Classification : Good')
elif z>=7:
  print('Classification : Khá')
elif z>=6:
   print('Classification : Average')
else:
   print("Classification : You don't have enough points to pass the subject !!🐓💩💩")

# example 6: 
u = input('Please enter information : ')
u = int(u)
if u < 5:
   print('thỏa mãn điều kiện')
elif u > 5 :
   print('điều kiện có thể tạm chấp nhận')
else:
   print('Do not condition !')

print('The end programme !!👿👿')

