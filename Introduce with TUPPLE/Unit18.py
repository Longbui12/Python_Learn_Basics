# Introduce about TUPPLE :
gender = ('man', 'woman')
print(gender[0])

classes = (1,2,3,4,5,6,7,8,9,10)
print(classes[0 : 3])

fruit = ('Apple', 'Banana','Apple','Orange', 'Lemon', 'Melon', 'Coconut')
print(fruit[0: 3])

# classes[0] = 13
#ex 2 : loop with Tupple :
for x in fruit:
    print(x)

# Ex3: plus 2 Tupples:
y = (1,2,3) + (4,5,6)
print(y)

# Ex4: multiply 2 Tupples:
z = (1,2,3) * 2
print(z)

# Ex5: dò xem phần tử có trong Tupple không IN
print("boom" in fruit)

#ex 6: tính độ dài của Tupple use LEN :
x = len(fruit)
print(x)

#ex7: đếm số lượng của các phần tử trong TUPPLE :
print(fruit.count('Apple'))

print(fruit.count('Xoài'))

# ex8: search min, search max and sum:
print(min(gender))
print(max(fruit))
print(min(classes))
print(max(classes))
print(sum(classes))

# ex9: sort Tuple and move back list: 
listTc = sorted(fruit)
print(listTc)