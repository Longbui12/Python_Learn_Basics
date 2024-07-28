# Ex 1: Tạo mới SET :
monHoc = {'Toán', 'Lý', 'Hóa','Văn', 'Sử', 'Địa'}
print(monHoc)
# Duyệt các phần tử bên trong SET :
for x in monHoc:
    print(x)

# thêm 1 phần tử vào bên trong SET (dùng add):
monHoc.add('Anh văn')
print(monHoc)
monHoc.add('Anh văn')
print(monHoc)  

# thêm nhiều phần tử vào bên trong SET (dùng update):
hocThem = {'Đàn', 'Vẽ', 'Múa', 'Nhảy'}
monHoc.update(hocThem)
print(monHoc)  

# Thêm vào list SET:
hocOnThi = ['Võ thuật', 'Kịch', 'Võ thuật']
print(hocOnThi)
monHoc.update(hocOnThi)
print(monHoc)

# Xóa phần tử:
# Use remove() : nếu phần tủ ko tồn tại sẽ phát sinh lỗi.
monHoc.remove('Võ thuật') 
#Use discard : nếu phần tử không tồn tại sẽ không phát sinh lỗi.
monHoc.discard('Toán')
print(monHoc)

# Use pop(): Loại bỏ phần tử đầu tiên.
monHoc.pop()
print(monHoc)

# Use clear(): Xóa sạch các phần tử.
monHoc.clear()
print(monHoc)

del monHoc
print(monHoc)