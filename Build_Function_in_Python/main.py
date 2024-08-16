# Create a function:
def hello():
    print('Hello !')

hello()
# Arguments are enclosed in parentheses ():
def whatSup(fullName):
    print('Hello World: ' + fullName)
whatSup('Mr.Peter_Chang')
whatSup('Mrs.Linda_ngo')

# multiple arguments, Each argument is separated by a comma:
def hi(firstName, middleName, lastName):
    print('Hi: ' + firstName + middleName + lastName)
    print('Hi: ' + firstName)
hi('Bui','Hai','Long')

# When the number of arguments is unknown, we can use * :
def timetable(*subject):
    print('subject 1: ' + subject[0])
    print('subject 2: ' + subject[1])
    print('subject 3: ' + subject[2])
    print('subject 4: ' + subject[3])

timetable('Math', 'History','Physics', 'Literature', 'Chemistry')

# Example : 
def total(*value):
    sum = 0
    for x in value:
        sum = sum + x
    print(sum)

total(1,2)
total(1,3,2,5,6,8)

# Pass multiple arguments, identified by name, use ** :
def welCome(**fullName):
    print('Welcome : ' + fullName['firstName'])
welCome(firstName= 'Mr.Chang', middleName = 'justin', lastName= 'bieber')
welCome(middleName = 'justin', lastName= 'bieber', firstName= 'Mr.Chang')

# Use key 'return' to return value :
def tinhTich(*value):
    tich = 1
    for x in value:
        tich = tich * x

    return tich

tich1 = tinhTich(1,4,6)
tich2 = tinhTich(3,4,6)
tong = tich1 + tich2
print(tong)

print('=======================================')
# Practice about Fucntion:
# tìm ước số chung lớn nhất của hai số tự nhiên a, b :
# Xây dựng hàm: gcb(a,b) => trả về ước số chung lớn nhất
# Ví dụ: 1 , 13 => gcd(1,13)=> 1
# Ví dụ: 35,77 => gcd(35,77)=>
# Thuật toán đơn:
# 35, 42
# 35, 7
# 28,7
# 21,7
# 14,7
# 7,7

def gcb(a,b):
    while (a!= b):
        if(a>b):
            a = a - b
        else:
            b= b - a
    return a
print(gcb(55,100)) 
print(gcb(11,121)) 
print('=======================================')

# Bài tập 2:
# Nhập vào một dãy (n) số từ bàn phím, sau đó tính tổng 
# Yêu cầu: 
# 1) Xây dựng các hàm :
# nhap(n, list_number)
# tinhTong(list_number)





