# This is a customer request : 
# Build a sweepstakes program with the following functions:
# 1) Add 1 prize phone number to the box.
# 2) Remove 1 prize phone number from the box.
# 3) Randomly dial to get 1 winning phone number.

import random
# declare SET :
voteBox = set()

# use LOOP :
while(True):
    print('---- MENU ----')
    print('Please choose feature :')
    print('1 - Add 1 prize phone number to the box')
    print('2 - Remove one phone number from the prize ballot box')
    print('3 - Randomly dial to get 1 winning phone number')
    print('4 - THE END -')
    print('Current ballot box :')
    print(voteBox)

    selectofCustomer = int(input('Select : '))
    if(selectofCustomer == 1):
       phoneNumber = input('Enter the prize phone numberEnter the prize phone number : ')
       voteBox.add(phoneNumber)
    elif(selectofCustomer == 2): 
       phoneNumber = input('Enter the prize phone number to be deleted : ')
       voteBox.discard(phoneNumber)
    elif(selectofCustomer == 3):
     index = random.randint(0, len(voteBox) - 1)
     print('Winning position phone number : ' + str(index))

     i = 0
     for x in voteBox:
        if(i == index):
          break
     i = i + 1

     print('Congratulations on ' + x + 'the winning phone number')
     voteBox.discard(x)

    else:
        break
    
x = input('Enter any key to continue !')
