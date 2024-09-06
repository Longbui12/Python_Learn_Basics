# Introduce 'LAMBDA' function:
# Theory about LAMBDA ==> Lambda function is used to write short functions without much calculation to save code time and save code amount (if using if else or try except etc. is complicated, don't use lambda function).
# Syntax:
# lambda arguments: expression

# Ex1:
checkEven = lambda a : (a%2 == 0)
print(checkEven(10))
print(checkEven(5))

# Ex2:
total = lambda a, b : a + b
print(total(5,10))
print(total(-5,2))

# Ex3: Review functions :
def total(a,b):
    return a+b
print(total(5,10))
print(total(5,-10))

# Ex4 : example about use to LAMBDA function inside functions:
def exponentialFunctionTwo(a):
    return a**2

def TripleExponentialFunction(a):
    return a**3

print('------------------------------------')

def exponentialFunction(n):
    return lambda x : x**n

exponentialFunction2= exponentialFunction(2)
exponentialFunction3= exponentialFunction(3)
exponentialFunction4= exponentialFunction(4)

print(exponentialFunction2(3))
print(exponentialFunction3(3))
print(exponentialFunction4(3))

# TOi VE NHO XEM LAI ON TAP VE LAMBDA FUNCTION VA BAI GIOI THIEU VE FUNCTION TRUOC DO.😀😀😀