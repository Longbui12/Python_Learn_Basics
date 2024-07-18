# ex1 : bài tập cơ bản về vòng lặp for :
for i in range (0, 11) :
    print(i)

print('==================================')

# ex2: Câu lệnh có BREAK với vòng lặp FOR :
for i in range (0,10):
    print(i)
    if(i > 5):
        break
print('==================================')
# ex3: Cậu lệnh có BREAK với vòng lặp WHILE :
n = 100
while (n > 0):
    print(n)
    n = n // 2
    if(n < 50):
        break

# ex4: Vòng lặp lồng nhau :
for i in range(1, 10):
    for j in range(2, 10):
        print("{0}*{1}={2}".format(i, j, i*j))
        if(j>5):
            break
    print("\n")

# Ex5: dung CONTINIUE :
for i in range(0, 10):
    if(i%2 ==1):
        continue
    print(i)

