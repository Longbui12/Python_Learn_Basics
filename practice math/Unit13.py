# Exercises math :( determine details ,Calculate the perimeter and area of ​​a triangle) 
# PS : sqrt() in library Math là căn bậc 2 .

import math

xA = (float(input('Please enter data xA : ')))
yA = (float(input('Please enter data yA : ')))
xB = (float(input('Please enter data xB : ')))
yB = (float(input('Please enter data yB : ')))
xC = (float(input('Please enter data xC : ')))
yC = (float(input('Please enter data yC : ')))

ab = math.sqrt((xB - xA)**2 + (yB - yC)**2)
bc = math.sqrt((xC - xB)**2 + (yC - yB)**2)
ca = math.sqrt((xA - xC)**2 + (yA - yC)**2)

if (ab + bc > ca) and (bc + ca > ab) and (ab + ca > bc):
    print('Những số nhập vào input đã tạo thành tam giác 😍 😎 😊 😉') 
    # Tính chu vi tam giác:
    chuVi = ab + bc + ca 
    print('Chu vi của tam giác là :', chuVi)
    
    # Tính diện tích tam giác :
    p = chuVi/2
    s = math.sqrt(p*(p-ab)*(p-bc)*(p-ca))
    print('Diện tích của tam giác là :', s)

else:
    print('Những số nhập vào input không thể tạo thành tam giác 🤬 😡 🤬 😡')