#
a = input('Please number a :')
print('Type of a :', type(a))
a = float(a)
print('Type of a :', type(a))
b = input('Please number b :')
print('Type of b :', type(b))
b=float(b)
print('Type of b :', type(b))


print('{0}+{1}={2}'.format(a, b, a + b))
print('{0}-{1}={2}'.format(a, b, a - b))
print('{0}/{1}={2}'.format(a, b, a / b))
print('{0}*{1}={2}'.format(a, b, a * b))
print('{0}%{1}={2}'.format(a, b, a % b))
print('{0}**{1}={2}'.format(a, b, a ** b))
print('{0}//{1}={2}'.format(a, b, a // b))
