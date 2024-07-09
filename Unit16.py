# Sometime Types in Python :
a = 10
print(type(a))

b = 'Hello world'
print(type(b))

c = 10.5
print(type(c))

d = True
print(type(d))

# Type String in Python :
# ex1 : Cộng chuỗi
s1 = 'Xin chào'
s2 = 'Peter'
s3 = s1 + ' ' +s2
print('Result :', s3)

# ex2 :Tạo Chuỗi nhiều dòng : """ """
chuoi_nhieu_dong = """
Dòng 1
Dòng 2
Dòng 3
"""
print(chuoi_nhieu_dong)

# ex3 : lặp lại chuỗi :
chep_phat =  "Tôi hứa sẽ học code đầy đủ \n"
chep_phat_10 = chep_phat * 10
print(chep_phat_10)

# ex4 : Kiểm tra chuỗi con có thuộc chuỗi khác ==>
chuoi_1 = 'Hello world Welcome'
chuoi_2 = 'Welcome'
chuoi_3 = 'to Việt Nam'

if chuoi_2 in chuoi_1:
    print("chuỗi 2 là chuỗi con của chuỗi 1")
else:
    print("chuỗi 2 không phải là chuỗi con của chuỗi 1")

if chuoi_3 in chuoi_1:
    print("chuỗi 3 là chuỗi con của chuỗi 1")
else:
    print("chuỗi 3 không phải là chuỗi con của chuỗi 1")

# Ex5 : Viết hoa chữ cái đầu của chuỗi :
s = 'have Nice day !'
s = str.capitalize(s)
print(s)

# Ex6: Viết hoa toàn bộ chuỗi :
s = s.upper()
print(s)

# Ex7: Viết thường toàn bộ chuỗi :
s = s.lower()
print(s)

# Ex 8: Tìm và Đếm số lượng chuỗi con :
s = "Lập trình Python đang là xu hướng hiện nay. So, you need learn programing ."
print(s.find('Python'))