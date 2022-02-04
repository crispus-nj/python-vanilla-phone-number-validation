'''
Write a program that gets a phone number from a form input or terminal. 
Validates the phone number by checking if it starts with 
+254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 
e.g if a user enters “0712345678”, the program should display “+254712345678”
Hint: check for substring with conditionals
'''
import sys
import os

def split(word):
    ref_number = '+254'
    string = word
    word_loop = list(word)
    if (string[0:2]== '07') or (string[0:2]== '71') or (string[0:2]== '01') or (string[0:3]== '254') or (string[0:4]== '+254'):
        if (len(word_loop) == 10) or (len(word_loop)== 13):
            if word: 
                print(type(word))
                for char in word: 
                    if char[0] != ref_number:
                        words = list(word)
                        menono = ''.join(words)
                        if (menono[0:2] == '07')or (string[0:2]== '71') or (string[0:2]== '01'):
                            maneno_mingi = list(menono)
                            maneno_mingi.pop(0)
                            wod = ''.join(maneno_mingi)
                            num_validate = int(ref_number + wod)
                            return num_validate
                        elif (menono[0:3]== '254') or (menono[0:4]== '+254'):
                            num_maneno = int(menono)
                            return num_maneno

            else :
                print("You have not enter any number!")
                print("Please enter your number")
                number = input()
                for char in number: 
                    if char[0] != ref_number:
                        words = list(number)
                        menono = ''.join(number)
                        if (menono[0:2] == '07')or (string[0:2]== '71') or (string[0:2]== '01'):
                            maneno_mingi = list(menono)
                            maneno_mingi.pop(0)
                            wod = ''.join(maneno_mingi)
                            num_validate = int(ref_number + wod)
                            return num_validate
                        elif (menono[0:3]== '254') or (menono[0:4]== '+254'):
                            num_maneno = int(menono)
                            return num_maneno

        else :
            print("Number less than required length")
            print("You have not enter any number!")
            print("Please enter your number")
            number = input()
            if (len(number) == 10) or (len(number)== 13):
                for char in number: 
                    if char[0] != ref_number:
                        words = list(word)
                        menono = ''.join(number)
                        if (menono[0:2] == '07')or (string[0:2]== '71') or (string[0:2]== '01'):
                            maneno_mingi = list(menono)
                            maneno_mingi.pop(0)
                            wod = ''.join(maneno_mingi)
                            num_validate = int(ref_number + wod)
                            return num_validate
                        elif (menono[0:3]== '254') or (menono[0:4]== '+254'):
                            num_maneno = int(menono)
                            return num_maneno

            else :
                print("Follow simple instructions")
    else :
        print("Invalid number")


try:
    print("Please enter your number")
    number = input()
    split(number)
except KeyboardInterrupt:
    print('Interrupted Keyboard')
    print("Please enter your number")
    number = input()
    split(number)
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
