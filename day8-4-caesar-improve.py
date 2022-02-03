
'''
ascii_a = 97
ascii_z = 122
print(chr(ascii_a))
print(ord('a'))
print(chr(ascii_z))
'''
#refer to ASCII code, translate character to int by ord(), ascii number translate as character by chr() function

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#convert text to a list by list() function
encode_words = list(text)
encrypt=""
decrypt=""
#Iterate char from list
for encode_char in encode_words:  
    if direction =="encode":
        #encode char with shift number by caesar 
        ascii_number = ord(encode_char)+shift
        #Get mode number once ascii number great than 122
        new_position = ascii_number % 122
        if ascii_number > 122 :
            # to caculate ascii number once char with shift over 122, thus to re-caculate new position start from char a to z 
            ascii_number = new_position + 96
            encrypt += chr(ascii_number)
        else:
            encrypt += chr(ascii_number)
    elif direction =="decode":
        ascii_number = ord(encode_char)-shift
        if ascii_number < 97 :
            ascii_number = ascii_number + shift
            decrypt += chr(ascii_number)
        else:
            decrypt += chr(ascii_number)

if direction =="encode":
    print(encrypt)
elif direction == "decode":
    print(decrypt)
