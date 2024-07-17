# Nhap n (n > 0)
n = -2
while ( n <= 0):
    n = int(input("Nhap vao n > 0: "))

# Chuyen tu thap phan sang nhi phan
x = n
ketQua = ""
while(n > 0):
   ketQua = str(n%2) + ketQua
   print("n % 2 = ", n % 2)
   n = n // 2
   print("n = ", n )
print("Ket qua :", ketQua)
