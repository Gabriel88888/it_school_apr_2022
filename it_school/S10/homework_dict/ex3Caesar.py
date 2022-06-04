#3) Make a script which encrypts a string using Caesar cipher with key 20, use a function to generate a dict representing the new alphabet
#caesar {
    #     "A": "Y",
    #     "B": "Z",
    #     "C": "A"
    # }

    # def get_alphabet(key):
    #     generate new alphabet
    #     return dict with alphabet

    # def crypt(msj, key):
    #     alphabet = get_alphabet(key)
    #     return msaj criptat

    # crypt("Mesajul", 20)


import string

alphabets = string.ascii_lowercase + string.ascii_lowercase

sentence = list(input('Introduceti textul:\n').lower())

what_to_do = input('Enter encrypt to ENCRYPT, Enter decrypt to DECRYPT, exit to EXIT the program \n').lower()

shift_number = int(input('Enter your shift number from 1 to 25: \n'))

end_program = False

while not end_program:
    if what_to_do == 'encrypt':
        for i in range (len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) + shift_number
                sentence[i] = alphabets[new_letter]
        
        print(''.join(map(str, sentence)))
        end_program = True
    elif what_to_do == 'decrypt':
        for i in range(len(sentence)):
            if sentence [i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) - shift_number
                sentence[i] = alphabets[new_letter]
        print(''.join(map(str, sentence)))
        end_program = True
            