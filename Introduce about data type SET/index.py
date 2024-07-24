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

# Thêm list vào SET:
hocOnThi = ['Võ thuật', 'Kịch', 'Võ thuật']
print(hocOnThi)
monHoc.update(hocOnThi)
print(monHoc)