"""
Đề bài :
Yêu cầu người dùng nhập một con số n>0 .
Nếu nhập sai thì yêu cầu người dùng nhập lại .
"""

n = -1 
while (n <= 0 ):
    n = int(input("Nhập vào n : "))

# Ex 2:
i = 0
tong = 0
while (i <= n):
    tong += i # tong = tong + i
    i += 1 # i = i + 1
print('Tổng = ', tong)

# Ex 3:
j = 0
while(j <= 10):
    print(j, 'Bên trong vòng lặp')
    j+= 1
else:
    print(j, 'Bên ngoài vòng lặp')

# Ex 4:
j = 0
while(j <= 10):
    print(j, 'Bên trong vòng lặp')
    j+= 1
    if (j>=5):
        break
else:
    print(j, 'Bên ngoài vòng lặp')