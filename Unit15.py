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

# example 3 : Tính tổng từ 0 => n 
n = int(input('Please enter number in here : '))
tong = 0
for i in range (n+1):
    tong += i
print('Tong =', tong)
