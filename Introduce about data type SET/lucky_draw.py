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

    selectofCustomer = int(input('Select :'))
    if(selectofCustomer == 1):
       phoneNumber = input('Enter the prize phone numberEnter the prize phone number :')
       voteBox.discard(phoneNumber)
    elif(selectofCustomer == 2): 
       phoneNumber = input('Enter the prize phone number to be deleted :')
       voteBox.add(phoneNumber)
    elif(selectofCustomer == 3):
     i = random.randint(0, len(voteBox))
     print('Congratulations on ' + voteBox[i] + 'the winning phone number')
     voteBox.discard(voteBox[i])
    else:
        break
x = input('Enter any key to continue !')
