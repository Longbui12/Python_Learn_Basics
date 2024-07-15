# Bài tập chuyển từ hệ thập phân sang hệ nhị phân :
# Nhập n (n > 0)
n = -1
while (n <= 0):
    n = int(input("Nhập vào n > 0 :"))

# Thuật toán : Chuyển từ thập phân sang nhị phân :
x = n
ketQua = ""
while (n > 0):
   ketQua = str(n % 2) + ketQua
   print('n % 2 =', n % 2)
   n = n // 2
   print('n = ', n )

print('kết quả :', ketQua)

# ôn tập lại thuật toán chuyển từ thập phân sang nhị phân 