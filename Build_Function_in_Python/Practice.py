# practices bonus:
# Request 1: Nhập vào 1 dãy số nguyên, xây dựng hàm cho biết số lượng số chẵn trong list
# Request 2: NHập vào 1 dãy số nguyên, xây dựng hàm sắp xếp dãy số và trả về list mới.

# Request 1:
sequenceNumbers = []
n = -1

while True:
    try:
        n=int(input('Enter a positive integer as the number of elements: '))
    except:
        print('You entered incorrectly!! Please, re-enter 🤬🤬🤬')
    if n > 0:
        break
def enterNumbers(n, sequenceNumbers):
    for i in range(n):
        sequenceNumbers.append(int(input('Enter second numbers:' + str(i) + ' is: ')))
def countNumbers(sequenceNumbers):
    countEvenNumbers = 0
    countOddNumbers = 0
    for i in sequenceNumbers:
        if i % 2 == 0:
            countEvenNumbers = countEvenNumbers + 1
        else:
            countOddNumbers = countOddNumbers + 1

    return (countEvenNumbers, countOddNumbers)
enterNumbers(n, sequenceNumbers)
countNumbers(sequenceNumbers)
print('Quantity of even numbers and odd number :' + str(countNumbers(sequenceNumbers)))

# Request 2:
sequenceNumbers = []
n = -1
while True:
    try:
        n = int(input('Enter a positive integer as the number of elements: '))
    except:
        print('You entered incorrectly!! Please, re-enter ')
    if n > 0:
        break
def enterNumbers(n, sequenceNumbers):
    for i in range(n):
        sequenceNumbers.append(int(input('Enter the number: ')))

def sortNumbers(sequenceNumbers):
    sequenceNumbers.sort()
    return(sequenceNumbers)
enterNumbers(n, sequenceNumbers)
sortNumbers(sequenceNumbers)

newList = []
smallToLarge = sortNumbers(sequenceNumbers)
newList.append(smallToLarge)
print('This is a sorted list of numbers: ', newList)
