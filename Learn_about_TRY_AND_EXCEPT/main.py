# Theory :   
#try:
  # Đoạn code dự đoán có lỗi 
#except:
  # Hành động khi lỗi xảy ra
#else:
  # Thực thi đoạn này nếu như mã không có lỗi
#finally:
  # Cho phép thực thi code, bất kể kết quả của các khối try có bị lỗi hay không

# Example :
a = int(input('Nhập vào số nguyên a: '))
print(str(a) + ' + 5' + str(a + 5))

# ex1:
try:
  a = int(input('Nhập vào số nguyên a: '))
  print(str(a) + ' + 5' + str(a + 5)) 
except :
  print('Bạn đã nhập sai dữ liệu')

# ex2: add EXCEPTION
try:
  a = int(input('Nhập vào số nguyên a: '))
  print(str(a) + ' + 5' + str(a + 5)) 
except Exception as e:
  print(e)

# ex3:
try:
  a = int(input('Nhập vào số nguyên a: '))
  print(str(a) + ' + 5' + str(a + 5)) 
except Exception as e:
  print(e)
else:
  print('Không có lỗi xảy ra')
finally:
  print('Kết thúc chương trình !!! 👌👌')