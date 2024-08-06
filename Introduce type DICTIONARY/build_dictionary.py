# Build a dictionary, has the following functions (Users select functions through the menu):
# 1. Add a new vocabulary word (with its meaning) to the dictionary.
# 2. Look up the meaning of a vocabulary word.
# 3. Update the meaning of vocabulary.
# 4. Allows users to delete a word from the dictionary .
# 5. Allows users to delete entire vocabulary.
# 6. Allows users to print out the entire vocabulary.
# 7. Allows users to print out the entire dictionary according to the structure: 'VOCABULARY', 'MEANING'.
# 8. End program.
# ********************************************** #

dictionary = {}
while(True):
    print('Please select the function (by number): ')
    # print('''
    #    1. Add a new vocabulary word (with its meaning) to the dictionary.
    #    2. Look up the meaning of a vocabulary word.
    #    3. Update the meaning of vocabulary.
    #    4. Allows users to delete a word from the dictionary .
    #    5. Allows users to delete entire vocabulary.
    #    6. Allows users to print out the entire vocabulary.
    #    7. Allows users to print out the entire dictionary according to the structure: 'VOCABULARY', 'MEANING'.
    #    8. End program.
    # ''')
    select = int(input('Enter your selection: '))
    if(select == 1 or select == 3):
        Vocabulary = input('Please enter vocabulary: ')
        Meaning = input('Please enter meaning: ')
        dictionary[Vocabulary] = Meaning
        print('Added or updated data')

    elif(select == 2):
        Vocabulary = input('Please enter vocabulary: ')
        print('Meaning: ', dictionary[Vocabulary])
    # elif(select == 3):
    #     Vocabulary = input('Please enter vocabulary: ')
    #     Meaning = input('Please enter meaning: ')
    #     dictionary.update
    elif(select == 4):
        Vocabulary = input('Please enter vocabulary need delete: ')
        dictionary.pop(Vocabulary)
        print('Deleted data')
    elif(select == 5):
        dictionary.clear()
        print('Deleted all data')
    elif(select == 6):
        print('List of vocabulary words in the dictionary: ')
        for x in dictionary.keys():
         print(x)
    elif(select == 7):
        if(dictionary):
          print('List of vocabulary words in the dictionary: ')
          for x, y in dictionary.items():
            print(x, ':', y)
        else:
           print('Dictionary is not data')

    
    elif(select == 8):
        break
    else:
      print('Incorrect selection entered !! 🤬🤬🤬🧨🚀')




