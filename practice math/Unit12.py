# Practice math :
"""
import math

print("Solve the equation : ax^2 + bx + c = 0")
a = float(input("Enter a : "))
b = float(input("Enter b : "))
c = float(input("Enter c : "))

print("{0}x^2 + {1}x + {2} = 0".format(a,b,c))

if (a!= 0) :
  delta = b ** 2 - 4 * a * c
  if(delta < 0):
    print("The equation has no solution")
  elif(delta == 0):
    x = -b/(2 * a)
    print('Has double solution : x1 = x2=', x)
  else :
    x1 = (-b - math.sqrt(delta))/(2 * a)
    x2 = (-b + math.sqrt(delta))/(2 * a)
    print('Has double solution : x1 = {0} & x2= {1}' .format(x1, x2))
else:
  print('This is not a quadratic equation')

"""
# Home work : work repeat practice math in the home (so work math if you don't know , you repeat)
# Topic : ax^2 + bx - c = 0
"""
import math

print('Solve the equation : ax^2 - bx + c = 0')
a = float(input('Enter a : '))
b = float(input('Enter b : '))
c = float(input('Enter c : '))

print('{0}x^2 - {1}x + {2} = 0'.format(a, b, c))

if a != 0:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print('Phương trình có hai nghiệm phân biệt:')
        print('x1 = {0}, x2 = {1}'.format(x1, x2))
    elif delta == 0:
        x = -b/(2*a)
        print('Phương trình có nghiệm kép: x1 = x2 =', x)
    else:
        print('Phương trình không có nghiệm thực.')
else:
    print('Đây không phải là phương trình bậc hai.')
"""
import math
print("GIẢI PHƯƠNG TRÌNH BẬC 2")
a = float(input("Nhập giá trị a:"))
b = float(input("Nhập giá trị b:"))
c = float(input("Nhập giá trị c:"))
if a!=0 and (a+b+c)!=0 and (a-b+c)!=0:
    delta = b**2-4*a*c
    if delta<0:
        print("Phương trình vô nghiệm")
    elif delta==0:
        x = -b/(2*a)
        print("Phương trình có nghiệm kép x1=x2:", x)
    else:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print("Phương trình có 2 nghiệm:", "x1=", x1, "x2=", x2)
        print("Phương trình có 2 nghiệm: x1 = {0}; x2 = {1}". format(x1, x2))
elif a!=0 and (a+b+c)==0:
    x1 = 1
    x2 = c/a
    if x1==x2:
        print("Phương trình có 01 nghiệm x =", x1)
    else:
        print("Phương trình có 2 nghiệm: x1 = {0}; x2 = {1}". format(x1, x2))
elif a!=0 and (a-b+c)==0:
    x1 = -1
    x2 = -c/a
    if x1==x2:
        print("Phương trình có 01 nghiệm x =", x1)
    else:
        print("Phương trình có 2 nghiệm: x1 = {0}; x2 = {1}". format(x1, x2))    
else: print("Đây không phải là phương trình bậc 2")

