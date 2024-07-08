# Practice about loop FOR :
# Exercise: Print Multiplication table (Bảng cửu chương):

# ex1 : Print Multiplication table of 2 x :
for i in range(1,11):
    print('2 x {0} = {1}'.format(i, 2 * i))


# ex2 : Print all Multiplication table : dùng vòng lặp vòng nhau :
for j in range(2 , 12):
    print('Multiplication table :', j)
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(j, i, j * i))

# Home work : again practice exercise above (loop 'FOR' & nested loop 'FOR')