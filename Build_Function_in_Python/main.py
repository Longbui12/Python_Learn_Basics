# # Create a function:
# def hello():
#     print('Hello !')

# hello()
# # Arguments are enclosed in parentheses ():
# def whatSup(fullName):
#     print('Hello World: ' + fullName)
# whatSup('Mr.Peter_Chang')
# whatSup('Mrs.Linda_ngo')

# # multiple arguments, Each argument is separated by a comma:
# def hi(firstName, middleName, lastName):
#     print('Hi: ' + firstName + middleName + lastName)
#     print('Hi: ' + firstName)
# hi('Bui','Hai','Long')

# # When the number of arguments is unknown, we can use * :
# def timetable(*subject):
#     print('subject 1: ' + subject[0])
#     print('subject 2: ' + subject[1])
#     print('subject 3: ' + subject[2])
#     print('subject 4: ' + subject[3])

# timetable('Math', 'History','Physics', 'Literature', 'Chemistry')

# # Example : 
# def total(*value):
#     sum = 0
#     for x in value:
#         sum = sum + x
#     print(sum)

# total(1,2)
# total(1,3,2,5,6,8)

# # Pass multiple arguments, identified by name, use ** :
# def welCome(**fullName):
#     print('Welcome : ' + fullName['firstName'])
# welCome(firstName= 'Mr.Chang', middleName = 'justin', lastName= 'bieber')
# welCome(middleName = 'justin', lastName= 'bieber', firstName= 'Mr.Chang')

# # Use key 'return' to return value :
# def tinhTich(*value):
#     tich = 1
#     for x in value:
#         tich = tich * x

#     return tich

# tich1 = tinhTich(1,4,6)
# tich2 = tinhTich(3,4,6)
# tong = tich1 + tich2
# print(tong)

# print('=======================================')
# # Practice about Fucntion:
# # tìm ước số chung lớn nhất của hai số tự nhiên a, b :
# # Xây dựng hàm: gcb(a,b) => trả về ước số chung lớn nhất
# # Ví dụ: 1 , 13 => gcd(1,13)=> 1
# # Ví dụ: 35,77 => gcd(35,77)=>
# # Thuật toán đơn:
# # 35, 42
# # 35, 7
# # 28,7
# # 21,7
# # 14,7
# # 7,7

# def gcb(a,b):
#     while (a!= b):
#         if(a>b):
#             a = a - b
#         else:
#             b= b - a
#     return a
# print(gcb(55,100)) 
# print(gcb(11,121)) 
# print('=======================================')

# # Bài tập 2:
# # Nhập vào một dãy (n) số từ bàn phím, sau đó tính tổng 
# # Yêu cầu: 
# # 1) Xây dựng các hàm :
# # nhap(n, list_number)
# # tinhTong(list_number)
# # Giải : 
# # Khai báo biến (variable):
# list_number = []
# n = -1
# # Nhập cho đến khi nào n >= 1
# while(True):
#     try:
#       n = int(input('Nhập vào số lượng phần tử: ')) 
#     except:
#       print("Vui lòng nhập n >= 1")
#     if (n>=1):
#         break

# # Hàm nhập()
# def nhap(n, list_number):
#     for i in range(n):
#         list_number.append(int(input('Nhập vào giá trị thứ ' + str(i) + ' : ')))

# # Hàm tính tổng:
# def tinhTong(list_number):
#     tong = 0
#     for x in list_number:
#         tong += x
#     return tong

# nhap(n, list_number)
# print('Tổng = ' + str(tinhTong(list_number)))

# Bài tập thêm:
# Bài 1: Nhập vào 1 dãy số nguyên, xây dựng hàm cho biết số lượng số chẵn trong list
# Bài 2: NHập vào 1 dãy số nguyên, xây dựng hàm sắp xếp dãy số và trả về list mới.
# Phải xem lại 2 bài tập làm ở dưới cùng rồi làm lại
# giải bài tập làm thêm số 1:
dayso = []
n = -1
while True:
  try:
    n = int(input("nhập vào số nguyên dương là số lượng phần tử: "))
  except:
    print("bạn đã nhập sai")
  if n> 0:
    break
def nhapso (n, dayso):
  for i in range (n):
    dayso.append(int(input("nhập số thứ: " + str(i) + " là: ")))
def demso(dayso):
  demchan =0
  demle =0
  for i in dayso:
    if i%2 == 0:
      demchan = demchan+1
    else:
      demle = demle + 1
  return(demchan,demle)
nhapso(n,dayso)
demso(dayso)
print("tổng số lượng của số chẵn và tổng số lượng của số lẻ là: " + str(demso(dayso)))

# Bài tập 2:

dayso = []
n = -1
while True:
  try:
    n = int(input("nhập vào số nguyên dương là số lượng phần tử: "))
  except:
    print("bạn đã nhập sai")
  if n> 0:
    break
def nhapso (n, dayso):
  for i in range (n):
    dayso.append(int(input("nhập số thứ: ")))
def sapxep(dayso):
  dayso.sort()
  return(dayso)
nhapso (n, dayso)
sapxep(dayso)
listmoi = []
nhodenlon = sapxep(dayso)
listmoi.append(nhodenlon)
print(listmoi)