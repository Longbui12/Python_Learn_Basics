# Loop 'FOR' in python :

# example 1 : loop to 0 come <n
# i ==> index

# for i in range(10):
#   print(i)
#   print(i, end=' ') # add (end=' ') để các số được xếp theo 1 hàng (tham khảo lại end() : Unit3.py)

# example 2 => 
n = 10   
for i in range (n) :
  print(i)

# example 3 : Tính tổng từ 0 => n  , mỗi lần tăng lên 1 đơn vị :
n = int(input('Please enter number in here : '))
tong = 0
for i in range (n+1):
    tong += i
print('Tong =', tong)

# Loop FOR , có bước tăng tùy chỉnh :
for i in range(0, 10, 2 ): # giải thích trong ngoặc là i đi từ 0 đến 10 mỗi lần tăng lên 2 .
   print(i)
   

# Loop FOR , có bước giảm tùy chỉnh :
for i in range(10,0, -2):# giải thích trong ngoặc là i đi từ 10 về 0 mỗi lần giảm -2 .
   print(i)

# Loop FOR , lấy cac phần tử trong list :
colors = ['RED', 'PINK', 'PURPLE', 'YELLOW', 'BLACK','WHITE']
for color in colors:
   print(color, end=' /')

# Loop FOR , duyệt các phần tử theo vị trí :
for i in range(len(colors)):
    print(colors[i])